import csv
with open('new.csv','r',newline='')as csvfile:
    records=csv.DictReader(csvfile)
    for i in records:
        print(i)
