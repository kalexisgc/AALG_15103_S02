"""
Cree una clase Persona en python con los atributos nombre y DNI, y cree un aplicativo con un menú con tres opciones:
1. Crear persona, donde pedirá los datos y creará una persona y la agregará a la lista.
2. Listar, donde mostrará todas las personas que hay en la lista.
3. Eliminar, donde pedirá un DNI y borrará a la persona que tenga ese DNI de la lista.
Habrá también una cuarta opción, que es Salir.

"""
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}"


lista_personas = []

while True:
    print("\n--- MENÚ ---")
    print("1. Crear persona")
    print("2. Listar personas")
    print("3. Eliminar persona por DNI")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre: ")
        dni = input("Ingrese DNI: ")
        persona = Persona(nombre, dni)
        lista_personas.append(persona)
        print("Persona agregada.")

    elif opcion == "2":
        if len(lista_personas) == 0:
            print("No hay personas en la lista.")
        else:
            print("\nLista de personas:")
            for p in lista_personas:
                print(p)

    elif opcion == "3":
        dni_eliminar = input("Ingrese el DNI a eliminar: ")
        encontrada = False

        for p in lista_personas:
            if p.dni == dni_eliminar:
                lista_personas.remove(p)
                print("Persona eliminada.")
                encontrada = True
                break

        if not encontrada:
            print("No se encontró una persona con ese DNI.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")