#!/usr/bin/python3
"""A base class"""


class Base():
    """
    This is the base class for this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This initializes an object of type base
        param1 = id, an int, or if none set to nb_object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of
        list_dictionaries, a list of dictionaries
        """
        import json

        if list_dictionaries is not None:
            if type(list_dictionaries) is list:
                if list_dictionaries == "" or len(list_dictionaries) == 0:
                    return "[]"
                else:
                    return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Gets the JSON string rep of an obj
        and saves it to a file with the name
        of the class
        param1: a list of objects
        """
        if list_objs is None:
            list_objs = []
        fname = cls.__name__ + ".json"
        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())

        with open(fname, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Takes a JSON string makes it into
        list of dictionaries
        """
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates instances from a dictionary
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        Creates instances from a saved JSON file
        """
        filename = cls.__name__ + ".json"
        results = []
        try:
            with open(filename, 'r') as f:
                for instance in cls.from_json_string(f.read()):
                    results.append(cls.create(**instance))
        except Exception as err:
            pass
        return (results)
