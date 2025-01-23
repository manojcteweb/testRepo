from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import logging
from marshmallow import Schema, fields, ValidationError
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# Define a schema for data validation
class DataSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)

@app.route('/web', methods=['GET'])
def web_channel():
    app.logger.debug('Web channel accessed')
    return jsonify({"message": "Welcome to the web channel!"})

@app.route('/mobile', methods=['GET'])
def mobile_channel():
    app.logger.debug('Mobile channel accessed')
    return jsonify({"message": "Welcome to the mobile channel!"})

@app.route('/in-person', methods=['GET'])
def in_person_channel():
    app.logger.debug('In-person channel accessed')
    return jsonify({"message": "Welcome to the in-person channel!"})

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        # Validate incoming data
        data = request.json
        schema = DataSchema()
        validated_data = schema.load(data)
        app.logger.debug('Data validated successfully')

        # Send notification email
        msg = Message('New Submission',
                      sender='your-email@example.com',
                      recipients=[validated_data['email']])
        msg.body = f"Hello {validated_data['name']}, your data has been received."
        mail.send(msg)
        app.logger.debug('Notification email sent')

        return jsonify({"message": "Data submitted successfully!"}), 200
    except ValidationError as err:
        app.logger.error('Validation error: %s', err.messages)
        return jsonify(err.messages), 400
    except Exception as e:
        app.logger.error('An error occurred: %s', str(e))
        return jsonify({"message": "An error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)