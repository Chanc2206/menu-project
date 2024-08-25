from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)
# Twilio configuration
TWILIO_ACCOUNT_SID = 'AC9aeb260122a2916798fc8fcae047d640'
TWILIO_AUTH_TOKEN = '30acc2627bd63d410dd97c2834a395fc'
TWILIO_PHONE_NUMBER = '+16034466198' 

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/send-sms', methods=['GET', 'POST'])
def send_sms():
    data = request.get_json()
    to_phone = data.get('to')
    message_body = data.get('body')

    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to= to_phone
        )
        return jsonify({'message': 'SMS sent successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



