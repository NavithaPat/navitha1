import  csv
with open('sample.csv','w') as file:
    data=[
        
        [1,'chandan'],
        [2,'nandan'],
        [3,'vrindan'],
        
    ]
    record=csv.writer(file)
    record.writerows(data)