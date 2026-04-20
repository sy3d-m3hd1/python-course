def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def min(num1,num2):
    return num1-num2
def exp(num1,num2):
    return num1**num2
def fdiv(num1,num2):
    return num1//num2
def mod(num1,num2):
    return num1%num2
num1=float (input("enter the first value "))
num2=float (input("enter your second value: "))
operater=input("choose a operater (+, -, *, /, **, //, %): ")
if operater=="+":
    print(f"the addition of {num1} and {num2} is { add(num1,num2)}")   
elif operater=="*":
    print(f"the multiple of {num1} and {num2} is { mul(num1,num2)}")  
elif operater=="/":
    print(f"the divisble of {num1} and {num2} is { div(num1,num2)}")  
elif operater=="-":
    print(f"the minus of {num1} and {num2} is { min(num1,num2)}")  
elif operater=="**":
    print(f"the exponiendiation of {num1} and {num2} is { exp(num1,num2)}")  
elif operater=="//":
    print(f"the floordivison of {num1} and {num2} is { fdiv(num1,num2)}")  
elif operater=="%":
    print(f"the mod of {num1} and {num2} is { mod(num1,num2)}")  
else: 
    print("invalid operater")
