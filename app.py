from flask import Flask, request, jsonify
from settings import *
from UserModel import User, Computer, File, db
import pprint

# endpoint to create new user
@app.route("/hids", methods=["POST"])
def add_user():
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request.__dict__)
    user = request.json['user']
    computer = request.json['computer']
    file = request.json['file']

    new_user = User(user)
    new_computer = Computer(computer)
    new_file = File(file)
    db.session.add(new_user)
    db.session.add(new_computer)
    db.session.add(new_file)
    db.session.commit()
    return("ok")
    # return jsonify({"user": new_user, "computer": new_computer, "file": new_file})



# Run Server
if __name__ == '__main__':
    app.run(debug=True)

