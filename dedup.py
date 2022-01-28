def dedup(lst):
    '''
    Remove duplicates from lst
    :param lst: a list
    :return: new list without duplicated elements

    linear for time and space
    '''
    result = []
    repeated = set()

    for e in lst:
        if e not in repeated:
            result.append(e)
            repeated.add(e)

    return result

    #return set(lst)

print(dedup(['banana','banana','banana','abacaxi','caqui']))