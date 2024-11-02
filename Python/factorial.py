#WAP TO ENTER ANY NUMBER AND FIND IT'S FACTORIAL:
num=int(input("Enter a number, to find it's factorial: "))
fac=1
for i in range(1, num + 1):
    fac *= i
print("factorial is:",fac)
