# write a function to greet a user with name if no name is provided the use the default name 
def greet(name = "person"):
    return ("Hello " + name + " !!")
print(greet("Bishal"))
print(greet())
