from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('linux.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    cmd = request.args.get('cmd')
    if cmd:
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
            return jsonify({'output': result})
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e), 'output': e.output}), 400
    return jsonify({'error': 'No command provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
