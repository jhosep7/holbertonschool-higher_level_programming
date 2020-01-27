#!/usr/bin/python3
"""class base
"""
import json
import turtle
from random import choice as random
import csv


class Base:
    """class constructor definition to check for id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """checks for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string rep of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string rep of list_objs to a file
        """
        TheFile = cls.__name__ + ".json"
        with open(TheFile, mode="w") as MyFile:
            if list_objs is None:
                MyFile.write("[]")
            else:
                DictList = [Obj.to_dictionary() for Obj in list_objs]
                MyFile.write(cls.to_json_string(DictList))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string represenation
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            Aux = cls(1, 1)
        if cls.__name__ is "Square":
            Aux = cls(1)
        Aux.update(**dictionary)
        return (Aux)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        TheFile = str(cls.__name__) + ".json"
        try:
            with open(TheFile, mode="r") as JsonFile:
                DictList = cls.from_json_string(JsonFile.read())
                return ([cls.create(**f) for f in DictList])
        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv
        """
        TheFile = cls.__name__ + ".csv"
        with open(TheFile, mode="w", newline="") as CSVfile:
            if list_objs is None or list_objs == []:
                CSVfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    ObjName = ["id", "width", "height", "x", "y"]
                else:
                    ObjName = ["id", "size", "x", "y"]
                MyWrite = csv.DictWriter(CSVfile, fieldnames=ObjName)
                for Obj in list_objs:
                    MyWrite.writerow(Obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from csv
        """
        try:
            TheFile = cls.__name__ + ".csv"
            with open(TheFile, newline="") as CSVfile:
                MyReader = csv.DictReader(CSVfile)
                MyList = []
                for i in MyReader:
                    for k, v in i.items():
                        i[k] = int(v)
                    MyList.append(i)
                return [cls.create(**Object) for Object in MyList]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """creates square and rectangle on GUI
        """
        InkColor = ('blue', 'black', 'red')
        for R in list_rectangles:
            Lines = turtle.Turtle()
            Lines.pencolor(random(InkColor))
            Lines.showturtle()
            Lines.up()
            Lines.goto(R.x, R.y)
            Lines.down()
            for i in range(0, 2):
                Lines.forward(R.width)
                Lines.left(90)
                Lines.forward(R.height)
                Lines.left(90)
            Lines.hideturtle()

        for S in list_squares:
            Lines = turtle.Turtle()
            Lines.pencolor(random(InkColor))
            Lines.showturtle()
            Lines.up()
            Lines.goto(S.x, S.y)
            Lines.down()
            for i in range(0, 2):
                Lines.forward(S.width)
                Lines.left(90)
                Lines.forward(S.height)
                Lines.left(90)
            Lines.hideturtle()

        turtle.exitonclick()
