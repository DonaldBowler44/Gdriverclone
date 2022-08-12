from flask import Blueprint, render_template, request, redirect, url_for, abort
from datetime import datetime
from model import db
from model import Event


upload = Blueprint("upload", __name__, template_folder="routes")

def format_event(event):
    return {
        "description": event.description,
        "id": event.id,
        "created_At": event.created_At
    }

@upload.route('/')
def hello():
    return 'Hey!'

# create an event
@upload.route('/events', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# get all events
@upload.route('/events', methods = ['GET'])
def get_events():
    events = Event.query.order_by(Event.created_At.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

# get single event
@upload.route('/events/<id>', methods = ['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {'event': formatted_event}

# delete an event
@upload.route('/events/<id>', methods = ['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {id}) deleted!'

# edit an event
@upload.route('/events/<id>', methods = ['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description = description, created_At = datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}