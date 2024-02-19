class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0) -> None:
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self) -> str:
        return f"Titular: {self.nombre} {self.apellido}\n Balance de la cuenta: {self.numero_cuenta}: ${self.balance}"

    def depositar(self, cantidad) -> None:
        self.balance += cantidad
        print(
            f"Su deposito por {cantidad} pesos ha sido realizado! Su nuevo balance es de: ${self.balance} pesos.")

    def retirar(self, cantidad) -> None:
        if self.balance < cantidad:
            return print(f"No tiene suficiente dinero en su cuenta. Balance: ${self.balance}")

        self.balance -= cantidad
        print(
            f"Su retiro por {cantidad} pesos ha sido realizado! Su nuevo balance es de: {self.balance} pesos.")


def volver_inicio() -> None:
    eleccion = 'x'
    while eleccion != 's':
        print("Ingrese 's' para regresar al inicio!")
        eleccion = input("Opcion:")


def crear_cuenta() -> Cliente:
    print("*"*55)
    print("Creemos una cuenta!")
    print("*"*55)
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese el numero de cuenta que desea: ")
    nuevo_cliente = Cliente(nombre, apellido, numero_cuenta)
    print("Su cuenta ha sido creada con exito!")
    print(nuevo_cliente)
    eleccion = 'x'
    while eleccion != 's':
        print("Ingrese 's' para ingresar al systema del banco!")
        eleccion = input("Opcion:")
    return nuevo_cliente


def inicio() -> int:
    nuevo_cliente = crear_cuenta()
    print("*"*55)
    print("Bienvenido al banco! Que es lo que desea hacer el dia de hoy?")
    print("*"*55)
    menu = 0
    while menu != 's':
        print(
            "Opciones: \n[d] - Depositar \n[r] - Retirar \n[c] - Consultar Cuenta Actual \n[s] - Salir")
        menu = input("Opcion: ")
        if menu == 'd':
            deposito = input("Ingrese la cantidad a depositar: $")
            nuevo_cliente.depositar(int(deposito))
            volver_inicio()
        elif menu == 'r':
            retiro = input("Ingrese la cantidad a retirar: $")
            nuevo_cliente.retirar(int(retiro))
            volver_inicio()
        elif menu == 'c':
            print(nuevo_cliente)
            volver_inicio()
        elif menu == 's':
            print("*"*55)
            print("Saliendo del progama, gracias  por usar nuestro banco!")
            print("*"*55)


inicio()
