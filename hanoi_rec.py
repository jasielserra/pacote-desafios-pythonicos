def hanoi(discos, orig='A', aux='B', dest='C'):
    """Recursive Solution to Hanoi Tower
      t(n) = 1 + 2(t(n-1))
      t(n) = 1 + 2 + 4(t(n-2))
      t(n) = 1 + 2 + 4 + 8(t(n-3))
      t(n) = 1 + 2 + 4 + 8 + 16(t(n-4))
      t(n) = 1 + 2 + 4 + 8 + 16 ... 2**n
      2(t(n)) = 2 + 4 + 8 + 16 + 32 ... 2**(n+1)
      t(n)=2**(n+1)-1 => O(2**n)
      m(n) = 1 + m(n-1) => O(n)
      """

    if discos >= 1:
        hanoi(discos-1, orig, dest, aux)
        print(f'{orig} -> {dest} : {discos}')
        hanoi(discos-1, aux, orig, dest)

for i in range(1,4):
    print('####### Hanoi %s' %i)
    hanoi(i)