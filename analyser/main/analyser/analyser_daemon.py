import daemon
import signal
import lockfile

from main.analyser.Analyser import (
    AnaSetup,
    Analyser,
    AnaCleanUp,
    AnaReload
)

context = daemon.DaemonContext(
    umask=0o002,
    pidfile=lockfile.FileLock('analyser.pid')
)

context.signal_map = {
    signal.SIGTERM: AnaCleanUp,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: AnaReload,
}

config_file = open('./config/config.ini', 'w')
main_blacklist = open('./lists/blacklist/blacklist.ini', 'a')
main_whitelist = open('./lists/whitelist/whitelist.ini', 'a')
context.files_preserve = [config_file, main_blacklist, main_whitelist]

AnaSetup(config_file)

with context:
    Analyser().analyse_process(main_blacklist, main_whitelist)
