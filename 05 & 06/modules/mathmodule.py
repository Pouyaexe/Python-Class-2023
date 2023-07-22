
def factorial(n:int):
    """
    This function calculates the factorial of a given number
    using a non-recursive method.
    """
    result = 1

        
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1): # i=1, i=2, i=3 ,,, 
            result = result * i
            # print("i: ", i)  
            # print("result: ", result)
        return result

