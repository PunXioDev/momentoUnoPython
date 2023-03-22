iterador = 0
idCuenta = 0
cuentas = []

while iterador <= 10:
    if (iterador != 10):
        idCuenta += 1
        cuenta = {}

        cuenta["idCuenta"] = idCuenta
        cuenta["numeroCuenta"] = int(input(f"Digita el numero de la cuenta para {cuenta['idCuenta']}: "))
        cuenta["saldo"] = float(input(f"Digita el saldo de la cuenta {cuenta['numeroCuenta']}: "))

        cuentas.append(cuenta)

        print(f"cuenta {cuenta['idCuenta']} registrada con el saldo {cuenta['saldo']}")

        iterador += 1

    elif (iterador >= 10 and len(cuentas) == 10):
        for auxCuenta in reversed(cuentas):
            print(f"IdCuenta: {auxCuenta['idCuenta']}")
            print(f"Numero cuenta: {auxCuenta['numeroCuenta']}")
            print(f"Saldo: {auxCuenta['saldo']}")
            print("***")
        break
