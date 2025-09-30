"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Personajes Warhammer 40k
Fecha: 29/09/2025
Autor: Grupo 1 - Integrantes: Matías Odiz

Descripción:
Gestión de personajes de Warhammer 40k: crear, leer, actualizar, eliminar e imprimir.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
# No se requieren módulos externos


#----------------------------------------------------------------------------------------------
# DATOS INICIALES
#----------------------------------------------------------------------------------------------
facciones_validas = (
    "Ultramarines", "Black Legion", "Aeldari", "Orkos", "Necrones",
    "Imperial Fists", "Blood Angels", "Dark Angels", "Space Wolves",
    "Iron Hands", "Salamanders", "Raven Guard", "White Scars",
    "Death Guard", "Thousand Sons", "World Eaters", "Emperor's Children",
    "Tau Empire", "Tyranids", "Drukhari", "Craftworld Eldar",
    "Harlequins", "Ynnari", "Chaos Space Marines", "Daemons",
    "Imperial Guard", "Adeptus Mechanicus", "Sisters of Battle",
    "Grey Knights", "Deathwatch", "Custodes"
)

personajes_40k = {
    "Guilliman": {
        "nombre": "Roboute Guilliman",
        "faccion": "Ultramarines",
        "rol": "Primarca",
        "arma": "Espada del Emperador",
        "estado": "Vivo"
    },
    "Abaddon": {
        "nombre": "Abaddon el Saqueador",
        "faccion": "Black Legion",
        "rol": "Señor del Caos",
        "arma": "Garra de Horus",
        "estado": "Activo"
    },
    "Eldrad": {
        "nombre": "Eldrad Ulthran",
        "faccion": "Aeldari",
        "rol": "Vidente",
        "arma": "Lanza bruja",
        "estado": "Activo"
    },
    "Ghazghkull": {
        "nombre": "Ghazghkull Thraka",
        "faccion": "Orkos",
        "rol": "Kaudillo",
        "arma": "Garra de poder",
        "estado": "Activo"
    },
    "Trazyn": {
        "nombre": "Trazyn el Infinito",
        "faccion": "Necrones",
        "rol": "Señor Necrón",
        "arma": "Empalador",
        "estado": "Activo"
    }
}

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crear_personaje(clave, nombre, faccion, rol, arma, estado="Activo"):
    if clave in personajes_40k:
        print(f"El personaje con clave '{clave}' ya existe.")
        return False
    if faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        print("Facciones válidas disponibles:")
        for i, f in enumerate(facciones_validas, 1):
            print(f"  {i}. {f}")
        return False
    personajes_40k[clave] = {
        "nombre": nombre,
        "faccion": faccion,
        "rol": rol,
        "arma": arma,
        "estado": estado
    }
    print(f"✅ Personaje '{nombre}' creado exitosamente con clave '{clave}'.")
    return True

def leer_personaje(clave):
    if clave not in personajes_40k:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return None
    personaje = personajes_40k[clave]
    print(f"\n=== Información del personaje '{clave}' ===")
    print(f"Nombre: {personaje['nombre']}")
    print(f"Facción: {personaje['faccion']}")
    print(f"Rol: {personaje['rol']}")
    print(f"Arma: {personaje['arma']}")
    print(f"Estado: {personaje['estado']}")
    print("=" * 40)
    return personaje

def actualizar_personaje(clave, nombre=None, faccion=None, rol=None, arma=None, estado=None):
    if clave not in personajes_40k:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return False
    if faccion is not None and faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        print("Facciones válidas disponibles:")
        for i, f in enumerate(facciones_validas, 1):
            print(f"  {i}. {f}")
        return False
    if nombre is not None:
        personajes_40k[clave]["nombre"] = nombre
        print(f"Nombre actualizado a '{nombre}' para el personaje '{clave}'.")
    if faccion is not None:
        personajes_40k[clave]["faccion"] = faccion
        print(f"Facción actualizada a '{faccion}' para el personaje '{clave}'.")
    if rol is not None:
        personajes_40k[clave]["rol"] = rol
        print(f"Rol actualizado a '{rol}' para el personaje '{clave}'.")
    if arma is not None:
        personajes_40k[clave]["arma"] = arma
        print(f"Arma actualizada a '{arma}' para el personaje '{clave}'.")
    if estado is not None:
        personajes_40k[clave]["estado"] = estado
        print(f"Estado actualizado a '{estado}' para el personaje '{clave}'.")
    return True

def eliminar_personaje(clave):
    if clave not in personajes_40k:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return False
    personajes_40k[clave]["estado"] = "Inactivo"
    print(f"Personaje '{clave}' eliminado (estado cambiado a 'Inactivo').")
    return True

def borrar_personaje(clave):
    """Elimina completamente el personaje del diccionario."""
    if clave in personajes_40k:
        del personajes_40k[clave]
        print(f"Personaje '{clave}' borrado definitivamente.")
        return True
    else:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return False

def personajes_activos():
    """Lista por comprensión y función lambda: muestra nombres de personajes activos."""
    activos = list(filter(lambda x: personajes_40k[x]['estado'] == 'Activo', personajes_40k))
    nombres = [personajes_40k[clave]['nombre'] for clave in activos]
    print("\nPersonajes activos:")
    for nombre in nombres:
        print(f"- {nombre}")
    if not nombres:
        print("No hay personajes activos.")

def imprimir_personaje_por_clave(clave):
    return leer_personaje(clave) is not None

def listar_personajes():
    print("\n--- Lista de personajes Warhammer 40k ---")
    for clave, datos in personajes_40k.items():
        print(f"{clave}: {datos['nombre']} ({datos['faccion']}) - Estado: {datos['estado']}")
    print("-----------------------------------------")

def reporte_tabla_completa():
    print("\n{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
        "Clave", "Nombre", "Facción", "Rol", "Arma", "Estado"))
    print("-" * 100)
    for clave, datos in personajes_40k.items():
        print("{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
            clave, datos['nombre'], datos['faccion'], datos['rol'], datos['arma'], datos['estado']))
    print("-" * 100)

def reporte_conteo_faccion():
    conteo = {}
    for datos in personajes_40k.values():
        faccion = datos['faccion']
        conteo[faccion] = conteo.get(faccion, 0) + 1
    print("\n--- Conteo de personajes por facción ---")
    for faccion, cantidad in conteo.items():
        print(f"{faccion}: {cantidad}")
    print("----------------------------------------")

#----------------------------------------------------------------------------------------------
# MENÚ PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    while True:
        print("\n---------------------------")
        print("--- MENÚ WARHAMMER 40K ---")
        print("---------------------------")
        print("[1] Agregar personaje")
        print("[2] Consultar personaje")
        print("[3] Actualizar personaje")
        print("[4] Eliminar personaje (estado Inactivo)")
        print("[5] Imprimir personaje")
        print("[6] Listar todos los personajes")
        print("[7] Borrar personaje definitivamente")
        print("[8] Mostrar personajes activos (lambda y comprensión)")
        print("[9] Reporte tabla completa")
        print("[10] Reporte conteo por facción")
        print("[0] Salir")
        print("---------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("¡Hasta la próxima batalla!")
            break

        elif opcion == "1":
            clave = input("Clave única del personaje: ")
            nombre = input("Nombre completo: ")
            print("Facciones válidas:")
            for i, f in enumerate(facciones_validas, 1):
                print(f"{i}. {f}")
            faccion = input("Facción: ")
            rol = input("Rol: ")
            arma = input("Arma principal: ")
            estado = input("Estado (Activo/Vivo/Inactivo): ")
            crear_personaje(clave, nombre, faccion, rol, arma, estado)

        elif opcion == "2":
            clave = input("Ingrese la clave del personaje a consultar: ")
            leer_personaje(clave)

        elif opcion == "3":
            clave = input("Ingrese la clave del personaje a actualizar: ")
            print("Deje vacío el campo que no desea modificar.")
            nombre = input("Nuevo nombre: ")
            faccion = input("Nueva facción: ")
            rol = input("Nuevo rol: ")
            arma = input("Nueva arma: ")
            estado = input("Nuevo estado: ")
            actualizar_personaje(
                clave,
                nombre if nombre else None,
                faccion if faccion else None,
                rol if rol else None,
                arma if arma else None,
                estado if estado else None
            )

        elif opcion == "4":
            clave = input("Ingrese la clave del personaje a eliminar: ")
            eliminar_personaje(clave)

        elif opcion == "5":
            clave = input("Ingrese la clave del personaje a imprimir: ")
            imprimir_personaje_por_clave(clave)

        elif opcion == "6":
            listar_personajes()

        elif opcion == "7":
            clave = input("Ingrese la clave del personaje a borrar definitivamente: ")
            borrar_personaje(clave)

        elif opcion == "8":
            personajes_activos()

        elif opcion == "9":
            reporte_tabla_completa()

        elif opcion == "10":
            reporte_conteo_faccion()

        else:
            print("Opción inválida. Intente nuevamente.")

        input("\nPresione ENTER para volver al menú.")

# Punto de entrada al programa
main()