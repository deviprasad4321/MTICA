l=10
b=9
try:
    if l<0 or b<0:
        raise ZeroDivisionError
    print('area of rectangle is',l*b)
except ZeroDivisionError:
    print('please enter valid integer value')
