from src.Modelo.ConexionJson import ConexionJSON

class ControlFiltro:
    """
    Clase encargada de gestionar la lectura y escritura de filtros definidos
    por el usuario, como palabras clave o remitentes específicos para análisis
    o clasificación de correos.
    """

    def __init__(self):
        """
        Inicializa la clase creando una instancia de ConexionJSON apuntando
        al archivo donde se guardan los filtros.
        """
        self.conexion_json = ConexionJSON("specs/filtros.json")

    def obtener_filtros(self):
        """
        Lee los filtros almacenados en el archivo JSON y valida que contengan
        la estructura correcta.

        Returns:
            dict: Diccionario con listas de palabras clave y remitentes.

        Raises:
            FileNotFoundError: Si el archivo no se puede leer.
            KeyError: Si no están presentes las claves necesarias.
        """
        datos = self.conexion_json.leer_datos()

        # Validar si la lectura fue exitosa
        if datos is None:
            raise FileNotFoundError("❌ No se pudo leer el archivo de filtros.")

        # Verificar que existan las claves obligatorias
        if datos.get("palabras_clave") is None or datos.get("remitentes") is None:
            raise KeyError("El JSON debe tener las claves 'palabras_clave' y 'remitentes'.")

        return datos
    
    def guardar_filtros(self, palabras_clave, remitentes):
        """
        Guarda los filtros proporcionados en el archivo JSON.

        Args:
            palabras_clave (list): Lista de palabras a filtrar.
            remitentes (list): Lista de correos remitentes a filtrar.
        """
        datos = {
            "palabras_clave": palabras_clave,
            "remitentes": remitentes
        }

        self.conexion_json.escribir_datos(datos)
        print("✅ Filtros guardados correctamente.")
