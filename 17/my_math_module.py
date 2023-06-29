def IsPrime(input_number: int):
    """Checking if a number is prime or not

    Args:
        input_number (int): _description_
    """
    if input_number > 1:
        for i in range(2, int(input_number / 2) + 1):
            if (input_number % i) == 0:
                return False

        return True

    return False


def IsDisiibleBySeven(number):
    pass
