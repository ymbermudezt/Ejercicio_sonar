from src.Control.ControlPrincipal import ControlPrincipal


class Launcher:
    """
    Clase lanzadora del programa.
    Actualmente no contiene lógica, pero sirve como punto de entrada
    conceptual para iniciar la aplicación desde un único archivo.
    """
    pass


# Punto de entrada real del programa
if __name__ == "__main__":
    """
    Este bloque se ejecuta únicamente cuando este archivo se ejecuta directamente
    (no cuando se importa desde otro archivo). Inicia la aplicación llamando
    a ControlPrincipal.
    """
    ControlPrincipal()
