"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Personajes Warhammer 40k
Fecha: 27/10/2025
Autor: 

Descripción:
Gestión de personajes de Warhammer 40k: crear, leer, actualizar, eliminar e imprimir.
Almacena los datos en formato JSON para mantener la persistencia.
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import json
import os
from datetime import datetime

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

ARCHIVO_JSON = "Archivos_administratum.json"

#----------------------------------------------------------------------------------------------
# FUNCIONES AUXILIARES
#----------------------------------------------------------------------------------------------

def guardar_json(diccionario):
    """Guarda el diccionario en el archivo JSON."""
    try:
        with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(diccionario, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
        return False
    return True

def cargar_json():
    """Carga el diccionario desde el JSON si existe."""
    try:
        if os.path.exists(ARCHIVO_JSON):
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            print("Creando nuevo archivo de datos...")
            guardar_json({})  # Crear archivo vacío si no existe
            return {}
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return {}

def sincronizar_archivos(diccionario):
    """Guarda el diccionario en el archivo JSON."""
    guardar_json(diccionario)

def pedir_estado():
    """Solicita el estado del personaje de manera amigable."""
    while True:
        respuesta = input("¿El personaje está activo? (si/no): ").lower()
        if respuesta in ['si', 's', 'sí']:
            return "Activo"
        elif respuesta in ['no', 'n']:
            return "No Activo"
        print("Por favor, responde 'si' o 'no'")

def pedir_faccion():
    """Muestra las facciones como lista numerada y permite seleccionar una."""
    print("\nFacciones disponibles:")
    for i, faccion in enumerate(facciones_validas, 1):
        print(f"[{i}] {faccion}")
    
    while True:
        try:
            seleccion = int(input("\nSelecciona el número de la facción: "))
            if 1 <= seleccion <= len(facciones_validas):
                return facciones_validas[seleccion - 1]
            print(f"Por favor, elige un número entre 1 y {len(facciones_validas)}")
        except ValueError:
            print("Por favor, ingresa un número válido")

#----------------------------------------------------------------------------------------------
# FUNCIONES PRINCIPALES
#----------------------------------------------------------------------------------------------

def guardar_log(mensaje):
    """Guarda un mensaje en el archivo log.txt."""
    with open("log.txt", "a", encoding="utf-8") as f:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{fecha} - {mensaje}\n")

def crear_personaje(clave, nombre, faccion, rol, arma, estado=None):
    personajes = cargar_json()
    if clave in personajes:
        print(f"El personaje con clave '{clave}' ya existe.")
        return
    if faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        return
    
    # Si no se proporcionó estado, pedirlo
    if estado is None:
        estado = pedir_estado()
    
    personajes[clave] = {
        "nombre": nombre,
        "faccion": faccion,
        "rol": rol,
        "arma": arma,
        "estado": estado
    }
    sincronizar_archivos(personajes)
    guardar_log(f"Personaje creado: {nombre}")
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
    
    nombre_actual = personajes[clave]["nombre"]
    if nombre: 
        personajes[clave]["nombre"] = nombre
    if faccion == "seleccionar": 
        faccion = pedir_faccion()
    if faccion and faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        return
    if faccion:
        personajes[clave]["faccion"] = faccion
    if rol:
        personajes[clave]["rol"] = rol
    if arma:
        personajes[clave]["arma"] = arma
    if estado == "seleccionar":
        estado = pedir_estado()
    if estado:
        personajes[clave]["estado"] = estado
    
    sincronizar_archivos(personajes)
    guardar_log(f"Personaje actualizado: {nombre_actual}")
    print(f"Personaje '{clave}' actualizado correctamente.")

def borrar_personaje(clave):
    personajes = cargar_json()
    if clave not in personajes:
        print(f"No se encontró el personaje con clave '{clave}'.")
        return
    nombre = personajes[clave]["nombre"]
    del personajes[clave]
    sincronizar_archivos(personajes)
    guardar_log(f"Personaje borrado: {nombre}")
    print(f"Personaje '{clave}' eliminado definitivamente.")

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
        print("No se encontró el archivo 'reporte.txt'.")

def leer_log():
    """Muestra el contenido del archivo de log."""
    try:
        with open("log.txt", "r", encoding="utf-8") as f:
            print("\n=== Registro de operaciones ===")
            print(f.read())
    except FileNotFoundError:
        print("No hay registros disponibles.")#----------------------------------------------------------------------------------------------
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
        print("[4] Borrar personaje definitivamente")
        print("[5] Listar todos los personajes")
        print("[6] Reporte tabla completa")
        print("[7] Reporte conteo por facción")
        print("[8] Leer reporte")
        print("[9] Ver registro de operaciones")
        print("[0] Salir")
        print("---------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("¡Hasta la próxima batalla!")
            break
        elif opcion == "1":
            clave = input("Clave única del personaje: ")
            nombre = input("Nombre completo: ")
            faccion = pedir_faccion()
            rol = input("Rol: ")
            arma = input("Arma: ")
            crear_personaje(clave, nombre, faccion, rol, arma)
        elif opcion == "2":
            leer_personaje(input("Clave del personaje: "))
        elif opcion == "3":
            clave = input("Clave a actualizar: ")
            nombre = input("Nuevo nombre (Enter para omitir): ") or None
            
            cambiar_faccion = input("¿Deseas cambiar la facción? (si/no): ").lower()
            faccion = "seleccionar" if cambiar_faccion in ['si', 's', 'sí'] else None
            
            rol = input("Nuevo rol (Enter para omitir): ") or None
            arma = input("Nueva arma (Enter para omitir): ") or None
            
            cambiar_estado = input("¿Deseas cambiar el estado? (si/no): ").lower()
            estado = "seleccionar" if cambiar_estado in ['si', 's', 'sí'] else None
            
            actualizar_personaje(clave, nombre, faccion, rol, arma, estado)
        elif opcion == "4":
            borrar_personaje(input("Clave del personaje: "))
        elif opcion == "5":
            listar_personajes()
        elif opcion == "6":
            reporte_tabla_completa()
        elif opcion == "7":
            reporte_conteo_faccion()
        elif opcion == "8":
            leer_reporte()
        elif opcion == "9":
            leer_log()
        else:
            print("⚠️ Opción inválida.")

        input("\nPresione ENTER para continuar...")

#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()