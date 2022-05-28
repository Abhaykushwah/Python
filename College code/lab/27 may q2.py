## write a python program to print laragest word in a text file abc.txt

f = open('abc.txt','r')
file = f.read().split()
max_ln = len(max(file,key=len))
# print(file)
'''
res=[]
for i in file:
    if len(i)==max_ln:
        res.append(i)
'''
res = [i for i in file if len(i)==max_ln]
print(res)
f.close()