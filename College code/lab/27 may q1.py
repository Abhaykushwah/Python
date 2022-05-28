##trying to raise two error in a program and then handle

try:
    a = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))
    if a<5:
        c=a/b
    print(c)
except NameError:
    print("C IS NOT defined")
except ZeroDivisionError:
    print("trying to divid by zero")
except Exception as e:
    print(e)