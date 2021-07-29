from flask import Blueprint, jsonify

index = Blueprint('index', __name__)


@index.route('/')
def health_check():
    return jsonify({'status': 'ok'})
