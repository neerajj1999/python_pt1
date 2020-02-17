def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x%y

def sqr_root(x):
    return x**0.5

print("// choice of operation//")
print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Divide")
print("5.Squre_root")

value1 = float(input("Enter the first choice: "))
value2 = float(input("Enter the second choice: "))
choice = int(input("enter your choice: "))


if choice ==1:
    print(value1,"+",value2,"=",add(value1,value2))
elif choice==2:
    print(value1,'-',value2,'=',subtract(value1,value2))
elif choice==3:
    print(value1,'*',value2,'=',multiply(value1,value2))
elif choice==4:
    print(value1,'/',value2,divide(value1,value2))
elif choice==5:
    print(value1,'=',sqr_root(value1))

else:
    print("INVALID")
