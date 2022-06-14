import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def validar_correo(email: str) -> bool:
    return bool(re.fullmatch(regex, email))


def filtrar_coreo(origen, destino):
    with open(origen, 'r') as archivo_origen:
        for x in archivo_origen:
            if validar_correo(x):
                with open(destino, 'a') as archivo_destino:
                    if x not in archivo_destino:
                        archivo_destino.write(x.lower())


print(filtrar_coreo('correos.txt', 'palabra.txt'))
