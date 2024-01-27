rows=int(input('enter the number of rows'))
for i in range(rows):
    for j in range(rows):
        if i==(i-1) and j==(j-1):
            print('',end='')
        else:
            print('* ',end='')
    print()