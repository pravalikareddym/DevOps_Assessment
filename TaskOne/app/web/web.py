from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Web Tier - Load Balanced"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)