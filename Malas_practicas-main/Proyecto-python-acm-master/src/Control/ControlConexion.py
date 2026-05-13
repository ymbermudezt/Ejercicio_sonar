from src.Modelo.ConexionJson import ConexionJSON


class ControlConexion:
    """
    Clase encargada de gestionar la lectura y escritura de credenciales
    almacenadas en un archivo JSON. Utiliza la clase ConexionJSON para
    interactuar con el archivo.
    """

    def __init__(self):
        """
        Inicializa la clase creando una instancia de ConexionJSON apuntando
        al archivo donde se guardan las credenciales.
        """
        self.conexion_json = ConexionJSON("specs/credentials.json")

    def obtener_credenciales(self):
        """
        Lee las credenciales almacenadas en el archivo JSON y valida que
        contengan la estructura correcta.

        Returns:
            tuple: (email, password)

        Raises:
            FileNotFoundError: Si el archivo no se puede leer.
            KeyError: Si las claves esperadas no existen en el JSON.
            ValueError: Si los valores están vacíos o incompletos.
        """
        datos = self.conexion_json.leer_datos()

        # Verifica si la lectura fue exitosa
        if datos is None:
            raise FileNotFoundError("❌ No se pudo leer el archivo de credenciales.")

        # Verifica que existan las claves necesarias
        if "email" not in datos or "password" not in datos:
            raise KeyError("⚠️ El JSON debe tener las claves 'email' y 'password'.")

        correo = datos["email"]
        contrasena = datos["password"]

        # Valida que los valores no estén vacíos
        if not correo or not contrasena:
            raise ValueError("⚠️ Las credenciales están vacías o incompletas.")

        print("✅ Credenciales cargadas correctamente.")
        return correo, contrasena
    
    def guardar_credenciales(self, email, password):
        """
        Guarda las credenciales proporcionadas en el archivo JSON.

        Args:
            email (str): Correo a guardar.
            password (str): Contraseña a guardar.
        """
        datos = {
            "email": email,
            "password": password
        }

        # Llama al método de la otra clase para escribir el JSON
        self.conexion_json.escribir_datos(datos)
