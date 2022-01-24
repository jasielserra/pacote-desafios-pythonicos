from random import shuffle

def max_min(lst):
    ''' Calculate the maximun and minimum of a list lst
     :param lst: list
     :return: tuple
     '''
    n = len(lst)
    if n == 0: # lst = [1, ... 99] #O(n)
        raise ValueError('Empty List')    #O(n)
    max_value = min_value = lst[-1]       #O(n)

    def max_min_rec(cursor):
        nonlocal max_value, min_value
        if cursor < 0:
            return max_value, min_value
        current = lst[cursor]
        if current > max_value:
            max_value = current
        if current < min_value:
            min_value = current
        return max_min_rec(cursor - 1)

    return max_min_rec(n-1)




print(max_min([1])) # 1,1
print(max_min([1,2])) # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(list(range(100)))) # 99,0
print(max_min([]))