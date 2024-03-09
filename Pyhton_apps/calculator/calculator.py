import art
print(art.logo)
def plus(a,b):
    print(f"{a}+{b}= {a+b}")
    return a+b
def minus(a,b):
    print(f"{a}-{b}= {a-b}")
    return a-b
def divide(a,b):
    if b!=0:
        print(f"{a}/{b}= {a/b}")
        return a/b
    else :
        return f"{a} cannot divided by 0"
def multiply(a,b):
    print(f"{a}*{b}= {a*b}")
    return a*b

firstnum = int(input("What is the first number ? "))
print("\n + \n - \n / \n * \n")

x=1
while x>0:
    operation = input("Please pick a operation: ")
    secondnum = int(input("What is the next number ? "))
    if operation =="+":
        firstnum=  plus(firstnum,secondnum)
    if operation =="-":
         firstnum=  minus(firstnum,secondnum)
    if operation =="/":
        firstnum=  divide(firstnum,secondnum)
    if operation =="*":
        firstnum=  multiply(firstnum,secondnum)
    condition = input(f"Type 'y' to continue calculating with {firstnum}, or type 'n' to start a new calculation: ")
    if condition == "n" :
        x-=1 

