# Rekursive Funktion: Fibonacci Reihe
def fib(n=5):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)


def fiblist(m=5):
    i = 0
    L = None
    L = []
    while i <= m:
        L.append(fib(i))
        i += 1
    return "Die Fibonacci Reihe von 0 bis " + str(m) + " lautet: \n" + str(L)

