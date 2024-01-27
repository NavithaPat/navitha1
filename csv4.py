import csv
with open('new.csv','w',newline='')as csvfile:
    fieldnames=['id','name','age']
    record=csv.DictWriter(csvfile,fieldnames)
    record.writeheader()
    data=[
        {'id':1,'name':'harsha','age':25},
         {'id':2,'name':'harshiya','age':25},
    ]
    record.writerows(data)