x=input("enter first value")
oprator=input("enter oprator(+,-,/):")
y=input("enter second value")
x=int(x)
y=int(y)

if oprator == '+':
    result= x + y
elif oprator == '-':
    result= x - y
elif oprator == '/':
    if y != 0:
        result= x / y
    else:
        print("nothing")



print("result:",result)
