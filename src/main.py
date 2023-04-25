"""
 file main.py
 author: Drew Seidel (dseidel@pdx.edu)
 description: used to change the survey being taken and 
 get the program running by calling the survey method in survey file
"""

import survey
survey_path = "../surveys/psu_survey1.json"  # edit survey path here
survey.survey(survey_path)
