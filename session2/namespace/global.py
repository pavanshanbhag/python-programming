# define a function in the global namespace
def func():
    print("I am a function in the global namespace")

# define a variable in the global namespace
x = 10

def main():
    # access the function and variable in the global namespace
    func()  
    print(x)  

main()