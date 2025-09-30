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

personajes_40k = {}

def crear_personaje(clave, nombre, faccion, rol, arma, estado="Activo"):
    """
    Crea un nuevo personaje en el diccionario

    Parámetros:
        clave (str): Identificador único del personaje
        nombre (str): Nombre completo del personaje
        faccion (str): Facción del personaje (debe estar en facciones_validas)
        rol (str): Rol del personaje
        arma (str): Arma principal del personaje
        estado (str): Estado del personaje (por defecto "Activo")

    Retorna:
        bool: True si se creó exitosamente, False si ya existe o facción inválida
    """
    # Validar que la clave no exista
    if clave in personajes_40k:
        print(f"Error: El personaje con clave '{clave}' ya existe.")
        return False

    # Validar que la facción sea válida
    if faccion not in facciones_validas:
        print(f"Error: La facción '{faccion}' no es válida.")
        print("Facciones válidas disponibles:")
        for i, f in enumerate(facciones_validas, 1):
            print(f"  {i}. {f}")
        return False

    # Crear el personaje
    personajes_40k[clave] = {
        "nombre": nombre,
        "faccion": faccion,
        "rol": rol,
        "arma": arma,
        "estado": estado
    }

    print(f"Personaje '{nombre}' creado exitosamente con clave '{clave}'.")
    return True

def leer_personaje(clave):
    """
    Lee y muestra la información de un personaje específico

    Parámetros:
        clave (str): Identificador del personaje a consultar

    Retorna:
        dict o None: Diccionario con los datos del personaje o None si no existe
    """
    if clave not in personajes_40k:
        print(f"Error: No se encontró el personaje con clave '{clave}'.")
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
    """
    Actualiza los datos de un personaje existente

    Parámetros:
        clave (str): Identificador del personaje a actualizar
        nombre (str): Nuevo nombre (opcional)
        faccion (str): Nueva facción (opcional)
        rol (str): Nuevo rol (opcional)
        arma (str): Nueva arma (opcional)
        estado (str): Nuevo estado (opcional)

    Retorna:
        bool: True si se actualizó exitosamente, False si no existe
    """
    if clave not in personajes_40k:
        print(f"Error: No se encontró el personaje con clave '{clave}'.")
        return False

    # Validar facción si se está actualizando
    if faccion is not None and faccion not in facciones_validas:
        print(f"Error: La facción '{faccion}' no es válida.")
        print("Facciones válidas disponibles:")
        for i, f in enumerate(facciones_validas, 1):
            print(f"  {i}. {f}")
        return False

    # Actualizar solo los campos que no son None
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
    """
    Elimina un personaje cambiando su estado a 'Inactivo'

    Parámetros:
        clave (str): Identificador del personaje a eliminar

    Retorna:
        bool: True si se eliminó exitosamente, False si no existe
    """
    if clave not in personajes_40k:
        print(f"Error: No se encontró el personaje con clave '{clave}'.")
        return False

    personajes_40k[clave]["estado"] = "Inactivo"
    print(f"Personaje '{clave}' eliminado (estado cambiado a 'Inactivo').")
    return True

def imprimir_personaje_por_clave(clave):
    """
    Imprime la información completa de un personaje por su clave

    Parámetros:
        clave (str): Identificador del personaje a imprimir

    Retorna:
        bool: True si se imprimió exitosamente, False si no existe
    """
    return leer_personaje(clave) is not None


def main():
    # Menu de opciones
    # Ejemplos de uso de las funciones
    # 1 para crear personaje, 2 para leer, 3 para actualizar, 4 para eliminar, 5 para imprimir
    if 1:
        crear_personaje("Guilliman", "Roboute Guilliman", "Ultramarines", "Primarca", "Espada del Emperador", "Vivo")
    if 2:
        leer_personaje("Guilliman")
    if 3:
        actualizar_personaje("Guilliman", estado="Activo")
    if 4:
        eliminar_personaje("Guilliman")
    if 5:
        imprimir_personaje_por_clave("Guilliman")
    
main()