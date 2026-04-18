n = int (input("enter an number: "))
prime= True
if n <2:
    prime=False
else :
    for i in range(2,n):
        if n %i==0:
            prime=False
            break
if prime:
    print("Its an prime number")
else:
    print("Not an prime number")
