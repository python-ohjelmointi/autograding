PYTHONPATH=/workspaces/autograding/submission pytest -v \
 --continue-on-collection-errors --json-report \
 --json-report-file=./submission/report.json \
  --timeout=5 tests/

