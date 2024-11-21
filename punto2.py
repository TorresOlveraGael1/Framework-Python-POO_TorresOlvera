#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).

print(" ")
print("Torres Olvera Gael")
print(" ")

# Definimos la clase Persona, ya que se menciona que el titular es una persona
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

#Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=1000):
        self.titular = titular  #titular es una instancia de la clase Persona
        self.cantidad = cantidad  #cantidad es un valor numérico (float por ejemplo)

    # Setters
    def set_titular(self, titular):
        self.titular = titular

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    # Getters
    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    #Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad en cuenta: {self.cantidad:.2f}")

    #Método para ingresar dinero en la cuenta
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad:.2f} a la cuenta. Saldo actual: {self.cantidad:.2f}")
        else:
            print("Cantidad negativa. No se ha realizado el ingreso.")

    #Método para retirar dinero de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0:
            if self.cantidad >= cantidad:
                self.cantidad -= cantidad
                print(f"Se han retirado {cantidad:.2f} de la cuenta. Saldo actual: {self.cantidad:.2f}")
            else:
                print("No hay suficiente saldo en la cuenta para realizar este retiro.")
        else:
            print("Cantidad negativa. No se ha realizado el retiro.")

#Solicitar los datos al usuario
nombre_titular = input("Nombre del Titular: ")
cantidad_inicial = float(input("Cantidad inicial en la cuenta: "))
cantidad_a_ingresar = float(input("Cantidad deseada a ingresar en la cuenta: "))
cantidad_a_retirar = float(input("Cantidad deseada a retirar en la cuenta: "))

#Crear un objeto de la clase Persona y un objeto de la clase Cuenta
titular = Persona(nombre_titular)
cuenta = Cuenta(titular, cantidad_inicial)

#Ejemplo de operaciones
cuenta.ingresar(cantidad_a_ingresar)  #Ingresar dinero
cuenta.retirar(cantidad_a_retirar)   #Retirar dinero
