d={1:111,2:222,3:333,4:444}
'''
x= int(input())
for i in range(x):
    k= int(input())
    v=int(input())
    d.update({k:v})
'''

#print(d)
#print(d.keys())
#print(d.values())
#print(d.items())
print(d.get(1))
print(d.get(483))
#d.clear()
#print(d)
d.pop(2)
print(d)
