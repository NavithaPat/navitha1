a=int(input('enter a value:-'))
b=int(input('enter b value:-'))
operator=input('enter a operator')
match operator:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '%':
        print(a%b)
    case _:
        print('invalid operator')