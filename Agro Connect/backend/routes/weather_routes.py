# Developer: Prajwal Dhage
from flask import Blueprint, jsonify
from modules.Dashboard.weather import get_weather_data

weather_bp = Blueprint('weather', __name__)  # Define a Blueprint

@weather_bp.route('/weather', methods=['GET'])
def get_weather():
    """API endpoint to get current temperature."""
    weather_data = get_weather_data()
    return jsonify(weather_data)  # Returns JSON response
