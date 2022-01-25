def hanoi(n, orig='A', aux='B', dest='C'):
    '''Recursive Solution to Hanoi Tower'''

    if n >= 1:
        hanoi(n-1, orig, dest, aux)
        print('{} -> {} : {}'.format(orig, dest, n))
        hanoi(n-1, aux, orig, dest)

for i in range(1,4):
    print('####### Hanoi %s' %i)
    hanoi(i)