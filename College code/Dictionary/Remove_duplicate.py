example_dic={1:1,2:2,3:2,4:3}
print("The original dictionary is:",example_dic)
temp=[]
res={}
for key,val in example_dic.items():
    if val not in temp:
        temp.append(val)
        res[key]=val
print("The dictionary after removing the duplicates is:",res)
