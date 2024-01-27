from functools import reduce
c=['hi','my','is','navi','not','sadhi']
print(reduce(lambda x,y,:x+' '+y,c))