print(" ")
print("Torres Olvera Gael")
print(" ")

class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.nombre = nombre
        self.edad = edad if isinstance(edad, int) and edad >= 0 else None  #Validación inicial de edad
        self.dni = dni
        if dni:  #Verificación del DNI solo si se proporciona
            self.set_dni(dni)  #Usar el setter para el DNI desde el constructor

    #Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Edad no válida. Debe ser un número entero positivo.")

    def set_dni(self, dni):
        if len(dni) == 9 and dni[:8].isdigit() and dni[-1].isalpha():
            self.dni = dni
        else:
            print("DNI no válido. Debe tener 8 dígitos seguidos de una letra.")

    #Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_dni(self):
        return self.dni

    #Mostrar los datos
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad if self.edad is not None else 'No especificada'}")
        print(f"DNI: {self.dni if self.dni else 'No especificado'}")

    #Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad is not None:
            return self.edad >= 18
        else:
            return False

#Solicitar datos al usuario
nombre_usuario = input("Introduce el nombre de la persona: ")
edad_usuario = input("Introduce la edad de la persona: ")
dni_usuario = input("Introduce el DNI de la persona (8 dígitos + letra): ")

#Validar que la edad sea un número entero positivo
while not edad_usuario.isdigit() or int(edad_usuario) < 0:
    print("Edad no válida. Debe ser un número entero positivo.")
    edad_usuario = input("Introduce la edad de la persona: ")

#Crear un objeto de la clase Persona con los datos proporcionados
persona = Persona(nombre_usuario, int(edad_usuario), dni_usuario)

#Mostrar los datos de la persona
persona.mostrar()

#Verificar si la persona es mayor de edad
if persona.es_mayor_de_edad():
    print(f"{persona.get_nombre()} es mayor de edad.")
else:
    print(f"{persona.get_nombre()} no es mayor de edad.")
