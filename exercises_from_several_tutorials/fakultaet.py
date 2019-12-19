# Rekursionsformel für Berechnung der Fakultät n!
# 0! = 1
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6

def fak(n=1):
    if n<=1:
        return 1
    else:
        return fak(n-1)*n
