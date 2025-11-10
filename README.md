# Gestor de Personajes Warhammer 40k

## Introducción
Este proyecto es un sistema de gestión de personajes ambientado en el universo de Warhammer 40,000, un popular juego de mesa y universo de ciencia ficción. El sistema permite a los usuarios mantener un registro detallado de sus personajes, incluyendo su afiliación a diferentes facciones, roles de combate y equipamiento.

El proyecto está diseñado para ser una herramienta útil tanto para jugadores como para narradores, facilitando el seguimiento y la gestión de múltiples personajes en sus campañas y partidas.

## Descripción Técnica
El sistema está implementado en Python y utiliza un enfoque modular con las siguientes características técnicas:

### Estructura de Datos
- Almacenamiento persistente en formato JSON
- Registro de operaciones con timestamps
- Validación de datos en tiempo real
- Sistema de reportes flexible

### Manejo de Personajes
- Sistema CRUD completo (Crear, Leer, Actualizar, Borrar)
- Validación de facciones contra una lista predefinida
- Estados de personaje (Activo/No Activo)
- Sistema de claves únicas para identificación

### Interfaz de Usuario
- Menú interactivo en consola
- Selección numérica de facciones
- Confirmaciones de estado simplificadas (si/no)
- Feedback inmediato de operaciones

## Características y Funcionalidades
- Crear nuevos personajes con nombre, facción, rol y armas
- Consultar información detallada de personajes existentes
- Actualizar datos de personajes
- Borrar personajes del sistema
- Generar reportes y estadísticas
- Sistema de logs para seguimiento de cambios
- Interfaz de menú interactiva

## Requisitos
- Python 3.x
- No requiere bibliotecas adicionales (usa módulos estándar)

## Uso
1. Ejecutar el programa:
```bash
python main.py
```

2. Menú principal:
- [1] Crear personaje
- [2] Consultar personaje
- [3] Actualizar personaje
- [4] Borrar personaje definitivamente
- [5] Listar todos los personajes
- [6] Reporte tabla completa
- [7] Reporte conteo por facción
- [8] Ver registro de operaciones
- [0] Salir

## Estructura del Código

### Módulo Principal (sprint1_uade.py)
El código está organizado en varias secciones principales:

1. **Funciones de Gestión de Datos**
   - `guardar_json()`: Persistencia de datos en archivo JSON
   - `cargar_json()`: Carga de datos desde archivo JSON
   - `sincronizar_archivos()`: Asegura la consistencia de datos

2. **Funciones de Interacción con Usuario**
   - `pedir_estado()`: Interfaz simplificada para estado de personaje
   - `pedir_faccion()`: Selector numérico de facciones
   - `guardar_log()`: Registro de operaciones con timestamp

3. **Funciones CRUD de Personajes**
   - `crear_personaje()`: Alta de nuevos personajes
   - `leer_personaje()`: Consulta de personajes individuales
   - `actualizar_personaje()`: Modificación de atributos
   - `borrar_personaje()`: Eliminación definitiva

4. **Funciones de Reporte**
   - `listar_personajes()`: Vista resumida de todos los personajes
   - `reporte_tabla_completa()`: Informe detallado en formato tabla
   - `reporte_conteo_faccion()`: Estadísticas por facción
   - `leer_log()`: Historial de operaciones

### Archivos del Sistema
- `main.py`: Programa principal con toda la lógica
- `Archivos_administratum.json`: Base de datos en formato JSON
- `log.txt`: Registro cronológico de operaciones

## Facciones Disponibles
- Ultramarines
- Black Legion
- Aeldari
- Orkos
- Necrones
- Imperial Fists
- Blood Angels
- Dark Angels
- Space Wolves
- Iron Hands
- Y muchas más...

## Características Técnicas Adicionales

### Manejo de Errores
- Validación de entradas de usuario
- Manejo de archivos con try-except
- Mensajes de error descriptivos
- Prevención de duplicados de claves

### Persistencia de Datos
- Guardado automático tras cada operación
- Formato JSON para fácil lectura y edición
- Logs con timestamp para auditoría
- Respaldo implícito en cada operación

### Extensibilidad
- Diseño modular para fácil expansión
- Constantes definidas para configuración
- Funciones auxiliares reutilizables
- Estructura clara y documentada

## Autor
Grupo integrado por: Venice Vito, Alice Augusto, Matias Odiz y Anzuinelli Ignacio

## Notas de Implementación
- El sistema utiliza Python 3.x por su simplicidad y potencia
- No requiere bibliotecas externas, solo módulos estándar
- Diseñado para ser robusto y fácil de mantener
- Documentación integrada en el código
