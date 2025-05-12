import json
import csv
import io
from pathlib import Path

def get_grade(scores, max_score):
    '''
    Less than 40 % of maximum score will fail

    >>> get_grade(0, 10)
    0.0

    40 % is the minimum passing score (1.0)

    >>> get_grade(4, 10)
    1.0

    >>> round(get_grade(5, 10), 2)
    1.67

    Full 100 % will give the maximum grade 5

    >>> get_grade(10, 10)
    5.0
    '''
    min_score = 0.4 * max_score

    if scores < min_score:
        return 0.0

    diff = max_score * 0.6
    return 1 + 4 * (scores - min_score) / diff

def main():
    file = Path(__file__).parent / "submission" / "report.json"
    report = json.loads(file.read_text('utf-8'))

    current_suite = ""

    # Print the outcome of each individual test
    for test in report["tests"]:
        # The test suite name, including extension, is the second keyword
        suite_name = test["keywords"][1].replace('_test.py', '')

        # Print the suite name only if it has changed
        if suite_name != current_suite:
            print(f"\n## {suite_name}\n")

        current_suite = suite_name

        # Test function name is the first keywrod. Remove the 'test_'
        # prefix and underscores to make them more human readable.
        case_name = test["keywords"][0].replace(
            'test_', '').replace('_', ' ')

        outcome = test["outcome"]

        print(f"* {case_name}: {outcome.upper()}")

    summary = report["summary"]

    # Print out all categories in the summary:
    print('\n## Total\n')
    for key, value in summary.items():
        print(f"* {key}: {value}")

    print()

    # Calculate the grade based on the number of passed and total tests
    passed = summary.get("passed", 0)
    total_tests = summary["collected"]
    grade = get_grade(passed, total_tests)

    print(f"Points: {passed} / {total_tests}")
    print(f"Grade:  {grade:.2f}")

main()