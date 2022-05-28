## write a python program to print the longest line in a file abc.txt

f = open('abc.txt','r')
file = f.readlines()
print(file)
max_ln = len(max(file,key=len))
res = [i for i in file if len(i)==max_ln]
print(res)
f.close()