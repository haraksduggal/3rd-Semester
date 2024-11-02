list1=[]
n=int(input("Enter the values:"))

for i in range(1,n+1):
    b=int(input("Enter the number of values:"))
    list1.append(b)


list1.sort()
print("largest element is:", list1[n-1])
