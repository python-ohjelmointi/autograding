#!/bin/bash

# delete all "harjoituskoe" and "tehtävä" folders
find students -type d \( -name "*harjoituskoe*" -o -name "*tehtävä*" \) -exec rm -rf {} +

# delete all empty folders
find students -depth -type d -empty -exec rmdir {} \;

# rename all returned files, where Teams has added a space and a number at the end
find students -type f -name '* [0-9]*.py' -exec sh -c 'mv "$1" "$(echo "$1" | sed "s/ [0-9]*\.py/.py/")"' _ {} \;

# install pytest and run tests for all student folders
pip install pytest pytest-json-report

# create the folder to save individual reports in
mkdir reports

# find all unique student directories and run tests
find students -type f -name '*.py' -exec dirname {} \; | sort | uniq | while read -r dir; do
    # student name should be found in the directory name
    student_name=$(echo "$dir" | cut -d'/' -f2)

    echo "Testing $dir"
    PYTHONPATH="$dir" pytest -v  --continue-on-collection-errors --json-report --json-report-file=reports/"$student_name".json tests/ > reports/"$student_name".txt
done

# Create a summary of the tests, save it, and print it out
python test_summary.py > summary.txt
cat summary.txt
