name = "syed"
total = int(input("total days: "))
absent = int(input("absent days: "))

present = total - absent
per = present / total * 100

print("your attendance is", per,"%")

if per >= 75:
    print(name, "you can give exam ")
else:
    print(name, "you cant give exam beacuse your attendance is low")