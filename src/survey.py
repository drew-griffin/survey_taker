"""
    file: survey.py 
    author: Drew Seidel (dseidel@pdx.edu)
    description: The survey file provides the interaction between user classes (and subclasses) 
    and the survey.
"""
from pathlib import Path
import json
import sys
from user import User, ExistingUser
from survey_class import SurveyClass


def survey(survey_file_path="../surveys/charity1.json"):
    """takes in survey path from main.py and handles user initialization/confirmation,
    and directs the user to taking/updating/leaving the program"""

    config_file_path = Path(f"{Path.home()}/survey_config.json")
    survey_file_path = Path(survey_file_path)

    if config_file_path.is_file():  # if config file exists, it is an Existing user
        with open(config_file_path, "r", encoding="utf8") as open_config:
            current_user = ExistingUser(json.load(open_config))
        config_changed = current_user.verify_config()
        if (
            config_changed
        ):  # if user has updated configuration, write and save for next time
            current_user.write_config(config_file_path=config_file_path)
    else:  # else new user (send to config_init)
        current_user = config_init()
        current_user.write_config(config_file_path=config_file_path)

    if survey_file_path.is_file():  # process survey
        process_survey(
            survey_file_path=survey_file_path,
            config_file_path=config_file_path,
            current_user=current_user,
        )
    else:
        print("Error. Supplied survey not found.\nExiting...")
        sys.exit(1)


def process_survey(survey_file_path, config_file_path, current_user):
    """process_survey functionality:
    -new users take survey
    -existing users who have taken the survey review results and can retake
    -existing or new users without a key needed for the survey will provide this key
    """
    with open(survey_file_path, "r", encoding="utf8") as survey_open:
        survey_data = json.load(survey_open)
    current_survey = SurveyClass(
        organization=survey_data[0],
        description=survey_data[1],
        key=survey_data[2],
        questions=survey_data[3],
    )
    update_config = False
    if current_survey.has_key:
        update_config = current_user.append_keys(current_survey.key)
    if update_config:
        current_user.write_config(config_file_path=config_file_path)

    result_file_path = f"../results/{current_survey.description[0]}_{current_user.config_info_dict['last_name'].lower()}_{current_user.config_info_dict['first_name'].lower()}"
    result_file_path += (
        ".json"
        if not current_survey.has_key
        else f"_{current_user.config_info_dict[current_survey.key[0]]}.json"
    )
    result_file_path = Path(result_file_path)
    if result_file_path.is_file():
        print(
            f"It looks like you've taken the {current_survey.description[0]} survey.\nHere's how you responded..."
        )

        with open(result_file_path, "r", encoding="utf8") as open_prev_result:
            prev_result = json.load(open_prev_result)
        for key, value in prev_result.items():
            print(f"{key.replace('_', ' ').title()}: {value.title()}")
        update_survey = input("Would you like to retake and update this survey (y/n)? ")
        if update_survey.upper() == "Y":
            current_survey.take_survey(user_profile=current_user.config_info_dict)
            current_survey.write_result(result_file_path=result_file_path)
        else:
            print("Thank you. Goodbye")
    else:
        current_survey.take_survey(user_profile=current_user.config_info_dict)
        current_survey.write_result(result_file_path=result_file_path)


def config_init():
    """configures a new user for the first time"""
    current_user = User({})  # empty as there is no config file
    current_user.new_user()  # use new user method to set up and save config file for next time
    return current_user
