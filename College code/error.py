try:
    a = int(input("1st no. : "))
    b = int(input("2nd no. : "))
    d = a/b
    print(d)
except ZeroDivisionError :
    print("b is equal to Zero \"Can't divid \"")
except NameError:
    print("Name Error")
except Exception as e:
    print(e)
else:
    print('running in else')
