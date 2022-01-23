def max_min(lst):
    ''' Calculate the maximun and minimum of a list lst
     :param lst: list
     :return: tuple
     '''
    if len(lst) == 0:
        raise ValueError('Empty List')
    return lst[-1], lst[0]
