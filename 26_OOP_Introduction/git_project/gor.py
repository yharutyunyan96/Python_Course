def fibo(n): return n if n <= 1 else fibo(n-1) + fibo(n-2)

def main():
    import sys
    n = int(sys.argv[1])
    result = fibo(n)
    print(result)

main()
