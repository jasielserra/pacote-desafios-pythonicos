def dedup(lst):
    '''
    Remove duplicates from lst
    :param lst: a list
    :return: new list without duplicated elements
    '''
    result = []

    for e in lst:
        if e not in result:
            result.append(e)

    return result

    #return set(lst)

print(dedup(['banana','banana','banana','abacaxi','caqui']))