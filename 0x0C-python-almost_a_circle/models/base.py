#!/usr/bin/python3
"""
Defines a Base module.
"""
import json
import os
import json


class Base:
    """Initialize Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): list of dict respersentaion.
        Returns:
            (str): Json represantation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.
        Args:
            cls: class
            list_objs (list): is list of instances.
        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        li = []
        if list_objs is not None:
            for i in list_objs:
                li.append(cls.to_dictionary(i))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Represent json string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        create: create a new instance depending of the cls._name_
        it is necessary to initialize the variables width, height
        if it is Rectangle or size if it is square
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file: reads from file.json and returns the objects
        """
        filename = cls.__name__ + ".json"
        variable = ""
        result = []
        inst = []
        if os.path.exists(filename) is True:
            with open(filename, 'r') as f:
                variable = f.read()
                result = cls.from_json_string(variable)
                for elem in result:
                    inst.append(cls.create(**elem))
            return(inst)
        else:
            return (result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv: save a dir in a csv file
        """
        filename = cls.__name__ + ".csv"
        result = ""
        new = []
        big = []
        with open(filename, 'w') as fd:
            if list_objs is None:
                result = csv.writer(fd, delimiter=',')
                result.writerow([])
            else:
                result = csv.writer(fd, delimiter=',')
                if cls.__name__ == "Rectangle":
                    for elem in list_objs:
                        new = ['id', 'width', 'height', 'x', 'y']
                        var = []
                        for i in new:
                            var.append(getattr(elem, i))
                        result.writerow(var)
                if cls.__name__ == "Square":
                    for elem in list_objs:
                        new = ['id', 'size', 'x', 'y']
                        var = []
                        for i in new:
                            var.append(getattr(elem, i))
                        result.writerow(var)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv: loads from csv file and create objects
        """
        filename = cls.__name__ + ".csv"
        inst = []
        d = {}
        if os.path.exists(filename) is True:
            with open(filename) as fd:
                result = csv.reader(fd, delimiter=',')
                for row in result:
                    a = []
                    for elem in row:
                        a.append(int(elem))

                    if cls.__name__ == "Rectangle":
                        new = ['id', 'width', 'height', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
                    if cls.__name__ == "Square":
                        new = ['id', 'size', 'x', 'y']
                        for i in range(len(a)):
                            d[new[i]] = a[i]
                        inst.append(cls.create(**d))
            return(inst)
        else:
            return(result)

"""
    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle = turtle.Turtle()
        for elem in list_rectangles:
            turtle.goto(elem.x, elem.y)
            for i in range(2):
                turtle.up()
                turtle.forward(elem.width)
                turtle.left(90)
                turtle.forward(elem.height)
                turtle.left(90)
            turtle.hidde()
    for elem in list_squares:
            turtle.goto(elem.x, elem.y)
            for i in range(2):
                turtle.up()
                turtle.forward(elem.width)
                turtle.left(90)
                turtle.forward(elem.width)
                turtle.left(90)
            turtle.hidde()
        turtle.done()
"""
