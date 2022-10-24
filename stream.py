import csv
import sys
import time


reader = csv.reader(sys.stdin)
for row in csv.reader(iter(sys.stdin.readline, '')):
    print("Read: ({}) {!r}".format(time.time(), row))