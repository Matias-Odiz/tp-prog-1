"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Personajes Warhammer 40k
Fecha: 27/10/2025
Autor: 

Descripción:
Gestión de personajes de Warhammer 40k: crear, leer, actualizar, eliminar e imprimir.
Actualiza automáticamente tanto el JSON como el diccionario Python en dic.py.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json
import os

#----------------------------------------------------------------------------------------------
# DATOS INICIALES
#----------------------------------------------------------------------------------------------
from dic import personajes_40k  # importa personajes base

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

ARCHIVO_JSON = "Archivos_administratum.json"
ARCHIVO_DIC = "dic.py"

#----------------------------------------------------------------------------------------------
# FUNCIONES AUXILIARES
#----------------------------------------------------------------------------------------------

def guardar_json(diccionario):
    """Guarda el diccionario en el archivo JSON."""
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(diccionario, f, indent=4, ensure_ascii=False)

def cargar_json():
    """Carga el diccionario desde el JSON si existe."""
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def guardar_dicpy(diccionario):
    """Actualiza el archivo dic.py con el contenido del diccionario."""
    with open(ARCHIVO_DIC, "w", encoding="utf-8") as f:
        f.write("personajes_40k = ")
        json.dump(diccionario, f, indent=4, ensure_ascii=False)
    print("Archivo dic.py actualizado correctamente.")

def sincronizar_archivos(diccionario):
    """Guarda tanto el JSON como el diccionario Python."""
    guardar_json(diccionario)
    guardar_dicpy(diccionario)

#----------------------------------------------------------------------------------------------
# FUNCIONES PRINCIPALES
#----------------------------------------------------------------------------------------------

def crear_personaje(clave, nombre, faccion, rol, arma, estado="Activo"):
    personajes = cargar_json()
    if clave in personajes:
        print(f"El personaje con clave '{clave}' ya existe.")
        return
    if faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        return
    personajes[clave] = {
        "nombre": nombre,
        "faccion": faccion,
        "rol": rol,
        "arma": arma,
        "estado": estado
    }
    sincronizar_archivos(personajes)
    print(f"Personaje '{nombre}' creado y guardado correctamente.")

def leer_personaje(clave):
    personajes = cargar_json()
    if clave not in personajes:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return
    p = personajes[clave]
    print(f"\n=== Información del personaje '{clave}' ===")
    for campo, valor in p.items():
        print(f"{campo.capitalize()}: {valor}")
    print("=" * 40)

def actualizar_personaje(clave, nombre=None, faccion=None, rol=None, arma=None, estado=None):
    personajes = cargar_json()
    if clave not in personajes:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return
    if faccion and faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        return
    if nombre: personajes[clave]["nombre"] = nombre
    if faccion: personajes[clave]["faccion"] = faccion
    if rol: personajes[clave]["rol"] = rol
    if arma: personajes[clave]["arma"] = arma
    if estado: personajes[clave]["estado"] = estado
    sincronizar_archivos(personajes)
    print(f"Personaje '{clave}' actualizado correctamente.")

def eliminar_personaje(clave):
    personajes = cargar_json()
    if clave not in personajes:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return
    personajes[clave]["estado"] = "Inactivo"
    sincronizar_archivos(personajes)
    print(f"Personaje '{clave}' marcado como 'Inactivo'.")

def borrar_personaje(clave):
    personajes = cargar_json()
    if clave not in personajes:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return
    del personajes[clave]
    sincronizar_archivos(personajes)
    print(f"Personaje '{clave}' eliminado definitivamente.")

def personajes_activos():
    personajes = cargar_json()
    activos = [p["nombre"] for p in personajes.values() if p["estado"].lower() == "activo"]
    with open("reporte.txt", "w", encoding="utf-8") as archivo:
        archivo.write("=== Personajes Activos ===\n")
        for nombre in activos:
            archivo.write(f"- {nombre}\n")
    print("Reporte generado correctamente en 'reporte.txt'.")

def listar_personajes():
    personajes = cargar_json()
    print("\n--- Lista de Personajes Warhammer 40k ---")
    for clave, datos in personajes.items():
        print(f"{clave}: {datos['nombre']} ({datos['faccion']}) - Estado: {datos['estado']}")
    print("------------------------------------------")

def reporte_tabla_completa():
    personajes = cargar_json()
    print("\n{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
        "Clave", "Nombre", "Facción", "Rol", "Arma", "Estado"))
    print("-" * 100)
    for clave, datos in personajes.items():
        print("{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
            clave, datos['nombre'], datos['faccion'], datos['rol'], datos['arma'], datos['estado']))
    print("-" * 100)

def reporte_conteo_faccion():
    personajes = cargar_json()
    conteo = {}
    for p in personajes.values():
        faccion = p["faccion"]
        conteo[faccion] = conteo.get(faccion, 0) + 1
    print("\n--- Conteo de personajes por facción ---")
    for faccion, cantidad in conteo.items():
        print(f"{faccion}: {cantidad}")
    print("----------------------------------------")

def leer_reporte():
    try:
        with open("reporte.txt", "r", encoding="utf-8") as f:
            print("\n=== Contenido de reporte.txt ===")
            print(f.read())
    except FileNotFoundError:
        print("No se encontró 'reporte.txt'. Generá el reporte primero con 'personajes_activos()'.")

#----------------------------------------------------------------------------------------------
# MENÚ PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    while True:
        print("\n---------------------------")
        print("--- MENÚ WARHAMMER 40K ---")
        print("---------------------------")
        print("[1] Crear personaje")
        print("[2] Consultar personaje")
        print("[3] Actualizar personaje")
        print("[4] Eliminar personaje (estado Inactivo)")
        print("[5] Borrar personaje definitivamente")
        print("[6] Listar todos los personajes")
        print("[7] Mostrar personajes activos (genera reporte.txt)")
        print("[8] Reporte tabla completa")
        print("[9] Reporte conteo por facción")
        print("[10] Leer reporte")
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
            for f in facciones_validas:
                print(f"- {f}")
            faccion = input("Facción: ")
            rol = input("Rol: ")
            arma = input("Arma: ")
            estado = input("Estado (Activo/Inactivo): ") or "Activo"
            if estado not in ["Activo", "Inactivo"]:
                print("Error, ingrese 'Activo' o 'Inactivo'")
                estado = input("Estado (Activo/Inactivo): ") or "Activo"
            crear_personaje(clave, nombre, faccion, rol, arma, estado)
        elif opcion == "2":
            leer_personaje(input("Clave del personaje: "))
        elif opcion == "3":
            clave = input("Clave a actualizar: ")
            nombre = input("Nuevo nombre (Enter para omitir): ") or None
            faccion = input("Nueva facción (Enter para omitir): ") or None
            rol = input("Nuevo rol (Enter para omitir): ") or None
            arma = input("Nueva arma (Enter para omitir): ") or None
            estado = input("Nuevo estado (Enter para omitir): ") or None
            actualizar_personaje(clave, nombre, faccion, rol, arma, estado)
        elif opcion == "4":
            eliminar_personaje(input("Clave del personaje: "))
        elif opcion == "5":
            borrar_personaje(input("Clave del personaje: "))
        elif opcion == "6":
            listar_personajes()
        elif opcion == "7":
            personajes_activos()
        elif opcion == "8":
            reporte_tabla_completa()
        elif opcion == "9":
            reporte_conteo_faccion()
        elif opcion == "10":
            leer_reporte()
        else:
            print("⚠️ Opción inválida.")

        input("\nPresione ENTER para continuar...")

#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()