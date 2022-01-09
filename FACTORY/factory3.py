from itertools import count


class Person:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


class PersonFactory:
    _ids = count(0)

    def create_person(self, name) -> Person:
        """Takes a person's name and return an initialized
                person with the name and an id.
               The id of the person should be set as a 0-based index
                of the object created.
            """
        person = Person(next(self._ids), name)

        return person
