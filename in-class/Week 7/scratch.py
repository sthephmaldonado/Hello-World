def factorial(input):
    if(type(input)==type(3,0)):
        raise ValueError("Need an interger value")
    if(input==0):
        return 1
    else:
        return input*factorial(input-1)
factorial(10)