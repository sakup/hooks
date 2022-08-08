#!/usr/bin/python3

import sys

def main():
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()

        for line in lines:
            print(line)

if __name__ == "__main__":
    main()