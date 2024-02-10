def pyfagor(a, b):
    return (a**2 + b**2)**0.5

def main():
    x = float(input('>>> '))
    y = float(input('>>> '))
    hypotenus = pyfagor(x, y)
    print(hypotenus)

main()