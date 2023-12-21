import json
import os
from password_target import PasswordTarget


class DataHandler:
    """
    DataHandler is responsible for handling the data.json file.

    Attributes:
    ----------
    json_file (str): path to the data.json file

    Methods:
    ------
    open_file (str): open the data.json file
    update_data_file(password_target: PasswordTarget): update the data.json file
    contains(password_target_name: str): check if the password target exists in the data.json file
    read_target_data_from_file(password_target_name: str): get the password target from the data.json file
    read_target_data_from_obj(self, password_target: PasswordTarget):
    add_password_target(password_target: PasswordTarget): add the password target to the data.json file

    """

    def __init__(self) -> None:
        self.json_file = "data.json"
        self.open_file()

    def open_file(self) -> None:
        """
        Open the data.json file.
        """
        if os.path.isfile(self.json_file):
            with open(self.json_file, "r+") as outfile:
                if (os.stat(self.json_file).st_size) < 2:
                    json.dump({}, outfile, indent=4)
        else:
            with open(self.json_file, "w+") as outfile:
                json.dump({}, outfile, indent=4)
                print(f"JSON file {self.json_file} created")
    
    def update_data_file(self, password_target: PasswordTarget) -> None:
        """
        Update the data.json file.
        """
        with open(self.json_file, "r+") as json_file:
            data = json.load(json_file)
            assert password_target.name in data
            data[password_target.name].update({
                        "min_uppers": password_target.min_uppers,
                        "min_lowers": password_target.min_lowers,
                        "min_digits": password_target.min_digits,
                        "length": password_target.length
                    })
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()

    def contains(self, password_target_name: str) -> bool:
        """
        Check if the password target exists in the data.json file.
        """
        if not (os.stat("data.json").st_size):
            return False
        with open(self.json_file, "r") as json_file:
            data = json.load(json_file)
            return password_target_name in data

    def read_target_data_from_file(self, password_target_name: str) -> PasswordTarget:
        """
        Get the password target from the data.json file.
        """
        password_target = PasswordTarget(password_target_name)
        with open(self.json_file, "r") as json_file:
            data = json.load(json_file)[password_target.name]
            password_target.min_uppers = data["min_uppers"]
            password_target.min_lowers = data["min_lowers"]
            password_target.min_digits = data["min_digits"]
            password_target.length = data["length"]
        return password_target

    def read_target_data_from_obj(self, password_target: PasswordTarget):
        """
        Get the password target from PasswordTarget object.
        """
        return {
            "name": password_target.name,
            "min_uppers": password_target.min_uppers,
            "min_lowers": password_target.min_lowers,
            "min_digits": password_target.min_digits,
            "length": password_target.length,
        }

    def add_password_target(self, password_target: PasswordTarget) -> None:
        """
        Add the password target to the data.json file.
        """
        with open(self.json_file, "r+") as json_file:
            data = json.load(json_file)
            data[password_target.name] = self.read_target_data_from_obj(password_target)
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
            
    def delete_password_target(self, password_target: PasswordTarget) -> None:
        """
        remove the password target from the data.json file

        Args:
            password_target (PasswordTarget): password target object
        """
        with open(self.json_file, "r+") as json_file:
            data = json.load(json_file)
            if password_target.name in data:
                del data[password_target.name]
            json_file.seek(0)
            json.dump(data, json_file, indent=4)
            json_file.truncate()
