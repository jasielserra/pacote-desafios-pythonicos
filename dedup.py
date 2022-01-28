def dedup(lst):
    '''
    Remove duplicates form lst
    :param lst: a list
    :return: new list without duplicated elements
    '''

    return set(lst)

print(dedup(['banana','banana','banana','abacaxi','caqui']))