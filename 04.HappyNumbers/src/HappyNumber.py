def is_happy(n):
    """
    A number is considered "happy" if by operating a mathematical sequence on that, it results in 1.
    The process is as:
    - start with a positive integer
    - replace it with the sum of the squares of its digit
    - reapeat the process until you end up with a single digit number If you eventually end up with 1, then the positive intiger is a happy number. 

    :param n: Input number
    :return: True if the n is a happy number, False is n is not a happy number
    
    Examples:

    >>> is_happy(19)
    True

    >>> is_happy(7)
    True

    >>> is_happy(45)
    False
    
    """
    while str(n).__len__() != 1:
        n = sum([int(i)**2 for i in str(n)])
        #print(n)
    if n == 1:
        return True
    else:
        return False


if __name__=="__main__":
    n = input('input a positive integer: ')
    print(is_happy(n))