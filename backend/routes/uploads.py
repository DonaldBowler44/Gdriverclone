from flask import Blueprint, render_template, request, redirect, url_for, abort, current_app, json, flash
from datetime import datetime
from model import db
from model import Upload
# from model import Event
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException

upload = Blueprint("upload", __name__, template_folder="routes")

# current_app.config['UPLOAD_EXTENSIONS'] = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
# current_app.config['UPLOAD_PATH'] = 'uploads'

# def format_event(event):
#     return {
#         "description": event.description,
#         "id": event.id,
#         "created_At": event.created_At
#     }

@upload.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        f.save(secure_filename(f.filename))
        upload = Upload(filename=f.filename, data=f.read())
        db.session.add(upload)
        db.session.commit()

    return 'file uploaded successfully'
    # return f'Uploaded: {f.filename}'
    # return 'file uploaded successfully' match return with first if request.method == post


@upload.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response



# create an event
# @upload.route('/events', methods = ['POST'])
# def create_event():
#     description = request.json['description']
#     event = Event(description)
#     db.session.add(event)
#     db.session.commit()
#     return format_event(event)

# get all events
# @upload.route('/events', methods = ['GET'])
# def get_events():
#     events = Event.query.order_by(Event.created_At.asc()).all()
#     event_list = []
#     for event in events:
#         event_list.append(format_event(event))
#     return {'events': event_list}

# get single event
# @upload.route('/events/<id>', methods = ['GET'])
# def get_event(id):
#     event = Event.query.filter_by(id=id).one()
#     formatted_event = format_event(event)
#     return {'event': formatted_event}

# delete an event
# @upload.route('/events/<id>', methods = ['DELETE'])
# def delete_event(id):
#     event = Event.query.filter_by(id=id).one()
#     db.session.delete(event)
#     db.session.commit()
#     return f'Event (id: {id}) deleted!'

# edit an event
# @upload.route('/events/<id>', methods = ['PUT'])
# def update_event(id):
#     event = Event.query.filter_by(id=id)
#     description = request.json['description']
#     event.update(dict(description = description, created_At = datetime.utcnow()))
#     db.session.commit()
#     return {'event': format_event(event.one())}