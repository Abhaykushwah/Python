#perfect number
#

num = int(input("Enter the number: "))
sum = 0
for i in range(1,num):
    if (num%i == 0):
        sum = sum+i
if (sum == num):
    print("The entered number is a perfect number")
else :
    print("The entered number is not a perfect")
