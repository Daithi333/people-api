from flask import jsonify


def handle_invalid_method(e):
    return jsonify({'message': 'Invalid method on request'}), 405


def handle_invalid_route(e):
    return jsonify({'message': 'Requested route not found on server'}), 404


def handle_bad_request(e):
    return jsonify({'message': 'Bad Request'}), 400


def handle_generic_exception(e):
    return jsonify({'message': f'Internal processing Error: {e}'}), 500


def handle_validation_error(e):
    return jsonify({'message': f'{e}'}), 422


def handle_not_found_error(e):
    return jsonify({'message': f'{e}'}), 404


class ValidationError(Exception):
    pass


class ResourceNotFoundError(Exception):
    pass
