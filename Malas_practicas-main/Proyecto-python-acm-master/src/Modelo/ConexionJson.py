import json
from pathlib import Path


class ConexionJSON:
    """
    Clase encargada de manejar la lectura y escritura de archivos JSON.
    Se usa como capa de acceso a datos para credenciales, filtros u otros
    archivos utilizados por la aplicación.
    """

    def __init__(self, ruta):
        """
        Inicializa la clase con la ruta del archivo JSON.

        Args:
            ruta (str | Path): Ruta del archivo que se gestionará.
        """
        self.ruta = Path(ruta)

    # ==========================================================
    # LECTURA
    # ==========================================================
    def leer_datos(self):
        """
        Lee y devuelve el contenido del archivo JSON.

        Returns:
            dict | None: Datos del JSON si existe y es válido,
            o None si el archivo no existe o hay error al leerlo.
        """
        if not self.ruta.exists():
            return None

        try:
            with self.ruta.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            # Si el JSON está corrupto, vacío o inaccesible
            return None
                
    # ==========================================================
    # ESCRITURA
    # ==========================================================
    def escribir_datos(self, datos):
        """
        Escribe datos en el archivo JSON.

        Args:
            datos (dict): Diccionario a guardar en el archivo.

        Nota:
            - Se usa indent=4 para hacer el archivo legible.
            - Cualquier error se captura y se informa.
        """
        try:
            with self.ruta.open("w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error al escribir en el archivo JSON: {e}")

    # ==========================================================
    # UTILIDADES
    # ==========================================================
    def cambiar_ruta(self, nueva_ruta):
        """
        Cambia dinámicamente la ruta del archivo JSON.

        Args:
            nueva_ruta (str | Path): Nueva ubicación del archivo.
        """
        self.ruta = Path(nueva_ruta)

    def existe_archivo(self):
        """
        Verifica si el archivo JSON existe en la ruta actual.

        Returns:
            bool: True si existe, False si no.
        """
        return self.ruta.exists()
