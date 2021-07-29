from app import db, ResourceNotFoundError
from app.models.person import Person, PersonSchema
from app.validator import Validator


class PeopleService:

    person_schema = PersonSchema()
    people_schema = PersonSchema(many=True)

    def retrieve_all(self, sort_key: str) -> list[dict]:
        all_people = Person.query.all()
        results = self.people_schema.dump(all_people)

        if sort_key is None:
            return results
        else:
            should_reverse, key = Validator().check_sort_key(sort_key)
            return sorted(results, key=lambda k: k[key], reverse=should_reverse)

    def add_one(self, person_data: dict) -> int:
        Validator().check_add_request(person_data)
        new_person = Person(**person_data)
        db.session.add(new_person)
        db.session.commit()
        person = Person.query.get(new_person.id)
        return self.person_schema.dump(person)

    def update_one(self, id: int, update_data: dict):
        Validator().check_update_request(update_data)
        person = Person.query.get(id)

        for key in update_data.keys():
            setattr(person, key, update_data[key])

        db.session.commit()
        return self.person_schema.dump(person)

    def delete_one(self, id: int) -> (str, int):
        person = Person.query.get(id)
        if person is None:
            raise ResourceNotFoundError(f'No Person found with id {id}')

        db.session.delete(person)
        db.session.commit()
        return f'Person with id {id} successfully deleted'
