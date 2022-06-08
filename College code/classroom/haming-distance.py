def haming(num,num1):
    c=num^num1
    count=0
    while(c>0):
        if(c&1==1):
            count+=1
            c=c>>1
    return count
x= int(input("Enter the frist value : "))
y= int(input("Enter the second value : "))
m=haming(x,y)
print(m)
