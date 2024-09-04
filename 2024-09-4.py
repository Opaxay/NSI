liste = [10, 15, 12, 121]

def affichage (L = list) -> None:
    print ('La liste :')
    for i in range (len(L)) :
        print (f' {i}\t{L[i]}')
    print (f'Il y a {len(L)} éléments')
        
def moins_dix(L: list) -> list:
    for e in L:
        L.insert (L.index (e),e - 10)
        L. remove (e)
    affichage (L)
    return L

def impaire_iteration (n):
    L = []
    for i in range (1,n*2, 2) :
        L.append (i)

def comprehension (n) :
    L = [i for i in range(1, n * 2, 2)]

def fibonacci(n: int):
    L = [0, 1]
    for i in range(2, n):
        L.append(L[-1] + L[-2])
    return L