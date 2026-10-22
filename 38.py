# function with args :write a function that takes variable number of arguments and return their sum

def sum_all(*args):
    return sum(args)

print(sum_all( 1 ,2 , 3, 4 ,5))
