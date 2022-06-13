def fat(n):
    if n == 0:
        return 1
    return n*fat(n-1)

def fatdiferente(n):
    prod = 1 
    for x in range(1,n+1):
        prod *= x
    return prod
