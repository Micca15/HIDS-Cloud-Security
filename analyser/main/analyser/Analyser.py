import os
import configparser
import json

# Public config variable
config = None


class AnaSetup:
    def __init__(self, config_file):
        self.__config_file = config_file
        self.__config = configparser.ConfigParser()
        config = self.__config.read(self.__config_file)


class NewFileProcess:
    def __init__(self):
        self.__config = config

    def check_new_file(self):
        while True:
            exists = os.path.exists(self.__config['DEFAULT']['NewFileName'])
            return exists


class Analyser:
    def __init__(self):
        self.__config = config
        self.risk_scores = self.__config['File.Scores']
        self.new_file_name = self.__config['DEFAULT']['NewFileName']
        self.system_locations = self.__config['System.locations']
        self.file_score = 0
        self.results = {}

    def parse_json_log(self):
        parsed_json = json.load(self.new_file_name)
        return parsed_json

    def calculate_score(self, parsed_json_log):
        for file in parsed_json_log:
            split_name = file['file_name'].split('.')
            if split_name[1] is '.dll':
                self.file_score += self.risk_scores['IsDLL']
            if split_name[1] is '.exe':
                self.file_score += self.risk_scores['IsEXE']
            if file['location'] in self.system_locations:
                self.file_score += self.risk_scores['IsSystemFile']
            else:
                self.file_score += self.risk_scores['IsUserFile']

            self.results.update({file, self.file_score})

            # TODO: Implements IoC support

        return self.results

    def analyse_process(self, blacklist, whitelist):
        while True:
            file_process = NewFileProcess().check_new_file()

            if file_process is True:
                results = self.calculate_score(self.parse_json_log())

                for result in results:
                    if result[1] >= self.__config['DEFAULT']['RiskThreshold']:
                        # Add to blacklist
                        blacklist.write(result)
                    if result[1] == 0:
                        # Add to whitelist
                        whitelist.write(result)


class AnaCleanUp:
    def __init__(self):
        pass


class AnaReload:
    def __init__(self):
        pass
