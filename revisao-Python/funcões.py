#exercicio 20
def volume(c, r):
    v = c * r
    return v

#exercicio 21
def maior_numero(n1, n2, n3, n4, n5):

    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        print(f'O numero maior é o {n1}')
    elif  n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print(f'O numero maior é o {n2}')
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print(f'O numero maior é o {n3}')
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print(f'O numero maior é o {n4}')
    else:
        print(f'O numero maior é o {n5}')

#exercicio 22
def media_numero(n1, n2, n3, n4, n5):

    m = (n1 + n2 + n3 + n4 +n5) / 5
    return m
