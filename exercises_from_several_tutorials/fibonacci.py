import fibo

if __name__ == '__main__':
    print("Fie Rekursionsformel für die Fibonacci Reihe (hier fib()) lautet \n fib(n) = fib(n-1) + fib(n-2) \n ")
    f=int(input("Geben Sie n ein:"))
    print(fibo.fiblist(f))