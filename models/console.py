#!/usr/bin/python3
"""Console module"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit"""
        return True

    def do_EOF(self, arg):
        """EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, arg):
        """Create object"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in classes:
            print("** class doesn't exist **")
            return

        obj = classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show object"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_all(self, arg):
        """Show all"""
        objects = []

        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        for key, obj in storage.all().items():
            if not arg or key.startswith(arg):
                objects.append(str(obj))

        print(objects)
