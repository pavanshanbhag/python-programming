def local_namespace():
    # This is an example of the local namespace

    # define a function in the local namespace
    def func():
        print("I am a function in the local namespace")

    # define a variable in the local namespace
    x = 20

    # use the function and variable in the local namespace
    func()  
    print(x) 

local_namespace()