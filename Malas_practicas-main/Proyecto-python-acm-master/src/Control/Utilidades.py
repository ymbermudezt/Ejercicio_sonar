import re

class Utilidades:
    """
    Clase de utilidades que agrupa funciones auxiliares
    utilizadas en diferentes partes de la aplicación.
    Todos los métodos son estáticos porque no requieren
    instancias de la clase.
    """

    @staticmethod
    def validar_email(email: str) -> bool:
        """
        Valida si un correo electrónico cumple con un formato estándar.

        Args:
            email (str): Correo a validar.

        Returns:
            bool: True si el formato es válido, False si no lo es.

        Notas:
            - El patrón revisa que el correo tenga la estructura:
              <usuario>@<dominio>.<extensión>
            - Admite caracteres comunes como:
              letras, números, ".", "_", "+", "-"
        """
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(patron, email) is not None
