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
    def mostrar(self): 
        return f"Nombre: {self.nombre} | DNI: {self.dni}" 
personas = [] 
while True: 
    print("\n--- MENÚ ---") 
    print("1. Crear persona") 
    print("2. Listar personas") 
    print("3. Eliminar persona") 
    print("4. Salir") 
    opcion = input("Seleccione una opción: ") 
    if opcion == "1": 
        nombre = input("Ingrese nombre: ") 
        dni = input("Ingrese DNI: ") 
        nueva_persona = Persona(nombre, dni) 
        personas.append(nueva_persona) 
        print("Persona agregada correctamente.")
    elif opcion == "2": 
        if not personas:
            print("No hay personas registradas.") 
        else: 
            for persona in personas: 
                print(persona.mostrar())
    elif opcion == "3": 
        dni_buscar = input("Ingrese DNI a eliminar: ") 
        eliminado = False 
        for persona in personas: 
            if persona.dni == dni_buscar: 
                personas.remove(persona) 
                eliminado = True 
                print("Persona eliminada.") 
                break
        if not eliminado: 
            print("No se encontró ese DNI.") 
    elif opcion == "4": 
        print("Saliendo del programa...") 
        break
    else: 
        print("Opción inválida.")