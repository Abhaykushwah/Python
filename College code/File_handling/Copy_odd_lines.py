## opening files in read & write mode
f = open('abc.txt', 'r') 
f1 = open('abc1.txt', 'w') 

cont = f.readlines() 
#type(cont)

for i in range(0, len(cont)): 
    if(i % 2 != 0): 
        f1.write(cont[i]) 
    else: 
        pass   
f1.close()
f.close()
print("Operation complete of copying odd line")
