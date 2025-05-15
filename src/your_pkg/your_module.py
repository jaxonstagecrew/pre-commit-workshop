import re
from pathlib import Path


pattern = r'(?i)verify\s*=\s*false'

def check_string_in_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if re.findall(pattern,line):
                    print(line.upper())
                    failure = True
                    break
                else:
                    failure = False
    except FileNotFoundError:
        failure = False
    if failure:
        print(f"SSL Verification Disabled, FAIL")
    else:
        print(f"SSL Verification Enabled, PASS")
    return 1 if failure else 0

# check_string_in_file('pre-commit-workshop/test.py')