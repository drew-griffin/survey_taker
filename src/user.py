"""
    file user.py 
    description: implements User and ExistingUser classes
    User: implements User class (contains all information about the user taking the survey)
    ExistingUser: implements ExistingUser class which inherits from User class (used in updating info) 
    
"""
import json
import sys


class User:
    """User class contains gathers new user profile, dictionary style, for ease
    of working with configuration file
    """

    def __init__(self, config_info_dict):
        """this dictionary is empty if new user, and read in from config file if existing"""
        self.config_info_dict = config_info_dict

    def new_user(self):
        """gather data from a new user (no configuration file noted)"""
        print("New user generation for our survey system:")
        self.config_info_dict["first_name"] = input("Enter your first name: ")
        self.config_info_dict["last_name"] = input("Enter your last name: ")
        print(
            f"Welcome {self.config_info_dict['first_name'].title()} {self.config_info_dict['last_name'].title()}"
        )

    def append_keys(self, key_id):
        """this method is called when the current survey requires a key"""
        if key_id == "" or len(key_id) != 2:
            print("Error. A key id must be supplied, or is of wrong format")
            sys.exit(2)
        else:
            if key_id[0] in self.config_info_dict:
                return False  # key already on file, return

            self.config_info_dict[key_id[0]] = input(
                f"Enter your {key_id[1]} (needed for this survey): "
            )
            return True

    def write_config(self, config_file_path):
        """ "this method writes out the updated user information to the config file"""
        if config_file_path == "":
            print("Error. A file path must be supplied")
        else:
            print("Saving your information for next time...")
            with open(config_file_path, "w", encoding="utf8") as out_config:
                out_config.write(json.dumps(self.config_info_dict))


class ExistingUser(User):
    """Existing user is a subclass of user and adds allows users to update existing info"""

    def __init__(self, config_info_dict):
        """initialize attributes of the parent class"""
        super().__init__(config_info_dict)

    def verify_config(self):
        """run this method to allow the user to make any necessary changes"""
        config_changed = False
        print("Welcome back!")
        print("Let's verify your information is up to date...")
        for key, value in self.config_info_dict.items():
            confirmation = input(
                f"{key.replace('_', ' ').title()}: {value.title()} (y/n)? "
            )
            if confirmation.upper() != "Y":
                self.config_info_dict[key] = input(
                    f"Enter your {key.replace('_', ' ').title()}: "
                )
                config_changed = True
        return config_changed
