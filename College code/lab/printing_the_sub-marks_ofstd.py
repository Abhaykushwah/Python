std = {}
std_count = int(input("data of how many studends : "))

for i in range(std_count):
	k1= int(input("Enter the roll number : "))
	dict_sub = {}
	for j in range(5):
		
		k2=input("enter the subject name : ")
		v2=int(input("Enter the marks in subject : "))
		dict_sub[k2]=v2
	std[k1]=dict_sub	
print(std)
###printing the results
sum_of_marks = 0
for i in std:
	for j in std[i]:
		sum_of_marks += std[i][j]
	print("Total number you got in the exam ",sum_of_marks)
	print("The avrage of marks ",(sum_of_marks)/5)
	print("The percentae you got ",((sum_of_marks)/500)*100)
