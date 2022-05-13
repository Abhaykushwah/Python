#write a pythton program to print a list of all perfect numbers of number of digits 
# specified by the user using function which will take number of digits as argument and return list.

def lst_perfect_num(num):
    res_list=[]
    for i in range (10**(num-1),10**(num)):
        sum = 0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            res_list.append(i)
    return res_list
# usr_in = int(input("Enter a lenght of number : "))
usr_in = int(input("Enter a number : "))

res = lst_perfect_num(usr_in)
print(res)