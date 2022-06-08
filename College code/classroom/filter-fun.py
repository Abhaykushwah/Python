def fun(n):
    if n%2==0:
        return True
    else:
        return False

lst=[1,2,3,4,5]
#list1= list(filter(fun,lst))
list1= list(filter(lambda n:n%2==0,lst))
print(list1)
