from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Configurations for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'schanchal2003.7@gmail.com'  # Your Gmail username
app.config['MAIL_PASSWORD'] = 'ljklszyocqtullwl'  # Your Gmail password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Configure CORS
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

@app.route('/send-bulk-email', methods=['POST'])
def send_bulk_email():
    data = request.get_json()
    recipients = data.get('recipients')
    subject = data.get('subject')
    body = data.get('body')
    sender = data.get('sender')

    if not all([recipients, subject, body, sender]):
        return jsonify({'error': 'All fields are required'}), 400

    try:
        for recipient in recipients:
            msg = Message(subject=subject,
                          sender=sender,
                          recipients=[recipient],
                          body=body)
            mail.send(msg)
        return jsonify({'message': 'Emails sent successfully'}), 200
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': 'An error occurred while sending the email.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
