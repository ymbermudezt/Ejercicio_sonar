from src.Control.ControlConexion import ControlConexion
from src.Control.ControlCorreo import ControlCorreo
from src.Vista.Menu import Menu
from src.Control.ControlFiltro import ControlFiltro
from src.Control.Opciones import Opciones
from src.Control.Utilidades import Utilidades
from email.utils import parseaddr
from src.Control.ControlReportes import ControlReportes


class ControlPrincipal:
    """
    Clase controladora principal de toda la aplicación.
    Coordina el menú, la gestión de credenciales, filtros,
    lectura y procesamiento de correos, y generación de reportes.
    """

    def __init__(self):
        """
        Inicializa todos los módulos necesarios del sistema:
        - Conexión y credenciales
        - Filtros del usuario
        - Reportes
        - Menú interactivo
        Luego inicia el ciclo principal.
        """
        self.control_conexion = ControlConexion()
        self.control_filtro = ControlFiltro()
        self.control_reportes = ControlReportes()
        self.menu = Menu()
        self.ejecutar()  # Ciclo principal

    # ==========================================================
    # CICLO PRINCIPAL DEL PROGRAMA
    # ==========================================================
    def ejecutar(self):
        """Bucle principal del menú. Ejecuta acciones según opción seleccionada."""
        while True:
            opcion = self.menu.mostrar_menu()
            
            if opcion == Opciones.CAMBIAR_CREDENCIALES:
                self.cambiar_credenciales()

            elif opcion == Opciones.MODIFICAR_CRITERIOS:                
                self.menu.ir_a_filtros()

            elif opcion == Opciones.AGREGAR_PALABRA:
                self.agregar_palabra()

            elif opcion == Opciones.ELIMINAR_PALABRA:                
                self.eliminar_palabra()

            elif opcion == Opciones.AGREGAR_REMITENTE:
                self.agregar_remitente()

            elif opcion == Opciones.ELIMINAR_REMITENTE:
                self.eliminar_remitente()

            elif opcion == Opciones.ELIMINAR_TODOS_FILTROS:
                self.eliminar_todos_filtros()

            elif opcion == Opciones.ELIMINAR_CORREOS:        
                self.eliminar_correos_spam()                    

            elif opcion == Opciones.MARCAR_COMO_SPAM:
                self.marcar_como_spam_correos()             

            elif opcion == Opciones.ATRAS: 
                self.menu.ir_atras()        

            elif opcion == Opciones.SALIR: 
                print("Saliendo de la aplicación")
                break            

            else:
                print("Opción no válida. Intente de nuevo") 


    # ==========================================================
    # GESTIÓN DE REMITENTES
    # ==========================================================
    def agregar_remitente(self):
        """Agrega un remitente a la lista de filtros."""
        try:
            remitente = input("Ingrese el remitente a agregar a los filtros: ").lower()

            if remitente.strip() == "":
                print("El remitente no puede estar vacío.")
                return

            if not Utilidades.validar_email(remitente):
                print("Formato de correo no válido")
                return

            filtros = self.control_filtro.obtener_filtros()

            # Evitar duplicados
            if remitente not in filtros["remitentes"]:
                filtros["remitentes"].append(remitente)
                self.control_filtro.guardar_filtros(
                    filtros["palabras_clave"],
                    filtros["remitentes"]
                )

            print("Remitentes actuales en los filtros:", filtros["remitentes"])
        except Exception as e:
            print("Error al agregar remitente:", e)

    def eliminar_remitente(self):
        """Elimina un remitente registrado en los filtros."""
        try:
            remitente = input("Ingrese el remitente a eliminar de los filtros: ")
            filtros = self.control_filtro.obtener_filtros()

            if remitente in filtros["remitentes"]:
                filtros["remitentes"].remove(remitente)
                self.control_filtro.guardar_filtros(
                    filtros["palabras_clave"],
                    filtros["remitentes"]
                )
                print("Remitente eliminado.")
            else:
                print("El remitente no está en los filtros.")
        except Exception as e:
            print("Error al eliminar remitente:", e)


    # ==========================================================
    # GESTIÓN DE FILTROS - PALABRAS CLAVE
    # ==========================================================
    def eliminar_todos_filtros(self):
        """Elimina todos los filtros de forma definitiva."""
        try:
            if self.menu.continuar("¿Está seguro de que desea eliminar todos los filtros?"):
                self.control_filtro.guardar_filtros([], [])
                print("Todos los filtros han sido eliminados.")
        except Exception as e:
            print("Error al eliminar todos los filtros:", e)

    def eliminar_correos_spam(self):
        """Inicia el proceso de eliminación de correos según filtros del usuario."""
        try:
            filtros = self.control_filtro.obtener_filtros()
            print("Filtros actuales:", filtros["palabras_clave"], filtros["remitentes"])

            if self.menu.continuar("¿Desea continuar?"):
                self.eliminar_correos()

        except Exception as e:
            print("Error al iniciar eliminación de correos:", e)

    def marcar_como_spam_correos(self):
        """Inicia el proceso de marcado de correos como spam."""
        try:
            filtros = self.control_filtro.obtener_filtros()
            print("Filtros actuales:", filtros["palabras_clave"], filtros["remitentes"])

            if self.menu.continuar("¿Desea continuar?"):
                self.marcar_correos()

        except Exception as e:
            print("Error al iniciar marcado de correos:", e)


    # ==========================================================
    # NAVEGACIÓN Y MENÚ
    # ==========================================================
    def ir_atras(self):
        """Regresa al menú anterior."""
        try:
            self.menu.ir_atras()
        except Exception as e:
            print("Error al navegar atrás:", e)


    # ==========================================================
    # AGREGAR / ELIMINAR PALABRAS CLAVE EN FILTROS
    # ==========================================================
    def agregar_palabra(self):
        """Agrega una palabra clave a los filtros."""
        try:
            palabra = input("Ingrese la palabra/frase a agregar a los filtros: ")
            filtros = {"palabras_clave": [], "remitentes": []}

            # Intentar cargar filtros existentes
            try:
                filtros = self.control_filtro.obtener_filtros()
            except Exception:
                pass
            
            if palabra.strip() == "":
                print("La palabra/frase no puede estar vacía.")
                return

            if palabra not in filtros["palabras_clave"]:
                filtros["palabras_clave"].append(palabra)

            self.control_filtro.guardar_filtros(
                filtros["palabras_clave"],
                filtros["remitentes"]
            )
            print("Palabras actuales en los filtros:", filtros["palabras_clave"])

        except Exception as e:
            print("Error al agregar la palabra/frase:", e)

    def eliminar_palabra(self):
        """Elimina una palabra clave de los filtros."""
        try:
            filtros = {"palabras_clave": [], "remitentes": []}
            
            try:
                filtros = self.control_filtro.obtener_filtros()
            except Exception:
                pass        

            print("Palabras/frases actuales en los filtros:", filtros["palabras_clave"])                    

            palabra = input("Ingrese la palabra/frase a eliminar de los filtros: ")

            if palabra in filtros["palabras_clave"]:
                filtros["palabras_clave"].remove(palabra)
                self.control_filtro.guardar_filtros(
                    filtros["palabras_clave"],
                    filtros["remitentes"]
                )
            else:
                print("La palabra/frase no está en los filtros.")

        except Exception as e:
            print("Error al eliminar la palabra/frase:", e)


    # ==========================================================
    # CREDENCIALES
    # ==========================================================
    def cambiar_credenciales(self):
        """
        Permite al usuario cambiar correo y/o contraseña.
        Admite conservar el correo escribiendo 'n'.
        """
        while True:
            try:
                print("\nEscriba ':q' para cancelar")

                existe_usuario = True
                actual_email = ""                

                # Intentar cargar credenciales actuales
                try:
                    actual_email, _ = self.control_conexion.obtener_credenciales()            
                except Exception:
                    existe_usuario = False

                # Pedir nuevo correo / contraseña
                if existe_usuario:            
                    email_account = input("Ingrese el nuevo correo electrónico (n para cambiar solo contraseña): ")
                    if email_account.strip() == ":q":
                        break

                    # Validar formato si se ingresa uno nuevo
                    if email_account.strip() != "n" and not Utilidades.validar_email(email_account.strip()):
                        print("Formato de correo no valido")
                        continue

                    password = input("Ingrese la nueva contraseña: ")
                    if password.strip() == ":q":
                        break    

                else:
                    email_account = input("Ingrese el nuevo correo electrónico: ")
                    if email_account.strip() == ":q":
                        break

                    if not Utilidades.validar_email(email_account.strip()):
                        print("Formato de correo no valido")
                        continue

                    password = input("Ingrese la nueva contraseña: ")
                    if password.strip() == ":q":
                        break    

                # Validar vacío
                if email_account == "" or password == "":
                    print("El correo y la contraseña no pueden estar vacíos.")
                    continue

                # Si escribió "n", conservar correo actual
                if email_account.strip() == "n" and existe_usuario:
                    email_account = actual_email

                # Guardar credenciales
                self.control_conexion.guardar_credenciales(email_account, password)            
                print("Credenciales actualizadas correctamente.")    
                break                        

            except Exception as e:
                print("Error al guardar las credenciales:", e)
                break


    # ==========================================================
    # PROCESAMIENTO DE CORREOS
    # ==========================================================
    def eliminar_correos(self):
        """Procesa correos ejecutando la opción de ELIMINAR."""
        try:
            email_account, password = self.control_conexion.obtener_credenciales()
            self.procesar_correos(email_account, password)

        except (FileNotFoundError, KeyError, ValueError) as err_cred:
            print("Credenciales no existen o son inválidas (créelas desde el menú):", err_cred)

        except Exception as e:
            print("Error al borrar correo:", e)

    def marcar_correos(self):
        """Procesa correos ejecutando la opción de MARCAR como SPAM."""
        try:
            email_account, password = self.control_conexion.obtener_credenciales()
            self.procesar_correos(email_account, password, "marcar")

        except (FileNotFoundError, KeyError, ValueError) as err_cred:
            print("Credenciales no existen o son inválidas (créelas desde el menú):", err_cred)

        except Exception as e:
            print("Error al marcar correos:", e)


    # ==========================================================
    # NÚCLEO DEL PROCESAMIENTO DE CORREOS
    # ==========================================================
    def procesar_correos(self, email_account, password, opcion="eliminar"):
        """
        Procesa todos los correos y aplica filtros según la acción:
        - eliminar: elimina correos con palabras clave o remitentes filtrados
        - marcar: mueve a carpeta SPAM los correos sospechosos

        Args:
            email_account (str): Cuenta de correo
            password (str): Contraseña o clave de aplicación
            opcion (str): "eliminar" o "marcar"
        """
        print("📬 Leyendo correos...")

        correo_control = ControlCorreo(email_account, password)
        correos = correo_control.leer_todos()
        filtros = self.control_filtro.obtener_filtros()

        eliminados = []
        marcados = []

        for c in correos:
            asunto = c["asunto"].lower()
            nombre, remitente = parseaddr(c["remitente"].lower())

            # ---- ELIMINAR ----
            if opcion == "eliminar":
                if asunto in filtros["palabras_clave"] or remitente in filtros["remitentes"]:
                    correo_control.eliminar_correo(c["id"])
                    eliminados.append(c)
                    print(f"🗑️ Eliminado: {c['asunto']}")
                else:
                    print(f"✔️ Válido: {c['asunto']}")

            # ---- MARCAR SPAM ----
            elif opcion == "marcar":
                if "spam" in asunto or "promocion" in asunto:
                    correo_control.marcar_correo(c["id"])
                    marcados.append(c)
                    print(f"🚩 Marcado como spam: {c['asunto']}")
                else:
                    print(f"✔️ Válido: {c['asunto']}")

        correo_control.cerrar()
        # ---- GENERAR REPORTES ----
        self.control_reportes.generar_reporte_completo(correos)
        self.control_reportes.generar_reporte_acciones(eliminados, marcados)
        self.control_reportes.generar_resumen(
            total=len(correos),
            eliminados=eliminados,
            marcados=marcados
        )

        print("\n🔹 Proceso finalizado.")
