##palindrome number or not
#
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
'''
##PYTHON WAY TO CHECK
num = str(n)
temp1 = str(temp)
temp1 = reversed(temp1)
if num == temp1:
   print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
'''