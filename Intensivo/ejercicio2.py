import os
import time

# para que se pueda limpiar la pantalla: Edit Configurations > Execution: Emulate terminal in output console
def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


def ordenar_agenda(agenda_desordenada):
    print('NOMBRE \t\t\t TELÉFONO')
    agenda_ordenada = sorted(agenda_desordenada)
    for contacto in agenda_ordenada:
        print(f'{contacto}\t\t{agenda[contacto]}')


agenda = {}
opcion = 0

while opcion != 6:

    print('AGENDA TELEFÓNICA POR CONSOLA')
    print('1. Agregar contacto')
    print('2. Modificar contacto')
    print('3. Eliminar contacto')
    print('4. Buscar contacto')
    print('5. Ver todos los contactos')
    print('6. Salir')

    opcion = int(input('Elige la opción que desees: '))
    cls()

    if opcion == 1:
        nombre = input('Nombre: ').title()
        telefono = input('Teléfono: ')
        if len(telefono) >= 10 and len(telefono) <= 12:
            agenda[nombre] = telefono
            print(f'Contacto guardado')
        else:
            print('Número telefónico debe tener entre 10 y 12 dígitos.\nIntenta de nuevo')
        time.sleep(2)
        cls()

    if opcion == 2:
        ordenar_agenda(agenda)
        nombre = input('\n¿Qué contacto deseas modificar?: ').title()
        if agenda.get(nombre):
            nuevo_nombre = input('Nuevo nombre: ').title()
            agenda[nuevo_nombre] = agenda.pop(nombre)
            nuevo_telefono = input('Nuevo teléfono: ')
            agenda.update({nuevo_nombre: nuevo_telefono})
            print(f'Contacto modificado')
        else:
            print('Contacto no encontrado')
        time.sleep(2)
        cls()

    if opcion == 3:
        ordenar_agenda(agenda)
        nombre = input('\n¿Qué contacto deseas eliminar?: ').title()
        del agenda[nombre]
        print(f'Contacto eliminado')
        time.sleep(2)
        cls()

    if opcion == 4:
        nombre = input('¿Qué contacto deseas buscar?: ').title()
        buscar = nombre[:5]
        resultado = dict(filter(lambda item: buscar in item[0], agenda.items()))
        if resultado == {}:
            print('Contacto no encontrado')
            time.sleep(2)
            cls()
        else:
            for r in resultado:
                print(f'Nombre: {r}\nTeléfono: {resultado[r]}\n')
        time.sleep(5)
        cls()

    if opcion == 5:
        ordenar_agenda(agenda)
        time.sleep(5)
        cls()
