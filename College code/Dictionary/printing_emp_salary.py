std = {}
std_count = int(input("data of how many emp "))

for i in range(std_count):
	k1= int(input("Enter the unique id : "))
	dict_sub = {}
	k2=input("enter the name : ")
	v2=int(input("Enter salary : "))
	dict_sub[k2]=v2
	std[k1]=dict_sub	
print(std)
