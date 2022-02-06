def phoneword(phonenumber):
    """
    Returns all possible phonewords respective to a phonenumber
    :param phonenumber: str
    :return: list of str with all phonewords
    """
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7':'pqrs', '8': 'tuv', '9': 'wxyz',
    }

print(phoneword('')) # ['']
print(phoneword('736')) #['REN' 'SEN']