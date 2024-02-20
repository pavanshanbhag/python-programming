x = 10 # global variable

def foo():
    y = 5 # local variable
    x =51
    print(x) # prints 10
    print(y) # prints 5

foo()

# generates an error because y is a local variable
# and cannot be accessed outside of the function foo
print(y)

