import pandas as pd
from pathlib import Path
from datetime import datetime
import csv

class ControlReportes:
    """
    Clase encargada de generar reportes en diferentes formatos (CSV y TXT)
    relacionados con el procesamiento de correos: reporte completo,
    reporte de acciones y un resumen general.
    """

    def __init__(self):
        """
        Crea automáticamente la carpeta donde se almacenarán los reportes.
        'exist_ok=True' evita errores si la carpeta ya existe.
        """
        Path("reportes").mkdir(exist_ok=True)

    # ==========================================================
    # REPORTE COMPLETO
    # ==========================================================
    def generar_reporte_completo(self, correos):
        """
        Genera un archivo CSV con todos los correos revisados.

        Args:
            correos (list): Lista de diccionarios con los datos de cada correo.
        """
        if not correos:
            print("⚠️ No hay correos para generar reporte.")
            return
        
        # Limpiar saltos de línea y comillas en el contenido para no romper el CSV
        correosLimpio = list(map(
            lambda c: {**c, "contenido": c["contenido"].replace("\r\n", "\\n").replace("\r", "\\n").replace("\n", "\\n").replace('"', '\\"')},
            correos
        ))


        # Convertir los datos a DataFrame para fácil exportación
        df = pd.DataFrame(correosLimpio)

        # Nombre único basado en fecha y hora
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ruta = f"reportes/reporte_completo_{fecha}.csv"

        # Exportar CSV
        df.to_csv(ruta, index=False, quoting= csv.QUOTE_ALL, escapechar='\\', encoding="utf-8-sig")
        print(f"📄 Reporte completo generado en: {ruta}")

    # ==========================================================
    # REPORTE DE ACCIONES (ELIMINADOS Y MARCADOS)
    # ==========================================================
    def generar_reporte_acciones(self, eliminados, marcados):
        """
        Genera archivos CSV independientes para:
        - Correos eliminados
        - Correos marcados como spam

        Args:
            eliminados (list): Correos que fueron eliminados.
            marcados (list): Correos marcados como spam.
        """
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # ---- Correos eliminados ----
        if eliminados:
            df_e = pd.DataFrame(eliminados)
            df_e.to_csv(
                f"reportes/correos_eliminados_{fecha}.csv",
                index=False,
                encoding="utf-8"
            )
            print("🗑️ Reporte de eliminados generado.")

        # ---- Correos marcados como spam ----
        if marcados:
            df_m = pd.DataFrame(marcados)
            df_m.to_csv(
                f"reportes/correos_marcados_{fecha}.csv",
                index=False,
                encoding="utf-8"
            )
            print("🚩 Reporte de marcados generado.")

    # ==========================================================
    # RESUMEN GENERAL
    # ==========================================================
    def generar_resumen(self, total, eliminados, marcados):
        """
        Genera un archivo de texto con las estadísticas
        del procesamiento realizado.

        Args:
            total (int): Total de correos revisados.
            eliminados (list): Lista de correos eliminados.
            marcados (list): Lista de correos marcados como spam.
        """
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ruta = f"reportes/resumen_{fecha}.txt"

        # Crear archivo .txt con el resumen
        with open(ruta, "w", encoding="utf-8") as f:
            f.write("📊 RESUMEN DE PROCESAMIENTO DE CORREOS\n\n")
            f.write(f"Total revisados: {total}\n")
            f.write(f"Eliminados: {len(eliminados)}\n")
            f.write(f"Marcados como spam: {len(marcados)}\n")

        print(f"📊 Resumen generado en: {ruta}")
