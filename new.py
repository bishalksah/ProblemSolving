from unittest import case
print("which operation do u want to perform : \n 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division")
operation = int(input("Enter the operation number :")) 
if operation in {1, 2, 3, 4}:
    num1 = int (input("Enter the first number:"))    
    num2 = int (input("Enter the second number:"))    

match (operation):
    case 1:
        print("the sum is:",num1 + num2) 
    case 2:
        print("the difference is:",num1 - num2) if num1 > num2 else print("the difference is:",num2 - num1)
    case 3:
        print("the product is:",num1 * num2)
    case 4:
        print("The quotient is:",num1 / num2)
        print("The remainder is:",num1 % num2)   
    case _:
        print("Invalid operation number")
        

# if operation == 1:
#     print("the sum is:",num1 + num2)
    
# elif operation == 2:
#     if num1 > num2 :
#         print("the difference is:",num1 - num2)
#     else:
#         print("the difference is:",num2 - num1)
    
# elif operation == 3:
#     print("the product is:",num1 * num2)
    
# elif operation == 4:
#     print("The quotient is:",num1 / num2)
#     print("The remainder is:",num1 % num2)