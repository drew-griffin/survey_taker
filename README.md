# ECE 508 Survey Taker
## Drew Seidel (dseidel@pdx.edu)
## ECE 508 Python Workshop Assignment #1
# Brief
This program allows users to take surveys via Python. 
First time users will be prompted for information that is saved in a configuration file (JSON format) for when they return. The user will then take the survey as specified in src/main.py (line 9). 

If the user is taking a survey that requires an ID that is not on file, then the user will be prompted for said key. 

If the user is retaking a survey with all of the same credentials (as in results are already on file), their previous results are displayed, and they are asked if they would like to repeat the survey. 

Results are saved in the results directory with the following convention: 
``` bash 
<survey_name>_<last_name>_<first_name>_(<id_if_needed>).json
```

To change the survey, edit survey_path. Example surveys are in the survey directory in this project

``` python 
import survey
survey_path = "../surveys/charity1.json"  # edit survey path here
survey.survey(survey_path)
```

# Repository organization 
- src: contains all python src code 
    - main.py - provides survey file path and invokes the program 
    - survey.py - provides the action interface between the file I/O, and Survey and User classes
    - user.py - defines the User class which stores personal attributes. ExistingUser is a subclass of User in the file that adds functionality for returning users
    - survey_class.py - provides organization of survey, and methods for taking the survey and writing out the results
- results: test survey results 
- surveys: test surveys 

# Test Runs (from new user): 
To run this program, navigate to the src directory of this repository and run main.py
``` bash
cd 'your_path_to_this_repository'/src
```
To run program
```
python3 main.py
```

## Running surveys/charity1.json (new user)
```
New user generation for our survey system:
Enter your first name: Drew
Enter your last name: Seidel
Welcome Drew Seidel
Saving your information for next time...
Welcome to this survey from Charity
ch_survey1: Survey description
First Question Text? Hello
Your results have been saved to ../results/ch_survey1_seidel_drew.json
Thank you. Goodbye
```

## Running surveys/charity1.json (again)
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? y
Last Name: Seidel (y/n)? y
It looks like you've taken the ch_survey1 survey.
Here's how you responded...
First Name: Drew
Last Name: Seidel
Quest1: Hello
Would you like to retake and update this survey (y/n)? Y
Welcome to this survey from Charity
ch_survey1: Survey description
First Question Text? Take two
Your results have been saved to ../results/ch_survey1_seidel_drew.json
Thank you. Goodbye
```

## Running surveys/psu_survey1.json 
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? Y
Last Name: Seidel (y/n)? y
Enter your Portland State Student ID (needed for this survey): 937494457
Saving your information for next time...
Welcome to this survey from Portland State University
psu_survey1: Survey description
First Question Text ('True', 'False')? true
Second Question Text ('Yes', 'No')? false
Not a valid answer. Try again.
Second Question Text ('Yes', 'No')? YES
Third Question Text ('Yes', 'No', 'Maybe')? Maybe
Fourth Question Text ('Greater Than', 'Less Than', 'Equal To')? NA
Not a valid answer. Try again.
Fourth Question Text ('Greater Than', 'Less Than', 'Equal To')? Less Than
Fifth Question Text? Hello
Your results have been saved to ../results/psu_survey1_seidel_drew_937494457.json
Thank you. Goodbye
```
## Running surveys/psu_survey2.json 
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? y
Last Name: Seidel (y/n)? y
Psu St Id: 937494457 (y/n)? y
Welcome to this survey from Portland State University
psu_survey2: Survey description
First Question Text ('False', 'True')? False
Second Question Text ('No', 'Yes')? No
Third Question Text ('No', 'Yes', 'Maybe')? yes
Fourth Question Text ('Equal To', 'Greater Than', 'Less Than')? equal to
Sixth Question Text? looking good  
Your results have been saved to ../results/psu_survey2_seidel_drew_937494457.json
Thank you. Goodbye
```
## Running surveys/work1.json 
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? y
Last Name: Seidel (y/n)? y
Psu St Id: 937494457 (y/n)? y
Enter your Work ID (needed for this survey): 45783
Saving your information for next time...
Welcome to this survey from Work
wk_survey1: Survey description
First Question Text? Hello
Second Question Text ('Yes', 'No')? no
Your results have been saved to ../results/wk_survey1_seidel_drew_45783.json
Thank you. Goodbye
```
## Running surveys/psu_survey1.json (retake) 
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? y
Last Name: Seidel (y/n)? y
Psu St Id: 937494457 (y/n)? y
Work Id: 45783 (y/n)? y
It looks like you've taken the psu_survey1 survey.
Here's how you responded...
First Name: Drew
Last Name: Seidel
Psu St Id: 937494457
Quest1: True
Quest2: Yes
Quest3: Maybe
Quest4: Less Than
Quest5: Hello
Would you like to retake and update this survey (y/n)? y
Welcome to this survey from Portland State University
psu_survey1: Survey description
First Question Text ('True', 'False')? false
Second Question Text ('Yes', 'No')? no
Third Question Text ('Yes', 'No', 'Maybe')? no
Fourth Question Text ('Greater Than', 'Less Than', 'Equal To')? equal to
Fifth Question Text? great
Your results have been saved to ../results/psu_survey1_seidel_drew_937494457.json
Thank you. Goodbye
```
## Running surveys/psu_survey1.json (change user config)
```
Welcome back!
Let's verify your information is up to date...
First Name: Drew (y/n)? n
Enter your First Name: Tom
Last Name: Seidel (y/n)? n
Enter your Last Name: Rich
Psu St Id: 937494457 (y/n)? n
Enter your Psu St Id: 489234
Work Id: 45783 (y/n)? n
Enter your Work Id: 45241
Saving your information for next time...
Welcome to this survey from Portland State University
psu_survey1: Survey description
First Question Text ('True', 'False')? True
Second Question Text ('Yes', 'No')? no
Third Question Text ('Yes', 'No', 'Maybe')? maybe
Fourth Question Text ('Greater Than', 'Less Than', 'Equal To')? less than
Fifth Question Text? tom's answers
Your results have been saved to ../results/psu_survey1_rich_tom_489234.json
Thank you. Goodbye
```