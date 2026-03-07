def greater_than(x,y):
    if x > y:
        return "true"
    else:
        return "false"

a = 10
b = 6
result = greater_than(a,b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result) )
