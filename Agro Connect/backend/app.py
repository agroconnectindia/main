from flask import Flask, render_template
from flask_cors import CORS
from routes.weather_routes import weather_bp  # Import weather route

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/')
def backend_working():
    return render_template('index.html')

app.register_blueprint(weather_bp)  # Register weather route

if __name__ == '__main__':
    app.run()