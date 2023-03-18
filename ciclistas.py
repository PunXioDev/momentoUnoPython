
# fecha
idDeCiclista = 0
ciclistas = []
options = 1


def findCiclista(codigoDeCiclista):
    for ciclista in ciclistas:
        if (ciclista['codigo'] == codigoDeCiclista):
            print(f"ciclista: ")
            print(ciclista['id'])
            print(ciclista['codigo'])
            print(ciclista['nombre'])
            print(ciclista['edad'])
            print(ciclista['pais'])
            print(ciclista['equipo'])
            print(ciclista['tiempo'])
            print(f"**")


def findCiclistas():
    for ciclista in ciclistas:
        if (ciclista):
            print(f"ciclista: ")
            print(ciclista['id'])
            print(ciclista['codigo'])
            print(ciclista['nombre'])
            print(ciclista['edad'])
            print(ciclista['pais'])
            print(ciclista['equipo'])
            print(ciclista['tiempo'])
            print(f"**")
        else:
            print(f"No hay ciclistas")


def deleteciclista(codigociclista):
    for ciclista in ciclistas:
        if (ciclista['codigo'] == codigociclista):
            ciclistas.remove(ciclista)


while options != 0:
    print(f"*****")
    print(f"*Opcion 1: Registrar ciclista*")
    print(f"*Opcion 2: Ver ciclistas*")
    print(f"*Opcion 3: Modificar tiempo de un ciclista*")
    print(f"*Opcion 4: Eliminar un ciclista*")
    print(f"*Opcion 5: eliminar TODOS los ciclistas*")
    print(f"*Presiona 0 para cerrar.*")
    print(f"*****")
    options = int(input("Digite una opción: "))
    print(f"*****")

    if (options == 1):
        print(f"*****")
        print(f"Estas registrando un ciclista")
        print(f"*****")

        idDeCiclista += 1
        ciclista = {}

        ciclista['id'] = idDeCiclista
        ciclista['codigo'] = int(
            input(f"Digite el codigo del ciclista {ciclista['id']}: "))
        ciclista['nombre'] = input(
            f"Digite el nombre del ciclista {ciclista['codigo']}: ")
        ciclista['edad'] = input(
            f"Digite la edad del ciclista {ciclista['nombre']}: ")
        ciclista['pais'] = input(
            f"Digite el pais del ciclista {ciclista['nombre']}: ")
        ciclista['equipo'] = input(
            f"Digite el equipo del ciclista {ciclista['nombre']}: ")
        ciclista['tiempo'] = float(
            input(f"Digite el tiempo del ciclista {ciclista['nombre']}: "))

        for ciclistaForCreate in ciclistas:
            if (ciclistaForCreate['codigo'] == ciclista['codigo']):
                print(
                    f"El ciclista ya existe. El dueno es: {ciclistaForCreate['nombre']}")
                options = 1
            else:
                pass

        if (ciclista):
            ciclistas.append(ciclista)

    elif (options == 2):
        print(f"*****")
        print(f"Estas viendo los ciclistas")
        findCiclistas()
        print(f"*****")

    elif (options == 3):
        print(f"*****")
        print(f"Estas modificando un ciclista")
        print(f"*****")

        ciclistaUpdate = int(
            input("Digite el codigo del ciclista que quiere actualizar: "))

        for ciclistaForUpdate in ciclistas:
            if (ciclistaForUpdate['codigo'] == ciclistaUpdate):
                print(
                    f"El ciclista {ciclistaUpdate} esta registrado para {ciclistaForUpdate['nombre']}")
                findCiclista(ciclistaUpdate)
            else:
                pass
        ciclistaForUpdate['tiempo'] = input(
            f"Digite el nuevo tiempo del ciclista {ciclistaForUpdate['nombre']}: ")
        findCiclistas()

    elif (options == 4):
        print(f"*****")
        print(f"Estas eliminando un ciclista")
        print(f"*****")

        numciclista = int(input(f'Digite el codigo del ciclista a eliminar: '))
        delete = input(
            f'¿Seguro que quieres eliminar el ciclista {numciclista}? (S/n) ')
        if (delete == 's' or delete == 'S'):
            deleteciclista(numciclista)
            print('Se elimino el ciclista. Los ciclistas actuales son:')
            findCiclistas()
        elif (delete == 'n' or delete == 'N'):
            options = int(input("Digite una opción (entre 1 a 2): "))

    elif (options == 5):
        print(f"*****")
        ciclistas.clear()
        codigoDeciclista = 0
        print(f"Se elimino todos los ciclistas")
        print(f"*****")
        findCiclistas()
    else:
        print(f"*****")
        options = int(input("Digite una opción (entre 1 y 5): "))
        print(f"*****")
