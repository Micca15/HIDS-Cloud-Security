from flask import request, send_from_directory
from werkzeug.utils import secure_filename
from settings import *
from models.user import User
from models.computer import Computer
from models.file import File

# endpoint to create new user
@app.route("/hids", methods=["POST"])
def add_user():

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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=["GET", 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['File']

        if uploaded_file.filename != 'conf.cfg':
            print('Geen geldig config')
            return ("", 204)

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join("conf", filename))
            print('nieuwe config geupload')
            return ("", 204)

    if request.method == 'GET':
        return send_from_directory(os.path.join('conf'), 'conf.cfg', as_attachment=True)

# Run Server
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=9000, debug=True)

