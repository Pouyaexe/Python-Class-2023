"""
1. Write a function that takes in a list of numbers 
and returns the sum of all the even numbers in the list.
The function should have an optional parameter that allows
the user to specify whether they want to include odd numbers in the sum as well.

2. Write a function that takes in a list of strings 
and returns a new list with all the strings capitalized. 
The function should have an optional parameter that allows 
the user to specify whether they want to capitalize only the 
first letter of each string or all letters.


""" 
def sum_even(lst, include_odd=False):
    """takes a list of numbers and returns the sum of all the even numbers in the list.

    Args:
        lst (list): list of numbers
        include_odd (bool, optional): whether to include odd numbers in the sum. Defaults to False.

    Returns:
        int: sum of even numbers
    """
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
        elif include_odd:
            sum += num
    return sum



def capitalize_strings(lst, capitalize_all=False):
    """takes a list of strings and returns a new list with all the strings capitalized.

    Args:
        lst (list): list of strings
        capitalize_all (bool, optional): whether to capitalize all letters or just the first letter. Defaults to False.

    Returns:
        list: list of capitalized strings
    """
    new_lst = []
    for string in lst:
        if capitalize_all:
            new_lst.append(string.upper())
        else:
            new_lst.append(string.capitalize())
    return new_lst



if __name__ == "__main__":
    # Testing sum_even:
    lst = [1, 2, 3, 4, 5, 6]
    print(sum_even(lst))
    print(sum_even(lst, True))

    # Testing capitalize_strings:
    lst = ["hello", "world", "how", "are", "you"]
    
    print(capitalize_strings(lst))
    print(capitalize_strings(lst, True))
    