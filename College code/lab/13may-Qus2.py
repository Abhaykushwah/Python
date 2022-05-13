#W.A.P to print a list of all prime numbers of number of digits specified by the user using fnction 
#which will take number of digits as argument and return list.

from importlib import import_module
from operator import imod


import random
def lst_prime_num(num):
    res_list=[]
    for i in range (10**(num-1),10**(num)):
        for j in range(2,i):
            if i%j==0:
               break
        else:
            res_list.append(i)
    return res_list
# usr_in = int(input("Enter a lenght of number : "))
usr_in = int(input("Enter a number : "))
res = lst_prime_num(usr_in)
print(res)

##print(random.choice(res))
