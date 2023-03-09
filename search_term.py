# sample command: (if folder is under the directory of this script then it will work, or please review glob function to scan correct folder)
# py search_term.py <term>
# py search_term.py <term> > dump.log

import glob
import sys

term_to_find = sys.argv[1]
print("Search term: " + term_to_find)
file_counter = 0
file_scanned = []
i = 0
j = 0
for file_name in glob.glob("./**/*.log",recursive=True):
    file = open(file_name,'r')
    file_scanned.append(file_name)
    file_counter = file_counter + 1;
    lines = file.readlines()
    linecounter = 0
    for line in lines:
        linecounter = linecounter + 1
        if term_to_find in line:
            print(file_name + ": " + str(linecounter))

print("\n")
print("..following " + str(file_counter) + " files were scanned for: " + term_to_find)
for file_s in file_scanned:
    print(file_s)