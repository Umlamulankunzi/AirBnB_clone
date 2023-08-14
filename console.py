#!/usr/bin/python3

"""
Module that defines the command console class
"""

import ast
import cmd
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


CLASSES = {
    "Amenity": Amenity, "BaseModel": BaseModel,
    "City": City, "Place": Place, "Review": Review,
    "State": State, "User": User
}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that inherits from cmd.Cmd class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Empty command"""
        pass

    def do_EOF(self, line):
        """Handles the EOF character input"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    # RULES AND ASSUMPTIONS:
    # You can assume arguments are always in the right order
    # Each arguments are separated by a space
    # A string argument with a space must be between double quote
    # The error management starts from the first argument to the last one

    def do_create(self, line):
        """Creates a new instance of BaseModel,

        saves it (to the JSON file) and prints the id
        Example:
            (hbnb)  create BaseModel

            If the class name is missing, print
            ** class name missing **
            (ex: $ create)

            If the class name doesn't exist, print
            ** class doesn't exist **
            (ex: $ create MyModel)"""

        if not line:
            print("** class name missing **")
        elif line in CLASSES:
            obj = CLASSES[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation of an instance

        based on the class name and id.
        Example:
            (hbnb)  show BaseModel 1234-1234-1234

            If the class name is missing, print
            ** class name missing **
            (ex: $ show)

            If the class name doesn't exist, print
            ** class doesn't exist **
            (ex: $ show MyModel)

            If the id is missing, print
            ** instance id missing **
            (ex: $ show BaseModel)

            If the instance of the class name doesn't exist
            for the id, print
            ** no instance found **
            (ex: $ show BaseModel 121212)"""

        if not line:
            print("** class name missing **")
            return

        command_list = line.split(" ")

        if len(command_list) == 1:
            print("** instance id missing **")

        else:
            cls_name = command_list[0]
            cls_id = command_list[1]
            cls_key_name = f"{cls_name}.{cls_id}"

            if cls_name not in CLASSES:
                print("** class doesn't exist **")

            else:
                instance = storage.all().get(cls_key_name)
                if instance is not None:
                    print(str(instance))

                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id

        (save the change into the JSON file).
        Example:
            (hbnb) destroy BaseModel 1234-1234-1234

            If the class name is missing, print
            ** class name missing **
            (ex: $ destroy)

            If the class name doesn't exist, print
            ** class doesn't exist **
            (ex:$ destroy MyModel)

            If the id is missing, print
            ** instance id missing **
            (ex: $ destroy BaseModel)

            If the instance of the class name doesn't exist
            for the id, print
            ** no instance found **
            (ex: $ destroy BaseModel 121212)"""

        if not line:
            print("** class name missing **")
            return

        command_list = line.split(" ")

        if len(command_list) == 1:
            print("** instance id missing **")
        elif len(command_list) == 2:
            cls_name = command_list[0]
            cls_id = command_list[1]
            cls_key_name = f"{cls_name}.{cls_id}"

            if cls_name not in CLASSES:
                print("** class doesn't exist **")

            else:
                if cls_key_name in storage.all():
                    storage.delete_obj(cls_key_name)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or

        not on the class name.
        Example:
            (hbnb) all BaseModel
        or
            (hbnb) all

        The printed result must be a list of strings (like the example below)
            (hbnb) all BaseModel
            ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at'
            : datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff
            9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2
            017, 10, 2, 3, 10, 25, 903300)}"]

        If the class name doesn't exist:
            (hbnb) all MyModel
            ** class doesn't exist **
        """
        if line:
            cls_name = line
            if cls_name not in CLASSES:
                print("** class doesn't exist **")
                return

            str_objs_list = [
                str(storage.all()[key]) for key in storage.all()
                if key.startswith(cls_name)
                ]

        else:
            str_objs_list = [str(obj) for obj in storage.all().values()]

        print(str_objs_list)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or

        updating attribute (save the change into the JSON file).
        Example:
            (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        Only one attribute can be updated at the time
        Assume the attribute name is valid (exists for this model)
        The attribute value must be casted to the attribute type

        If class name is missing:
            (hbnb) update
            ** class name missing **

        If class name doesn't exist:
            (hbnb) update MyModel
            ** class doesn't exist **

        If the id is missing:
            (hbnb) update BaseModel
            ** instance id missing **

        If the instance of the class name doesn't exist for the id:
            (hbnb) update BaseModel 121212
            ** no instance found **

        If the attribute name is missing:
            (hbnb) update BaseModel existing-id
            ** attribute name missing **

        If the value for the attribute name doesn't exist:
            (hbnb) update BaseModel existing-id first_name
            ** value missing **

        All other arguments should not be used::
            (hbnb) update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            first_name "Betty" = $ update BaseModel 1234-1234-1234
            email "aibnb@mail.com"

        id, created_at and updated_at can't be updated. You can assume they
        won't be passed in the update command
        Only “simple” arguments can be updated: string, integer and float.
        Assume nobody will try to update list of ids or datetime.
        """

        if not line:
            print("** class name missing **")
            return

        command_list = line.split(" ")
        number_of_cmds = len(command_list)

        if number_of_cmds == 1:
            print("** instance id missing **")
        elif number_of_cmds == 2:
            print("** attribute name missing **")

        elif number_of_cmds == 3:
            print("** value missing **")

        else:
            cls_name = command_list[0]
            cls_id = command_list[1]
            attr_name = command_list[2]
            attr_new_value = command_list[3]
            cls_key_name = f"{cls_name}.{cls_id}"

            if cls_name not in CLASSES:
                print("** class doesn't exist **")

            else:
                instance = storage.all().get(cls_key_name)
                if instance is not None:
                    setattr(instance, attr_name, attr_new_value)
                    instance.save()
                else:
                    print("** no instance found **")

    def count_instances(self, cls_name):
        """Counts the number of instances of class given as parameter

        Args:
            cls_name (str): class name given as str

        Returns:
            int: number of instances of class
        """
        objects = [
            key for key in storage.all() if key.startswith(cls_name)]
        return len(objects)

    def default(self, line):
        """class_name.command(parameters)"""

        exec_cmds = (
            "all", "count", "show",
            "destroy", "update"
        )

        match = re.match(r"""
                            (?P<cls_name>[A-Za-z]+)
                            \.(?P<cmd>[a-z]+)
                            \((?P<parameters>.*)\)
                        """, line, re.X)
        if match is None:
            return

        match_dict = match.groupdict()
        cls_name = match_dict["cls_name"]
        cmd = match_dict["cmd"]
        params = match_dict["parameters"]

        if cls_name not in CLASSES:
            print("** class doesn't exist **")

        if cls_name in CLASSES and cmd in exec_cmds:
            if cmd == "all":
                self.do_all(cls_name)
            elif cmd == "count":
                print(self.count_instances(cls_name))
            elif cmd == "show":
                self.do_show(f"{cls_name} {params}")
            elif cmd == "destroy":
                self.do_destroy(f"{cls_name} {params}")
            elif cmd == "update":
                match = re.search(r"{.*}", params)
                if match:
                    cls_id = params.split()[0]
                    update_dict = ast.literal_eval(match.group(0))

                    for key, val in update_dict.items():
                        line = f"{cls_name} {cls_id} {key} {val}"
                        self.do_update(line)
                else:
                    # <class name> <id> <attribute name> <attribute value>
                    self.do_update(f"{cls_name} {params}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
