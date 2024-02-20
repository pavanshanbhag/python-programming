myvar = 10

def myfunc():
    myvar = 20
    print(f"During Function value {myvar = }")

print(f"Before Function Execution - Value of {myvar = }")
myfunc()
print(f"After Fucntion Execution - Value of {myvar = }")