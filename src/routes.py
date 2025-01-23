from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from .schemas import DataSchema
from .mail import send_notification_email
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create a Blueprint for the routes
routes = Blueprint('routes', __name__)

@routes.route('/web', methods=['GET'])
def web_channel():
    logging.debug('Web channel accessed')
    return jsonify({"message": "Welcome to the web channel!"})

@routes.route('/mobile', methods=['GET'])
def mobile_channel():
    logging.debug('Mobile channel accessed')
    return jsonify({"message": "Welcome to the mobile channel!"})

@routes.route('/in-person', methods=['GET'])
def in_person_channel():
    logging.debug('In-person channel accessed')
    return jsonify({"message": "Welcome to the in-person channel!"})

@routes.route('/submit', methods=['POST'])
def submit_data():
    try:
        # Validate incoming data
        data = request.json
        schema = DataSchema()
        validated_data = schema.load(data)
        logging.debug('Data validated successfully')

        # Send notification email
        send_notification_email(validated_data)
        logging.debug('Notification email sent')

        return jsonify({"message": "Data submitted successfully!"}), 200
    except ValidationError as err:
        logging.error('Validation error: %s', err.messages)
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error('An error occurred: %s', str(e))
        return jsonify({"message": "An error occurred."}), 500
