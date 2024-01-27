def fact2():
    a=int(input("enter a number :-"))
    out=1
    for i in range(1,a+1):
        out*=i
    print(out)
fact2()