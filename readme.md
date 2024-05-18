# Autograding for Python exercises returned in MS Teams

This repository contains the autograding scripts for Python exercises returned
in MS Teams. Students should submit their Python code as .py files, and the
teacher can run the autograding script to check the code.

## How to use

Student submissions should be placed in the `submissions` folder. The teacher
can download submissions from Sharepoint and place them in the `submissions`.

The teacher can then run the `autograding.sh` script to check the submissions.
Check the contents of the autograding before executing, as it will make changes
in the submission folders to remove unneeded files and rename incorrect files.

The autograding script will create a `results` folder with the results of the
pytest tests written in the `tests` folder. See examples in the `tests` folder.

Finally, `autograding.sh` will execute the `test_summary.py` script to create a
summary of the test results in the `results` folder, and save the summary in the
`summary.txt` file.

## Requirements

The autograding script requires Python 3 and pytest. It is intended to be run on
a Unix-like system, such as Linux or MacOS.

## Credits

ChatGPT has been used extensively in the creation of the autograding scripts.
The pytest tests have been written with the help of GitHub copilot.
