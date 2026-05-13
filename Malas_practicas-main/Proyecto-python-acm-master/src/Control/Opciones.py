from enum import Enum

class Opciones(Enum):
    """
    Enumeración que define todas las opciones disponibles en el menú
    principal y submenús de la aplicación.

    Usar Enum permite:
    - Evitar errores por escribir cadenas diferentes.
    - Mantener un listado centralizado y consistente.
    - Asegurar que todas las comparaciones sean exactas.
    """

    # === Gestión de credenciales ===
    CAMBIAR_CREDENCIALES = "CAMBIAR_CREDENCIALES"

    # === Gestión de filtros ===
    MODIFICAR_CRITERIOS = "MODIFICAR_CRITERIOS"
    AGREGAR_PALABRA = "AGREGAR_PALABRA"
    ELIMINAR_PALABRA = "ELIMINAR_PALABRA"
    AGREGAR_REMITENTE = "AGREGAR_REMITENTE"
    ELIMINAR_REMITENTE = "ELIMINAR_REMITENTE"
    ELIMINAR_TODOS_FILTROS = "ELIMINAR_TODOS_FILTROS"

    # === Procesamiento de correos ===
    ELIMINAR_CORREOS = "ELIMINAR_CORREOS"
    MARCAR_COMO_SPAM = "MARCAR_COMO_SPAM"

    # === Navegación ===
    ATRAS = "ATRAS"

    # === Salida del programa ===
    SALIR = "SALIR"
