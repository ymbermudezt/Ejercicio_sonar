from src.Control.Opciones import Opciones as opciones


class Menu:
    """
    Clase que representa el sistema de menús de la aplicación.
    Maneja tanto el menú principal como el submenú de filtros,
    además del historial de navegación entre ellos.
    """

    def __init__(self):        
        """
        Inicializa el menú con un historial de navegación.
        El historial permite volver atrás cuando sea necesario.
        """
        self.menu_history = ["principal"]  # Menú actual

    # ==========================================================
    # NAVEGACIÓN ENTRE MENÚS
    # ==========================================================
    def ir_a_filtros(self):
        """Cambia el estado al menú de filtros."""
        self.menu_history.append("filtros")

    def ir_atras(self):
        """
        Regresa al menú anterior eliminando el último estado.
        No hace nada si ya está en el menú principal.
        """
        if len(self.menu_history) > 1:
            self.menu_history.pop()

    # ==========================================================
    # SELECCIÓN AUTOMÁTICA DE MENÚ
    # ==========================================================
    def mostrar_menu(self):
        """
        Decide qué menú mostrar dependiendo del historial.
        """
        if self.menu_history[-1] == "principal":
            return self.mostrar_principal()
        elif self.menu_history[-1] == "filtros":
            return self.mostrar_filtros()

    # ==========================================================
    # MENÚ PRINCIPAL
    # ==========================================================
    def mostrar_principal(self):        
        """
        Muestra el menú principal y devuelve la opción
        seleccionada como un valor del Enum Opciones.
        """
        print("\n=== Menú Principal ===")
        print("1. Cambiar usuario y contraseña")
        print("2. Modificar criterios de filtrado")
        print("3. Eliminar correos")
        print("4. Marcar correos como Spam")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        # Convertir número ingresado en una opción del Enum
        if opcion == "1":
            opcion = opciones.CAMBIAR_CREDENCIALES
        elif opcion == "2":
            opcion = opciones.MODIFICAR_CRITERIOS
        elif opcion == "3":
            opcion = opciones.ELIMINAR_CORREOS
        elif opcion == "4":
            opcion = opciones.MARCAR_COMO_SPAM
        elif opcion == "0":
            opcion = opciones.SALIR

        return opcion

    # ==========================================================
    # MENÚ DE FILTROS
    # ==========================================================
    def mostrar_filtros(self):        
        """
        Muestra el menú de filtros y devuelve la opción seleccionada.
        """
        print("\n=== Menú Filtros ===")
        print("1. Agregar palabra/frase a los filtros")
        print("2. Quitar palabra/frase de los filtros")
        print("3. Agregar remitente a los filtros")
        print("4. Eliminar remitente de los filtros")
        print("5. Eliminar todos los filtros")
        print("0. Atrás")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion = opciones.AGREGAR_PALABRA
        elif opcion == "2":
            opcion = opciones.ELIMINAR_PALABRA
        elif opcion == "3":
            opcion = opciones.AGREGAR_REMITENTE
        elif opcion == "4":
            opcion = opciones.ELIMINAR_REMITENTE
        elif opcion == "5":
            opcion = opciones.ELIMINAR_TODOS_FILTROS
        elif opcion == "0":
            opcion = opciones.ATRAS

        return opcion

    # ==========================================================
    # CONFIRMACIÓN DE ACCIONES
    # ==========================================================
    def continuar(self, mensaje):
        """
        Solicita confirmación al usuario para acciones sensibles.

        Args:
            mensaje (str): Texto a mostrar al usuario.

        Returns:
            bool: True si confirma con 's', False en caso contrario.
        """
        respuesta = input(f"{mensaje} (s/n): ").lower()
        return respuesta == 's'
