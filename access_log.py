from flask import Flask, request, jsonify,render_template
import boto3

app = Flask(__name__)

# Initialize the CloudWatch Logs client
logs = boto3.client('logs')


@app.route('/')
def index():
    return render_template('access_log.html')


@app.route('/access-cloud-logs', methods=['POST'])
def access_cloud_logs():
    try:
        # Get log group and log stream from the request JSON body
        data = request.get_json()
        log_group = data.get('log_group')
        log_stream = data.get('log_stream')

        if not log_group or not log_stream:
            return jsonify({'error': 'log_group and log_stream are required'}), 400

        # Fetch log events from CloudWatch
        response = logs.get_log_events(
            logGroupName=log_group,
            logStreamName=log_stream,
            startFromHead=True
        )

        # Extract and return log messages
        log_messages = [event['message'] for event in response['events']]
        return jsonify({'log_messages': log_messages}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
