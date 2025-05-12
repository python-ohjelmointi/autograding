# Autograding for Python exercises returned in MS Teams

This repository contains the autograding scripts for Python exercises returned
in MS Teams. Students should submit their Python code as *.py* files, and the
teacher can run the autograding script to check the submissions from all students
at once, using *pytest*.

## How to use

The repository contains scripts for both grading a single submission and a batch of submissions from a Sharepoint folder that stores Teams submissions.

### Single submission

The `tests.sh` script can be used to test a single submission. Tests should be placed in the [tests folder](./tests/) and the student submission in the [submission folder](./submission/). When testing a single submission, the Python files should be placed in the folder as plain Python files:

```sh
./tests.sh
```


### Multiple submissions

When testing a batch of submissions, the submissions should be placed in the
`submissions` folder and the folder structure should be the same as in the
Sharepoint folder, where the submissions are stored in folders, which have the
student's name as the folder name.

The teacher can then run the `autograding.sh` script to check the submissions.
Check the contents of the autograding script before executing, as it will make
changes in the submission folders to remove unneeded files and rename incorrect
files. Never use the autograding scripts on the "main" files in Sharepoint, but
be sure to make local copies.

The autograding script will run pytest tests found in the `tests` folder for each
student. The results from the test for each student will be saved both as .txt
and .json files in the `results` folder. See example tests in the `tests` folder.

Finally, `autograding.sh` will execute the `test_summary.py` script to create a
summary of the test results from previous steps. The summary is saved in the
`summary.txt` file and printed to the console.

The `summary.txt` file will contain the test results, as well as the total points
and the grade, for each student. The summary for an individual student is similar to
the following example (the test names being in Finnish):

```
Samuel Student

puuttuva_luku:
* luvut jarjestyksessa ykkosesta alkaen: PASSED
* luvut jarjestyksessa kympista alkaen: PASSED
* luvut epajarjestyksessa: PASSED
* negatiiviset luvut: PASSED
* positiiviset ja negatiiviset luvut: PASSED

ristinolla:
* voittava rivi: FAILED
* voittava sarake: FAILED
* voitto vinosti: FAILED
* tasapeli: FAILED
* tyhja peli: FAILED

rivinumerot:
* yksi rivi: FAILED
* kaksi rivia: PASSED
* kolme rivia: PASSED
* monta rivia: PASSED
* tyhja rivi valissa: PASSED

taustavari:
* funktio kunnossa: PASSED
* otsikkorivin tausta: PASSED
* ekan rivin tausta: PASSED
* toka rivi: PASSED
* isot rivimumerot: PASSED

tekstin_keskittaminen:
* keskita yksi merkki: FAILED
* keskita yksi rivi: FAILED
* keskita monta rivia: FAILED
* keskita liian pitka rivi: FAILED
* keskita pariton keskitys: FAILED

tervehdys:
* funktio on olemassa: PASSED
* nimi loytyy tulosteesta: PASSED
* tervehdys oikein muotoiltu: FAILED
* tyhja merkkijono on tuntematon: PASSED
* none on tuntematon: FAILED

Total:
* passed: 17
* failed: 13
* total: 30
* collected: 30


Points: 17 / 30
Grade:  2.11
```

## Requirements

The autograding script requires Python 3 and pytest. It is intended to be run on
a Unix-like system, such as Linux or MacOS.

## Credits

ChatGPT has been used extensively in the creation of the autograding scripts.
The pytest tests have been written with the help of GitHub copilot.
