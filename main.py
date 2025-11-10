"""
-----------------------------------------------------------------------------------------------
Título: Gestor de Personajes Warhammer 40k
Fecha: 9/11/2025
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
    """
    Solicita el estado del personaje de manera amigable.
    Acepta 'si'/'no' y variantes, devolviendo 'Activo' o 'No Activo'.
    """
    while True:
        respuesta = input("¿El personaje está activo? (si/no): ").lower()
        if respuesta in ['si', 's', 'sí']:
            return "Activo"
        elif respuesta in ['no', 'n']:
            return "No Activo"
        print("Por favor, responde 'si' o 'no'")

def pedir_faccion():
    """
    Muestra las facciones disponibles como lista numerada y permite seleccionar una.
    Valida la entrada para asegurar una selección válida.
    """
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
    """
    Crea un nuevo personaje con los atributos especificados.
    Si no se proporciona estado, lo solicita interactivamente.
    Guarda el personaje en el archivo JSON y registra la acción en el log.
    """
    personajes = cargar_json()
    if clave in personajes:
        print(f"El personaje con clave '{clave}' ya existe.")
        return
    if faccion not in facciones_validas:
        print(f"La facción '{faccion}' no es válida.")
        return
    
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
    """
    Muestra en pantalla toda la información de un personaje específico.
    Busca el personaje por su clave en el archivo JSON.
    """
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
    """
    Actualiza los atributos de un personaje existente.
    Solo modifica los campos que se proporcionan, manteniendo el resto sin cambios.
    Para facción y estado, permite selección interactiva si se pasa "seleccionar".
    """
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
    """
    Elimina definitivamente un personaje del sistema.
    Registra la acción en el log antes de eliminar.
    """
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
    """
    Muestra una lista resumida de todos los personajes en el sistema.
    Incluye clave, nombre, facción y estado de cada personaje.
    """
    personajes = cargar_json()
    print("\n--- Lista de Personajes Warhammer 40k ---")
    for clave, datos in personajes.items():
        print(f"{clave}: {datos['nombre']} ({datos['faccion']}) - Estado: {datos['estado']}")
    print("------------------------------------------")

def reporte_tabla_completa():
    """
    Genera un reporte detallado de todos los personajes en formato de tabla.
    Muestra todos los atributos de cada personaje de manera ordenada.
    """
    personajes = cargar_json()
    print("\n{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
        "Clave", "Nombre", "Facción", "Rol", "Arma", "Estado"))
    print("-" * 100)
    for clave, datos in personajes.items():
        print("{:<12} {:<25} {:<18} {:<15} {:<20} {:<10}".format(
            clave, datos['nombre'], datos['faccion'], datos['rol'], datos['arma'], datos['estado']))
    print("-" * 100)

def reporte_conteo_faccion():
    """
    Genera un reporte estadístico que muestra la cantidad de personajes por facción.
    Útil para ver la distribución de personajes entre las diferentes facciones.
    """
    personajes = cargar_json()
    conteo = {}
    for p in personajes.values():
        faccion = p["faccion"]
        conteo[faccion] = conteo.get(faccion, 0) + 1
    print("\n--- Conteo de personajes por facción ---")
    for faccion, cantidad in conteo.items():
        print(f"{faccion}: {cantidad}")
    print("----------------------------------------")

def leer_log():
    """
    Muestra el historial completo de operaciones realizadas en el sistema.
    Lee y muestra el contenido del archivo log.txt que registra todas las acciones.
    """
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
        print("[8] Ver registro de operaciones")
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
            leer_log()
        else:
            print("⚠️ Opción inválida.")

        input("\nPresione ENTER para continuar...")

#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()