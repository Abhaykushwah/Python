print('Welcome to the game of lossers.....')
print('total number of balls = 51')

print('------------------------------------')
print("--------YOU CAN ONLY PICK 1,2,3,4---------")
n=51
while (n>0): 
	u_in = int(input("pick some balls : "))
	if u_in==1 or u_in==2 or u_in==3 or u_in==4 :
		if n!=1:		
			print("computer : ", 5-u_in)
			n-=5
			print("Remaning balls : ", n)
		else:
			if u_in!=1:
				print("Invalid choice ! 😑")
			else:
				break		
	else:
		print("Invalid choice ! 😑")
print("YOU lose 😪")
print("TRY Again 🤗")
