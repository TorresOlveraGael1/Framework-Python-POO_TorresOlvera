#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior

print(" ")
print("Torres Olvera Gael")
print(" ")

#Clase Persona
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def es_menor_de_25(self):
        return self.edad < 25


#Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=1000):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}")
        print(f"Cantidad en cuenta: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Ingresado: {cantidad:.2f}. Saldo actual: {self.cantidad:.2f}")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Retirado: {cantidad:.2f}. Saldo actual: {self.cantidad:.2f}")
        else:
            print("Cantidad inválida o insuficiente.")


#Clase CuentaJoven que hereda de Cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=1000, bonificacion=0.05):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.es_menor_de_25()

    def mostrar(self):
        print(f"Cuenta Joven de {self.titular.nombre}")
        print(f"Bonificación: {self.bonificacion * 100:.2f}%")
        super().mostrar()


#Solicitar datos al usuario
nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
dni = input("Introduce el DNI: ")

#Crear el objeto Persona
persona = Persona(nombre, edad, dni)

#Verificar si es válido para una Cuenta Joven
if persona.es_mayor_de_edad() and persona.es_menor_de_25():
    bonificacion = float(input("Introduce la bonificación (en decimal, ej. 0.05 para 5%): "))
    cuenta_joven = CuentaJoven(persona, 1000, bonificacion)
    
    #Mostrar los detalles de la cuenta joven
    cuenta_joven.mostrar()

    #Realizar un retiro
    retiro = float(input("Introduce la cantidad a retirar: "))
    cuenta_joven.retirar(retiro)
else:
    print("El titular no es válido para una Cuenta Joven.")
