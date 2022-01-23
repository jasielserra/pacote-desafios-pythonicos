from random import shuffle

def max_min(lst):
    ''' Calculate the maximun and minimum of a list lst
     :param lst: list
     :return: tuple
     '''
    if len(lst) == 0: # lst = [1, ... 99]
        raise ValueError('Empty List')
    return max(lst), min(lst) # O(n + n) = O(2n) = O(n) #tempo linear

print(max_min([1])) # 1,1
print(max_min([1,2])) # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(list(range(100)))) # 99,0
print(max_min([]))