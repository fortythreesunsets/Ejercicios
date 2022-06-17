def numeros_primos(num):
    print(f'Números primos entre 1 y {num}:')
    num_primos = []
    for n in range(1, num):
        if n > 1:
            if n == 2 or n == 3 or n == 5:
                num_primos.append(n)
            elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
                num_primos.append(n)
    print(num_primos)


num = int(input("Introduce un número para calcular los números primos hasta ese número: "))
numeros_primos(num)
