from flask import Blueprint, jsonify, request

from app.people_service import PeopleService

people = Blueprint('people', __name__)
people_service = PeopleService()


@people.route('', methods=['GET'])
def retrieve_people():
    args = request.args.get('sort')
    results = people_service.retrieve_all(args)
    return jsonify(results)


@people.route('', methods=['POST'])
def add_person():
    data = request.json
    result = people_service.add_one(data)
    return result, 201


@people.route('/<id>', methods=['PATCH'])
def update_person(id):
    data = request.json
    result = people_service.update_one(id, data)
    return result, 200


@people.route('/<id>', methods=['DELETE'])
def delete_person(id):
    result = people_service.delete_one(id)
    return jsonify({"message": f"{result}"}), 200
