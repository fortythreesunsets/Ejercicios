def numeros_primos(num):
    print(f'Números primos entre 1 y {num}:')
    num_primos = []
    for n in range(1, num+1):
        div = 0
        x = n//2
        for i in range(2, (x + 1)):
            if n % i == 0:
                div += 1
                break
        if div == 0 and n > 1:
            num_primos.append(n)
    print(num_primos)


num = int(input("Introduce un número para calcular los números primos hasta ese número: "))
numeros_primos(num)
