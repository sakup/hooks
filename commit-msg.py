#!/usr/bin/python3

import sys
import re
from rules import rules

def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()

        for idx, line in enumerate(lines):
            if line.strip() == "# ------------------------ >8 ------------------------":
                break
            if line[0] == "#":
                continue
            if not line_valid(idx, line):
                show_rules()
                sys.exit(1)

    sys.exit(0)
    
def line_valid(idx,line):
    if idx == 0:
        return re.match("^(JR|jr)\: [A-Z]{2,4}-[0-9]{1,5};.{0,50}",line)

def show_rules():
    print(rules)

if __name__ == "__main__":
    main()