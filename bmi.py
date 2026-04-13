height= float (input("enter your height in meters: ")) 
weight= float (input("enter your weight in kilograms: "))
bmi= weight/(height*height)
print(f"your bmi is: {bmi}")
if bmi<18.5:
    print("you are under weight")
elif bmi>=18.5 and bmi<25:
    print("you are healthy")
elif bmi>=25 and bmi<30:
    print("you are overweight")
else: 
    print("your obese")