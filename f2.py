a = []
for i in range(10):
    num = int(input("Enter number {i+1}: "))
    a.append(num)
print("The numbers you entered are:", a)
total=sum(a)
average=total/10
print("sum",total)
print("average",average)
