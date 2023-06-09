"""
1. Write a function that takes in a list of numbers 
and returns the sum of all the even numbers in the list.
The function should have an optional parameter that allows
the user to specify whether they want to include odd numbers
in the sum as well.

2. Write a function that takes in a list of strings 
and returns a new list with all the strings capitalized. 
The function should have an optional parameter that allows 
the user to specify whether they want to capitalize only the 
first letter of each string or all letters.
list = ["hello", "world", "how", "are", "you"] -> ["Hello", "World", "How", "Are", "You"] or ["HELLO",]
(list:list[str]) -> list[str]
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
        if num % 2 == 0:  # This means the number is even.
            sum += num
        elif include_odd:
            sum += num
    return sum


def capitalize_strings(lst, capitalize_all=True):
    """
    Args:
        lst (list): list of strings
        capitalize_all (bool, optional): whether to capitalize all letters. Defaults to False.

    Returns:
        list: list of strings with capitalized letters.
    """
    new_lst = []
    for string in lst:
        if capitalize_all:
            new_lst.append(string.upper())  # Hello -> HELLO
        else:
            new_lst.append(string.capitalize())  # hello -> Hello ||  Hello -> Hello

    return new_lst


if __name__ == "__main__":
    # Testing sum_even:
    list_of_numbers = [1, 2, 3, 4, 5, 6]
    print(sum_even(lst=list_of_numbers))
    print(
        sum_even(
            include_odd=True,
            lst=list_of_numbers,
        )
    )

    # Testing capitalize_strings:
    lst = ["hello", "world", "how", "are", "you"]

    print(capitalize_strings(lst))
    print(capitalize_strings(lst, False))
