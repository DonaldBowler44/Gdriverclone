To install packages:

https://packaging.python.org/en/latest/tutorials/installing-packages/ 

https://pypi.org/project/pipenv/

virtualenv location:
C:\Users\donal\.virtualenvs\backend-c2psvOtZ

from pipenv
(use select intrepretor w- crtl-shift-p, paste in virtualenv location.)

//Running on http://127.0.0.1:5000
//use flask run to start app

//method to create databse
--python
--from app import db
--db.create_all() to create database
//all cmmds, run this without flask run in terminal

# upload = Upload(filename=f.filename, data=f.read())
        # db.session.add(upload)
        # db.session.commit()

@upload.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

https://stackoverflow.com/questions/10219486/flask-post-request-is-causing-server-to-crash

RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.

///this route works
@upload.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        f.save(secure_filename(f.filename))
    return 'file uploaded successfully'

//dude, watch your spaces, make sure "return" matches with the first "if", works for all files

https://stackoverflow.com/questions/46540664/no-application-found-either-work-inside-a-view-function-or-push-an-application

https://web.itu.edu.tr/uyar/fad/data-model.html

https://stackoverflow.com/questions/58216619/how-to-commit-code-for-a-second-time-on-terminal





