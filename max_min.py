from random import shuffle

def max_min(lst):
    ''' Calculate the maximun and minimum of a list lst
     :param lst: list
     :return: tuple
     '''
    if len(lst) == 0: # lst = [1, ... 99] #O(n)
        raise ValueError('Empty List')    #O(n)
    max_value = min_value = lst[0]        #O(n)
 #   return max(lst), min(lst) # Utilizando a biblioteca embutida O(n + n) = O(2n) = O(n)

    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value # O(n) Tempo Linear

print(max_min([1])) # 1,1
print(max_min([1,2])) # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(list(range(100)))) # 99,0
print(max_min([]))