import os

def formato_directorio():
    directorio = input('Directorio: ')
    dir = str(directorio).replace('\\', '/')
    return dir

def convertir_bytes(bytes):
    for i in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f'{bytes:3.2f} {i}'
        bytes /= 1024.0

directorio = os.scandir(formato_directorio())
print('\t\t\t\t\tARCHIVOS---------------------------- TAMAÑO')

for archivo in directorio:
    if archivo.is_file():
        nombre_archivo = str(archivo).lstrip("<DirEntry, '").rstrip("', >")
        size_archivo = os.stat(archivo).st_size
        print(f'{nombre_archivo} -------------- {convertir_bytes(size_archivo)}')
