import imaplib
import email
from email.header import decode_header


class ControlCorreo:
    """
    Clase encargada de conectarse a un servidor de correo mediante IMAP,
    leer mensajes, obtener sus datos y realizar acciones como eliminar o
    mover correos a la carpeta de spam.
    """

    def __init__(self, email_account, password):
        """
        Inicializa los datos necesarios para autenticarse contra Gmail.

        Args:
            email_account (str): Correo del usuario.
            password (str): Contraseña o clave de aplicación.
        """
        self.email_account = email_account
        self.password = password
        self.server = "imap.gmail.com"  # Servidor IMAP de Gmail
        self.mail = None  # Conexión IMAP

    def conectar(self):
        """
        Establece conexión con el servidor IMAP y selecciona el buzón de entrada.

        Raises:
            imaplib.IMAP4.error: En caso de credenciales incorrectas.
        """
        self.mail = imaplib.IMAP4_SSL(self.server)
        self.mail.login(self.email_account, self.password)
        self.mail.select("inbox")  # Selecciona bandeja de entrada

    def leer_todos(self):
        """
        Lee todos los correos del buzón de entrada y retorna una lista con
        la información relevante de cada mensaje.

        Returns:
            list: Lista de diccionarios con ID, remitente, asunto y contenido del mensaje.
        """
        self.conectar()
        status, messages = self.mail.search(None, "ALL")  # IDs de todos los correos
        email_ids = messages[0].split()
        correos = []

        for num in email_ids:
            # Obtiene el correo completo en formato RFC822
            status, msg_data = self.mail.fetch(num, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # ---- Decodificar asunto ----
            subject, encoding = decode_header(msg.get("Subject", ""))[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8", errors="ignore")

            # Obtener remitente
            sender = msg.get("From")

            # Obtenemos la fecha 
            date = msg.get("Date")

            # ---- Obtener cuerpo del mensaje ----
            body = ""
            if msg.is_multipart():  # Mensaje con varias partes
                for part in msg.walk():
                    # Solo texto plano y sin adjuntos
                    if part.get_content_type() == "text/plain" and \
                       "attachment" not in str(part.get("Content-Disposition", "")):

                        body = part.get_payload(decode=True).decode(
                            part.get_content_charset() or "utf-8",
                            errors="ignore"
                        )
                        break
            else:
                # Mensaje simple
                body = msg.get_payload(decode=True).decode(
                    msg.get_content_charset() or "utf-8",
                    errors="ignore"
                )

            correos.append({
                "id": num,
                "remitente": sender,
                "asunto": subject,
                "contenido": body,
                "fecha": date                
            })

        return correos

    def eliminar_correo(self, correo_id):
        """
        Marca un correo para ser eliminado del buzón.

        Args:
            correo_id (bytes): ID del correo a eliminar.
        """
        self.mail.store(correo_id, '+FLAGS', '\\Deleted')

    def marcar_correo(self, correo_id):
        """
        Mueve un correo a la carpeta de spam o junk del correo.

        Args:
            correo_id (bytes): ID del correo a mover.
        """
        # ---- Buscar carpeta de SPAM ----
        result, folders = self.mail.list()
        carpeta_spam = None

        for folder in folders:
            folder_decoded = folder.decode().lower()

            # Gmail usa distintos nombres según idioma y configuración
            if "\\spam" in folder_decoded or "spam" in folder_decoded or "junk" in folder_decoded:
                # Extraer solo el nombre final de la carpeta
                carpeta_spam = folder.decode().split(' "/" ')[-1]
                break

        # Si no se encontró carpeta de spam, evitar error
        if not carpeta_spam:
            raise RuntimeError("⚠️ No se encontró una carpeta de Spam o Junk en el servidor IMAP.")

        # Copiar correo a la carpeta de spam
        self.mail.copy(correo_id, carpeta_spam)

        # Marcar para eliminación en la bandeja original
        self.eliminar_correo(correo_id)

    def cerrar(self):
        """
        Aplica los cambios pendientes (como eliminaciones) y cierra sesión IMAP.
        """
        if self.mail:
            self.mail.expunge()  # Elimina correos marcados como \Deleted
            self.mail.logout()
