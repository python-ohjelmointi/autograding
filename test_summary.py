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


def list_json_files(folder: str) -> list[Path]:
    path = Path(__file__).parent / folder
    return path.glob("*.json")


if __name__ == "__main__":

    # Create an in-memory buffer
    csv_buffer = io.StringIO()

    # Create a CSV writer object, writing to the buffer
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(["Name", "Points", "Grade"])

    reports_folder = "reports"

    # After running autograding.sh, the test results are stored in JSON files
    json_reports = list_json_files(reports_folder)

    # Each JSON file is expected to contain the test results of a single student
    for file in json_reports:

        # the file is expected to be named after the student:
        student_name = file.name.replace('.json', '')

        # The report is encoded in Pytest JSON format
        report = json.loads(file.read_text('utf-8'))

        print('#', student_name)

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

        # Write the student's name and grade to the CSV file
        csv_writer.writerow([student_name, passed, round(grade, 2)])

        print('\n\n', '*' * 80, '\n\n', sep='')

    csv_content = csv_buffer.getvalue()
    csv_path = Path(__file__).parent / 'summary.csv'
    csv_path.write_text(csv_content, encoding='utf-8-sig')
