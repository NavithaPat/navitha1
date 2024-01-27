import  csv
with open('sample.csv','w',newline='') as file:
    data=[
        
        [1,'chandan',28],
        [2,'nandan',30],
        [3,'vrindan',18],
        
    ]
    record=csv.writer(file)
    record.writerow(['id','name','age'])
    record.writerows(data)