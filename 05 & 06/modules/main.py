import mathmodule



# We want to use a loop to execute this lines multiple times

# for i in range(1,3): #[1,2]  
#     number = int(input("Enter a number: "))
#     print(mathmodule.factorial(number))

number = 1

while number !=-1: # True or False 
    number = int(input("Enter a number (-1 for exit): "))
    print("number: ", number)
    if number != -1:
        print(mathmodule.factorial(number))
else:
    print("-1 was entered, app stopped!")


# while 2==1:
#     print("Hey!")

# from mathmodule import factorial
# print(factorial(5))


