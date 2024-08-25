from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'schanchal2003.7@gmail.com'  # Your Gmail username
app.config['MAIL_PASSWORD'] = 'ljklszyocqtullwl'  # Your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'schanchal2003.7@gmail.com'  # Default sender

mail = Mail(app)

@app.route('/')
def index():
    return render_template('mail.html')

@app.route('/send-email',methods=["GET","POST"])
def send_email():
    data = request.json
    to_email = data.get('to')
    subject = data.get('subject')
    body = data.get('body')

    if not to_email or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        msg = Message(
            subject=subject,
            sender=app.config['MAIL_DEFAULT_SENDER'],  # Sender set here
            recipients=[to_email]
        )
        msg.body = body
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
