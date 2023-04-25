"""
    file: survey_class.py
    author: Drew Seidel (dseidel@pdx.edu)
    description: SurveyClass contains information about the current survey: 
        organization: (PSU, Charity, Work, etc. )
        description:  (survey_name, survey description)
        key:          (key_id, description)
        questions:    (questions nested dictionaries)
    and a methods for taking the survey, and writing out the result
"""

import json


class SurveyClass:
    """SurveyClass holds survey information and methods for taking and writing out result"""

    def __init__(self, organization, description, key, questions):
        """class is initialized with values from survey JSON file"""

        self.organization = organization
        self.description = description
        self.key = key
        self.questions = questions
        self.has_key = True if (len(key) != 0) else False
        self.result = {}  # empty dictionary result created on initialization

    def take_survey(self, user_profile):
        """builds relevant result dictionary and allows user to answer questions from
        quest1 ... questn where n is the last question"""

        # initialize beginning of result dictionary
        self.result["first_name"] = user_profile["first_name"].lower().title()  
        self.result["last_name"] = user_profile["last_name"].lower().title()
        if self.has_key:
            self.result[self.key[0]] = user_profile[self.key[0]]

        print(f"Welcome to this survey from {self.organization.title()}")
        print(f"{self.description[0]}: {self.description[1]}")
        i = 1
        question_key = f"quest{i}"
        while question_key in self.questions:
             # answer open-ended questions
            if (len(self.questions[question_key]["answers"]) == 0): 
                answer = input(f"{self.questions[question_key]['text']}? ")
            else:  # answer questions with defined responses ('Yes', 'No', etc.)
                answer = input(
                    f"{self.questions[question_key]['text']} ({str(self.questions[question_key]['answers'])[1:-1]})? "
                )
                # if answer provided is not within the option
                if (
                    answer.lower().title()
                    not in self.questions[question_key]["answers"]
                ):
                    print("Not a valid answer. Try again.")
                    continue
            self.result[question_key] = answer.lower().title()
            i += 1
            question_key = f"quest{i}"

    def write_result(self, result_file_path):
        """write out results to the output path provided"""
        with open(result_file_path, "w", encoding="utf8") as out_result:
            out_result.write(json.dumps(self.result))
        print(f"Your results have been saved to {result_file_path}")
        print("Thank you. Goodbye")
