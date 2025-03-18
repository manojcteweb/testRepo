from flask import Blueprint, jsonify, request, render_template_string
from marshmallow import ValidationError
from .schemas import DataSchema
from .mail import send_notification_email
import logging
Set up logging
logging.basicConfig(level=logging.DEBUG)
Create a Blueprint for the routes
routes = Blueprint('routes', __name__)
@routes.route('/web', methods=['GET'])
def web_channel():
logging.debug('Web channel accessed')
Simulate user authentication check
user_logged_in = True   This should be replaced with actual authentication logic
user_name = "John Doe" if user_logged_in else None
Determine welcome message
if user_logged_in and user_name:
welcome_message = f"Welcome to the web channel, {user_name}!"
else:
welcome_message = "Welcome to the web channel!"
HTML template for the web channel page
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Web Channel</title>
<style>
body {{
font-family: Arial, sans-serif;
margin: 0;
padding: 0;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 100vh;
background-color: f4f4f9;
color: 333;
}}
.welcome-message {{
font-size: 2em;
margin-bottom: 20px;
text-align: center;
}}
.features {{
margin-bottom: 20px;
text-align: center;
}}
.get-started {{
padding: 10px 20px;
background-color: 007bff;
color: white;
text-decoration: none;
border-radius: 5px;
}}
.get-started:hover {{
background-color: 0056b3;
}}
@media (max-width: 768px) {{
.welcome-message {{
font-size: 1.5em;
}}
}}
</style>
</head>
<body>
<div class="welcome-message">{welcome_message}</div>
<div class="features">
<p>Explore our top features:</p>
<ul>
<li>Feature 1: Description of feature 1.</li>
<li>Feature 2: Description of feature 2.</li>
<li>Feature 3: Description of feature 3.</li>
</ul>
</div>
<a href="/tutorial" class="get-started">Get Started</a>
</body>
</html>
"""
return render_template_string(html_content)
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
Validate incoming data
data = request.json
schema = DataSchema()
validated_data = schema.load(data)
logging.debug('Data validated successfully')
Send notification email
send_notification_email(validated_data)
logging.debug('Notification email sent')
return jsonify({"message": "Data submitted successfully!"}), 200
except ValidationError as err:
logging.error('Validation error: %s', err.messages)
return jsonify(err.messages), 400
except Exception as e:
logging.error('An error occurred: %s', str(e))
return jsonify({"message": "An error occurred."}), 500