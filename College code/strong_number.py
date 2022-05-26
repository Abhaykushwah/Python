'''
Sample Input: num = 132

Sample Output: Given number is not a strong number

Explanation: 1! + 3! + 2! = 9 which is not equal to the 132

Sample Input: num = 145

Sample Output: Given number is a strong number
'''

sum=0  
num=int(input("Enter a number:"))  
# temporary var
temp=num  

while(num):
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")  