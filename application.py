from flask import Flask, render_template, jsonify

# Elastic Beanstalk looks for an application callable by default
application = Flask(__name__)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/health')
def health():
    return jsonify(status="healthy")

@application.route('/api/info')
def info():
    return jsonify({
        "service": "Elastic Beanstalk Python Demo",
        "version": "1.0.0",
        "environment": "development"
    })

# Run the application
if __name__ == '__main__':
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=5000)