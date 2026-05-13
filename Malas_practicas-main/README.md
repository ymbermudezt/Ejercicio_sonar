# Malas_practicas

Integrantes

- Yhoan Mauricio Bermudez Tique (20242020242)

- Sebastian David Trujillo Vargas (20242020217)

- David Felipe Batanero Molina (20241020092)

# Patrones de Diseño y Mejoras para el Proyecto "Bot de Correo Spam"

## Patrones de Diseño Utilizados

El proyecto implementa varios patrones de diseño comunes en aplicaciones Python, organizados en una arquitectura modular:

### 1. **Modelo-Vista-Controlador (MVC)**
- **Modelo**: `ConexionJSON` maneja el acceso a datos (JSON para credenciales y filtros).
- **Vista**: `Menu` gestiona la interfaz de usuario por consola.
- **Controlador**: Clases como `ControlPrincipal`, `ControlCorreo`, `ControlFiltro` coordinan la lógica de negocio.

### 2. **Fachada (Facade)**
- `ControlPrincipal` actúa como fachada, simplificando el acceso a módulos complejos (conexión, filtros, reportes).

### 3. **Estrategia (Strategy)**
- En `procesar_correos`, se selecciona dinámicamente la acción ("eliminar" o "marcar") basada en parámetros.

### 4. **Método de Plantilla (Template Method)**
- `leer_todos` en `ControlCorreo` define un flujo fijo para procesar correos, con variaciones en el manejo de partes MIME.

### 5. **Enumeración (Enum)**
- `Opciones` centraliza las opciones del menú, evitando errores por cadenas literales.

### 6. **Comando (Command)**
- Las opciones del menú encapsulan acciones específicas, ejecutadas en `ControlPrincipal.ejecutar`.

### 7. **Singleton Implícito**
- Instancias únicas de controladores en `ControlPrincipal`, aunque no estrictamente enforced.

---

# Alternativas a Patrones de Diseño en el Proyecto

## Patrones que Podrían Reemplazarse o Mejorarse

### 1. **Singleton Implícito (en Controladores)**
- **Por qué no necesario**: No hay estado global compartido crítico; las instancias se crean una vez en `ControlPrincipal`. Puede llevar a acoplamiento.
- **Alternativa**: Usar **Factory Pattern** para crear instancias de controladores dinámicamente, o inyección de dependencias para pasar objetos. Esto facilita pruebas y flexibilidad.

### 2. **Comando (en Opciones del Menú)**
- **Podría mejorarse**: Es útil, pero la lógica condicional en `ejecutar` es extensa. 
- **Alternativa**: **Strategy Pattern** más puro, con clases concretas para cada acción (e.g., `EliminarCorreosStrategy`), eliminando el `if-elif` largo.

### 3. **Método de Plantilla (en leer_todos)**
- **Podría reemplazarse**: Es adecuado, pero si el procesamiento varía mucho, 
- **Alternativa**: **Chain of Responsibility** para procesar partes MIME en secuencia, delegando a handlers específicos.

---

## Patrones Innecesarios o Sobredimensionados

### 1. **Fachada (ControlPrincipal)**
- **No siempre necesario**: Simplifica, pero en un proyecto pequeño, podría fusionarse con el controlador principal sin pérdida de claridad. Es útil aquí, pero no esencial.

### 2. **Enumeración (Opciones)**
- **Es beneficioso**: Evita errores, pero en proyectos muy simples, constantes de cadena bastarían. Aquí es apropiado y recomendado mantenerlo.

### 3. **MVC Completo**
- **Podría simplificarse**: Para una app de consola pequeña, un enfoque funcional o procedural sería suficiente, evitando clases separadas. MVC es overkill si no hay vistas complejas.

---

## Alternativas Generales Sugeridas

- **Observer Pattern**: Para notificar cambios en filtros o credenciales a otros módulos, en lugar de llamadas directas.
- **Builder Pattern**: Para construir objetos complejos como reportes o conexiones IMAP con configuraciones opcionales.
- **Adapter Pattern**: Si se agrega soporte para otros protocolos (e.g., POP3), adaptar interfaces existentes.

En general, los patrones usados son apropiados para la escala del proyecto, pero para mayor mantenibilidad, priorizar inyección de dependencias y reducir acoplamiento. Evitar patrones innecesarios mantiene el código simple.

---

## Mejoras al Código

### 1. **Manejo de Errores y Excepciones**
- Agregar excepciones personalizadas (e.g., `CredencialesInvalidasError`).
- Usar `logging` en lugar de `print` para errores y depuración.
- Validar conexiones IMAP con reintentos automáticos.

### 2. **Seguridad**
- Enmascarar contraseñas en entrada/salida.
- Usar variables de entorno o un gestor de secretos para credenciales (e.g., `python-dotenv`).
- Evitar almacenar contraseñas en texto plano; considerar encriptación básica.

### 3. **Rendimiento y Eficiencia**
- Leer correos en lotes o con paginación para evitar cargar todos los mensajes en memoria.
- Usar expresiones regulares compiladas para filtros de palabras clave.
- Paralelizar procesamiento de correos con `concurrent.futures` si es necesario.

### 4. **Calidad del Código**
- Agregar type hints completos (e.g., `def leer_datos(self) -> dict | None`).
- Implementar pruebas unitarias con `unittest` o `pytest` para clases críticas.
- Refactorizar métodos largos (e.g., `procesar_correos`) en funciones auxiliares.

### 5. **Arquitectura y Mantenibilidad**
- Inyección de dependencias: Pasar instancias en lugar de crearlas en `__init__`.
- Separar lógica de negocio de I/O (e.g., extraer validaciones a una capa de servicios).
- Soporte para múltiples proveedores IMAP (no solo Gmail).

### 6. **Interfaz de Usuario**
- Mejorar el menú con librerías como `rich` para colores y tablas.
- Agregar validación de entrada más robusta y mensajes de ayuda.

### 7. **Documentación y Reportes**
- Generar reportes en formatos adicionales (e.g., JSON, PDF con `reportlab`).
- Agregar configuración externa para rutas de archivos.

### 8. **Dependencias y Compatibilidad**
- Actualizar requirements.txt con versiones fijas (e.g., `pandas==2.0.0`).
- Agregar compatibilidad con Python 3.8+ y probar en múltiples entornos.

Estas mejoras harían el código más robusto, seguro y escalable, manteniendo la simplicidad del proyecto.

---

# Antipatrones de Software

## 1. God Object (Objeto Dios)

Un **God Object** es una clase que concentra demasiadas responsabilidades y controla gran parte de la lógica del sistema.

### Problemas

* Código difícil de mantener.
* Alto acoplamiento.
* Baja reutilización.
* Cambios pequeños afectan muchas partes.

### Ejemplo

```java
class Sistema {
    void gestionarUsuarios() {}
    void generarReportes() {}
    void procesarPagos() {}
    void enviarCorreos() {}
}
```

### Solución

Aplicar el principio de responsabilidad única (**SRP**) y dividir la lógica en varias clases.

---

# 2. Spaghetti Code (Código Espagueti)

Código desorganizado con flujo difícil de seguir y dependencias caóticas.

### Problemas

* Difícil de entender.
* Complicado de depurar.
* Mantenimiento costoso.

### Ejemplo

```python
if x:
    while y:
        if z:
            for i in range(10):
                if a:
                    ...
```

### Solución

Modularizar el código y mejorar la estructura lógica.

---

# 3. Copy-Paste Programming

Consiste en copiar y pegar código repetidamente en lugar de reutilizar componentes.

### Problemas

* Duplicación de errores.
* Mantenimiento complicado.
* Código innecesariamente largo.

### Ejemplo

```java
void calcularEmpleado1() {}
void calcularEmpleado2() {}
void calcularEmpleado3() {}
```

### Solución

Crear funciones reutilizables o clases genéricas.

---

# 4. Golden Hammer (Martillo Dorado)

Usar siempre la misma tecnología o patrón aunque no sea adecuado.

### Problemas

* Soluciones ineficientes.
* Complejidad innecesaria.
* Limitación tecnológica.

### Ejemplo

Usar una base de datos relacional para todo, incluso datos temporales simples.

### Solución

Elegir herramientas según el problema específico.

---

# 5. Lava Flow

Código viejo o inútil que permanece porque nadie quiere tocarlo.

### Problemas

* Incrementa complejidad.
* Confusión para nuevos desarrolladores.
* Riesgo de errores ocultos.

### Ejemplo

```java
// NO BORRAR, TAL VEZ SE USE
void metodoViejo() {}
```

### Solución

Eliminar código muerto y mantener documentación clara.

---

# 6. Boat Anchor (Ancla de Barco)

Componente pesado o inútil que ralentiza el proyecto.

### Problemas

* Reduce rendimiento.
* Aumenta dependencias innecesarias.
* Complica despliegues.

### Ejemplo

Incluir una librería enorme para usar una sola función pequeña.

### Solución

Usar dependencias ligeras y necesarias.

---

# 7. Reinventar la Rueda

Crear soluciones desde cero cuando ya existen herramientas confiables.

### Problemas

* Pérdida de tiempo.
* Más errores.
* Costos innecesarios.

### Ejemplo

Crear tu propio sistema de autenticación en lugar de usar uno probado.

### Solución

Evaluar bibliotecas y frameworks existentes antes de programar.

---

# 8. Hard Code (Valores Quemados)

Valores escritos directamente en el código fuente.

### Problemas

* Difícil configuración.
* Baja flexibilidad.
* Riesgo al modificar.

### Ejemplo

```python
conexion = "192.168.1.1"
```

### Solución

Usar archivos de configuración o variables de entorno.

---

# 9. Magic Numbers

Uso de números sin contexto ni explicación.

### Problemas

* Código poco legible.
* Difícil mantenimiento.

### Ejemplo

```java
if (temperatura > 37.5) {}
```

### Solución

Usar constantes descriptivas.

```java
final double TEMPERATURA_MAXIMA = 37.5;
```

---

# 10. Programming by Exception

Usar excepciones para controlar el flujo normal del programa.

### Problemas

* Código lento.
* Difícil de leer.
* Mal manejo de errores reales.

### Ejemplo

```python
try:
    valor = lista[10]
except:
    valor = None
```

### Solución

Validar condiciones antes de lanzar excepciones.

---

# 11. Cargo Cult Programming

Copiar código sin entender cómo funciona.

### Problemas

* Errores ocultos.
* Dependencias innecesarias.
* Baja calidad del software.

### Ejemplo

Copiar configuraciones de internet “porque funcionan”.

### Solución

Comprender el propósito del código antes de implementarlo.

---

# 12. Premature Optimization

Optimizar demasiado pronto sin necesidad real.

### Problemas

* Código complejo.
* Pérdida de tiempo.
* Difícil mantenimiento.

### Ejemplo

Usar algoritmos avanzados para un sistema pequeño.

### Solución

Primero hacer que funcione, luego medir y optimizar.

---

# 13. Swiss Army Knife (Navaja Suiza)

Clase o componente que intenta hacer demasiadas cosas.

### Problemas

* Baja cohesión.
* Complejidad excesiva.
* Difícil reutilización.

### Ejemplo

```java
class Utilidades {
    void imprimir() {}
    void conectarBD() {}
    void calcularNomina() {}
}
```

### Solución

Separar funcionalidades por responsabilidad.

---

# 14. Singleton Abuse

Uso excesivo del patrón Singleton.

### Problemas

* Dependencias ocultas.
* Difícil testing.
* Problemas de concurrencia.

### Ejemplo

```java
Config.getInstance()
```

### Solución

Usar inyección de dependencias cuando sea posible.

---

# 15. Yo-Yo Problem

Jerarquías de herencia tan profundas que obligan a subir y bajar muchas clases para entender el sistema.

### Problemas

* Difícil comprensión.
* Mantenimiento complejo.
* Acoplamiento excesivo.

### Ejemplo

```text
Animal -> Mamifero -> Canino -> Perro -> PastorAleman
```

### Solución

Preferir composición sobre herencia excesiva.
