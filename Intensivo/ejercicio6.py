def generar_key(password):
    key = 0
    for c in range(len(password)):
        key = key * 10 + (ord(password[c]) - ord('0'))
    return key


def quitar_no_alnum(caracter, key):
    caracter_ascii = ord(caracter)
    while caracter_ascii < 48 or 57 < caracter_ascii < 65 or 90 < caracter_ascii > 97 or caracter_ascii > 122:
        if caracter_ascii < 48:
            caracter_ascii = chr(((caracter_ascii - ord('0') + key) % 26) + ord('0') + 16)
            return caracter_ascii

        if 57 < caracter_ascii < 65:
            caracter_ascii = chr(((caracter_ascii - ord('0') + key) % 26) + ord('0') + 32)
            return caracter_ascii

        if 90 < caracter_ascii < 97:
            caracter_ascii = chr(((caracter_ascii - ord('a') + key) % 26) + ord('a'))
            return caracter_ascii

        if caracter_ascii > 122:
            caracter_ascii = chr(((caracter_ascii - ord('N') + key) % 26) + ord('N') - 99)
            return caracter_ascii


def convertir_password(password):
    psswrd = []
    num = 0
    caracteres = 'rdUO1EBn6aFt5W2RysKri3jct5Hvg86m0'

    for i in password:
        psswrd.append(i)
        num += 1

    for i in range(len(password) + 1, 33):
        psswrd.append(caracteres[i])
    print(psswrd)

    key = generar_key(password)

    password_enc = ''
    for i in range(len(psswrd)):
        if psswrd[i].isalpha():
            if psswrd[i].isupper():
                caracter = chr(((ord(psswrd[i]) - ord('A') + key) % 26) + ord('A'))
                if caracter.isalnum():
                    password_enc = password_enc + caracter
                else:
                    password_enc = password_enc + quitar_no_alnum(caracter, key)
            elif psswrd[i].islower():
                caracter = chr(((ord(psswrd[i]) - ord('a') + key) % 26) + ord('a'))
                if caracter.isalnum():
                    password_enc = password_enc + caracter
                else:
                    password_enc = password_enc + quitar_no_alnum(caracter, key)
        elif psswrd[i].isnumeric():
            caracter = chr(((ord(psswrd[i]) - ord('0')) + key % 26) + ord('0'))
            if caracter.isalnum():
                password_enc = password_enc + caracter
            else:
                password_enc = password_enc + quitar_no_alnum(caracter, key)
        else:
            caracter = psswrd[i]
            password_enc = password_enc + str(quitar_no_alnum(caracter, key))

    return password_enc


password = input('Password (6-12 caracteres): ')
resultado = convertir_password(password)
print(resultado)
