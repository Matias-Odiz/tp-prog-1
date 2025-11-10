# Gestor de Personajes Warhammer 40k
# Limk de la presentacion *https://docs.google.com/presentation/d/1WIEKsKsW7HC42dLxqBOLx-lMi9O3IE5BDvIep7WwY9k/edit?usp=sharing*

## Descripción
Sistema de gestión de personajes ambientado en el universo de Warhammer 40,000. Este proyecto permite mantener un registro detallado de personajes, incluyendo su afiliación a diferentes facciones, roles de combate y equipamiento.

Fecha de última actualización: 10/11/2025

## Características Principales

### Gestión de Personajes (CRUD)
- ✨ **Crear** nuevos personajes con información completa
- 🔍 **Consultar** detalles de personajes existentes
- 📝 **Actualizar** información de personajes
- ❌ **Borrar** personajes del sistema
- 📋 **Listar** todos los personajes registrados
- 📊 **Reportes** detallados y estadísticos
- 📜 **Registro** de todas las operaciones

### Datos Almacenados por Personaje
- Clave única
- Nombre completo
- Facción (de una lista predefinida)
- Rol
- Arma
- Estado (Activo/No Activo)

## Requisitos Técnicos
- Python 3.x
- Módulos utilizados (todos estándar):
  - json: Para almacenamiento persistente
  - os: Para operaciones de archivo
  - datetime: Para registro de timestamps
  - re: Para validación de nombres

## Estructura del Proyecto
```
tp-prog-1/
├── main.py               # Programa principal
├── Archivos_administratum.json  # Base de datos
├── log.txt              # Registro de operaciones
└── README.md            # Documentación
```

## Funcionalidades Detalladas

### Sistema de Menú
1. Crear personaje
2. Consultar personaje
3. Actualizar personaje
4. Borrar personaje definitivamente
5. Listar todos los personajes
6. Reporte tabla completa
7. Reporte conteo por facción
8. Ver registro de operaciones
0. Salir

### Validaciones Implementadas
- Nombres: Solo letras y espacios (incluye caracteres especiales españoles)
- Facciones: Lista predefinida de 31 facciones válidas
- Estado: Sistema simplificado de entrada (si/no)
- Claves: Verificación de duplicados

### Reportes Disponibles
1. **Lista Resumida**: Muestra clave, nombre, facción y estado
2. **Tabla Completa**: Presenta todos los datos en formato tabular
3. **Conteo por Facción**: Estadísticas de personajes por facción
4. **Registro de Operaciones**: Historial completo con timestamps

## Facciones Disponibles
El sistema incluye 31 facciones canónicas del universo Warhammer 40k:

### Space Marines
- Ultramarines
- Imperial Fists
- Blood Angels
- Dark Angels
- Space Wolves
- Iron Hands
- Salamanders
- Raven Guard
- White Scars

### Chaos
- Black Legion
- Death Guard
- Thousand Sons
- World Eaters
- Emperor's Children
- Chaos Space Marines
- Daemons

### Xenos
- Aeldari
- Orkos
- Necrones
- Tau Empire
- Tyranids
- Drukhari
- Craftworld Eldar
- Harlequins
- Ynnari

### Imperium
- Imperial Guard
- Adeptus Mechanicus
- Sisters of Battle
- Grey Knights
- Deathwatch
- Custodes

## Implementación Técnica

### Persistencia de Datos
- Formato JSON para almacenamiento
- Manejo de errores robusto
- Registro de operaciones con timestamps
- Backup implícito en cada operación

### Características de Código
- Funciones modulares y reutilizables
- Documentación inline detallada
- Manejo de errores con try-except
- Uso de list comprehension para reportes
- Funciones lambda para conteo de facciones

## Autores
- Venice Vito
- Alice Augusto
- Matias Odiz
- Anzuinelli Ignacio

## Uso del Sistema
1. Ejecutar el programa:
```bash
python main.py
```
2. Seleccionar la opción deseada del menú
3. Seguir las instrucciones en pantalla
4. Las operaciones se registran automáticamente en `log.txt`
5. Los datos se guardan automáticamente en `Archivos_administratum.json`
