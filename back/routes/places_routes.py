# routes/place_routes.py
from flask import Blueprint, jsonify, request
import requests
from config import Config

place_bp = Blueprint('place_bp', __name__)

@place_bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    headers = {
        'Authorization': f'Bearer {Config.TAT_API_KEY}',
        'Accept-Language': 'th'  # เลือกภาษาไทย (หรือลบออกหากต้องการภาษาอังกฤษ)
    }
    tat_api_url = f"{Config.TAT_API_URL}/{place_id}"
    response = requests.get(tat_api_url, headers=headers)

    if response.status_code == 200:
        place_data = response.json()
        return jsonify(place_data)
    else:
        return jsonify({'error': 'Unable to fetch data from TAT API'}), response.status_code
