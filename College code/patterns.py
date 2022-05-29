'''

# pattern 1

\'''
*
**
***
****
*****
******
\'''
r=int(input())
for i in range (1,r+1):
    for j in range (i):
        print("*",end="")
    print()

# pattern 2

\'''
******
*****
****
***
**
*
\'''
r=int(input())
for i in range (1,r+1):
    for j in range (r+1-i):
        print("*",end="")
    print()

'''

# pattern 3
'''
1
12
123
1234
12345
'''

r = int(input())
for i in range(1,r+1):
    for j in range(i):
        print(j+1,end="")
    print()