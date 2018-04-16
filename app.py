# Finds conflicts in course exam date and times
# By Sepehr Mohammadi

import csv

emtehanslist = {}
with open('data/takhasosi.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #name = "{0} - {1} ".format(row[0], row[1])
        name = row[0]
        #time = row[6]
        #day = row[7]
        date = "{0} - {1}".format(row[2],row[3])
        if date in emtehanslist:
            emtehanslist[date].append(name)
        else:
            emtehanslist[date] = [name]

for key, value in emtehanslist.items():
    if (len(value) > 1):
        print("=====\nDate:", key)
        print("Dars:\n", "\n".join(value), "\n====")
