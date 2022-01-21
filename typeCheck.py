def only_ints(num1,num2):
    if type(num1) == int and type(num2) == int:
        return True
    else:
        return False
print(only_ints(1,2))
