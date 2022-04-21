ran = int(input("Enter center number of star"))

num = int(input("How many number of time loops will run"))


for i in range(0,num):

    for i in range(0,ran):
        print("*"*i,end=' ')
        print()
    for i in  range(ran,0,-1):
        print("*"*i,end=' ')
        print()
