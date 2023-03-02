# date_to_find = date in YYYY-MM-DD format from command line args[1]
# directory = from command line args[2]
# Read recursively from given directory to all directories inside
# for each file found
#   open the file in read mode
#   find date_to_find
#       open file in write mode      
#       write from this position to end
#       break

# sample command: (modify the glob function if this script is in other folder than the files to be modified)
# py prod_trim_log_to_date.py 2023-01-08 folder_name
import glob
import sys

date_to_find = sys.argv[1]
directory = sys.argv[2]
print("Replacing upto line with date: " + date_to_find + " in directory " + directory)
file_counter = 0
for file_name in glob.glob("./" + directory + "/**/*.log*",recursive=True):
    file = open(file_name,'r')
    print("\n")
    print("Working on file: " + file_name)
    lines = file.readlines()
    linecounter = 0
    datefound = False
    for line in lines:
        linecounter = linecounter + 1
        if date_to_find == line[0:len(date_to_find)]:
            datefound = True
            if linecounter == 1:
                print("...file starts with " + date_to_find + ", so no modification will be applied")
                break
            else:
                file = open(file_name,'w')
                file.writelines(lines[linecounter-1:])
                print("....file done")
                file_counter = file_counter + 1
                break
    if not datefound:
        print(date_to_find + " was not found in file")
        
print(str(file_counter) + " files are modified")