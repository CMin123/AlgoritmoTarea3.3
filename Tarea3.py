class empleado: 
    def __init__(self, rol, nombre, cedula, balance):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula
        self.balance = balance

    def __str__(self):
        return (f"""
    Soy un empleado:
        Rol: {self.rol}
        Nombre: {self.nombre}
        Cedula: {self.cedula}
        Balance = {self.balance}


    """)

    def retirar(self, monto):
        self.balance = self.balance - monto

    def agregar(self, monto):
        self.balance = self.balance + monto


class nomina:
    def __init__(self,presupuesto,candidadDinero, empleados):
        self.presupuesto = presupuesto
        self.cantidadDinero = candidadDinero
        self.empleados = empleados

    global listaEmpleados
    listaEmpleados = []

    def agregarEmpleados(self):
        listaEmpleados.append(self.empleados)
    
    def mostrarEmpleados(self):
        for x in listaEmpleados:
            print(f"Rol: {x.rol}, nombre: {x.nombre}, cedula: {x.nombre}, balance: {x.balance}")
            print(x)
        

    def pagar(self):
        self.presupuesto = 0
        for empleado in listaEmpleados:
            match empleado.rol:
                case "Programador Junior":
                    self.presupuesto = self.presupuesto + 1000

                case "Programador Senior":
                    self.presupuesto = self.presupuesto + 2000

                case "Manager":
                    self.presupuesto = self.presupuesto + 3000

        print(f"El presupuesto es de: {self.presupuesto}")

        if self.presupuesto > self.cantidadDinero:
            print("No se puede pagar con esta cantidad de dinero")
            return
        
        else:
            print("Se pueden pagar los empleados")
            for empleado in listaEmpleados:
                match empleado.rol:
                    case "Programador Junior":
                        empleado.agregar(1000)
                        print(empleado)

                    case "Programador Senior":
                        empleado.agregar(2000)
                        print(empleado)

                    case "Manager":
                        empleado.agregar(3000)
                        print(empleado)

class app:
    
    def menu(self):
        opciones = input("""
            1: Registrar Empleados
                    
            2: Pagar Empleados

    """)
        
        match opciones:
            case "1":
                self.registradorEmpleados()

            case "2":
                self.pagarEmpleados()

        self.menu()

            
    def registradorEmpleados(self):
        rol = input("Introduzca el rol del empleado: ")
        nombre = input("Introduzca el nombre del empleado: ")
        cedula = input("Introduzca la cedula: ")
        while not cedula.isnumeric():
            cedula = input("Solo pueden ser numeros: ")
        balance = input("Introduzca el Balance: ")
        while not balance.isnumeric():
            balance = input("Solo numeros: ")
        balance = int(balance)
        
        empleados = empleado(rol, nombre, cedula, balance)
        nominas = nomina(None, None, empleados)
        nominas.agregarEmpleados()
        nominas.mostrarEmpleados()
        
    def pagarEmpleados(self):
        cantidadDinero = input("Introduzca la cantidad de dinero disponible: ")
        while not cantidadDinero.isnumeric():
            cantidadDinero = input("Solo numeros: ")
        cantidadDinero = int(cantidadDinero)
        nominas = nomina(None, cantidadDinero, None)
        nominas.pagar()
        

Runner = app()
Runner.menu()

print("Arreglo Agregado")

print("Version final")