def reverseofanumber(num):
    """
    This function takes an integer as input and returns its reverse.
    """
    if num < 0:
        return -reverse_of_number(-num)
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return reversed_num
