<p align="center"> <img src="img/images.png" width="15%"> </p> 
<h1 align="center">Bot de Correo Spam</h1> 
<p align="center">
<br> 21/10/2025
<br> Python de 0 a 100 </b> 
</p><hr> <h2>Descripción</h2> 
<p>El proyecto consiste en un bot automatizado desarrollado en Python que ayuda a los estudiantes a limpiar su bandeja de entrada eliminando mensajes no deseados o spam. El bot utiliza reglas simples y conexión IMAP para analizar los correos y mover los mensajes sospechosos a la carpeta de spam o eliminarlos. De esta manera, el usuario ahorra tiempo y mantiene su correo organizado. </p> 
<h3>Problemática o necesidad</h3> 
<p>Los estudiantes suelen recibir gran cantidad de correos no deseados: promociones, suscripciones y notificaciones irrelevantes. Revisar y borrar estos mensajes manualmente consume tiempo que podría aprovecharse en tareas académicas. Este bot busca automatizar esa limpieza, detectando mensajes de spam con base en palabras clave o remitentes repetidos.</p> 
<hr> <h2>Descripción General</h2> 
<p>Este proyecto es un <strong>bot automatizado en Python</strong> que analiza los correos electrónicos de la cuenta del usuario, identifica mensajes no deseados mediante palabras clave y los elimina o marca como spam.</p> 
<h3>¿Qué hace el proyecto?</h3> 
<ol> <li>Analiza los correos electrónicos de la cuenta del usuario.</li> 
<li>Identifica mensajes que contienen palabras clave como “promoción”, “suscríbete”, “casino”, “gana dinero”, etc.</li> 
<li>Los marca como spam o los elimina directamente.</li> </ol> 
<h3>⚙️ ¿Cómo funciona?</h3> 
<ol> <li>El usuario ejecuta el bot desde la consola.</li> 
<li>Se conecta a su cuenta de correo mediante el protocolo <strong>IMAP</strong>, que permite descargar los mensajes al sistema local para su análisis.</li> 
<li>Descarga los asuntos y remitentes de los correos recientes.</li> 
<li>Aplica reglas de detección (por palabras clave o listas de remitentes).</li> 
<li>Elimina o clasifica los mensajes detectados como spam.</li> 
</ol> <h3>Fuentes de palabras clave y remitentes</h3> 
<p>El bot utilizará un archivo de configuración externo (por ejemplo, <code>config.json</code> o <code>datos.csv</code>) que contendrá:</p> 
<ul> <li>Credenciales del usuario (correo y contraseña de aplicación).</li> 
<li>Palabras clave y remitentes a bloquear.</li> 
</ul> <p>El archivo será editable desde la consola, de modo que el usuario pueda modificar las listas de spam o actualizar sus datos sin tocar el código directamente.</p> <h3>Resultados esperados</h3> 
<ul> <li>Bandeja de entrada más limpia y ordenada.</li> 
<li>Ahorro de tiempo al eliminar correos basura automáticamente.</li> 
<li>Reporte con cantidad de correos revisados, detectados y eliminados.</li> </ul> 
<hr> <h2>Alcance</h2> 
<h3>Qué sí incluirá</h3> 
<ul> <li>Conexión IMAP al correo electrónico.</li> 
<li>Búsqueda y lectura de correos recientes.</li> 
<li>Filtrado mediante palabras clave y remitentes.</li> 
<li>Eliminación o clasificación de correos como spam.</li> <li>Archivo externo con credenciales y listas de spam editables desde consola.</li> 
<li>Generación de un reporte con estadísticas.</li> 
<li>Interfaz por consola simple para que el usuario elija acciones.</li> 
</ul> <h3>Qué no incluirá</h3> 
<ul> <li>No implementará un modelo de inteligencia artificial.</li> 
<li>No manejará interfaz gráfica interactiva.</li> 
<li>No incluirá conexión POP3, solo IMAP.</li> 
</ul> <p><em>Estas funciones quedan fuera del alcance por la complejidad técnica, el tiempo disponible y la poca versatilidad.</em></p> 
<hr> <h2>Categoría</h2> 
<p>La aplicación cae en las categorías de <strong>automatización</strong> y <strong>aplicación interactiva por consola</strong>.</p> 
<hr> <h2>Tecnologías y Herramientas</h2> 
<ul> <li><strong>Lenguaje:</strong> Python 3.11</li> 
<li><strong>Entorno:</strong> Visual Studio Code</li> <li><strong>Protocolo:</strong> IMAP (para lectura de correos)</li> </ul> 
<h3>Librerías principales</h3> 
<table> <tr><th>Librería</th>
  <th>Función</th></tr> 
  <tr><td>poplib</td>
  <td>Conexión y lectura de correos mediante IMAP.</td></tr> 
  <tr><td>email</td>
  <td>Análisis del contenido de los mensajes.</td></tr> 
  <tr><td>re</td>
  <td>Búsqueda de palabras clave con expresiones regulares.</td></tr> 
  <tr><td>pandas</td><td>Manipulación de datos y generación de reportes.</td></tr> 
  <tr><td>json</td><td>Lectura y modificación del archivo de configuración.</td></tr> </table> 
<hr> <h2>Fuentes de Datos</h2> 
<ol> <li>Archivo local de configuración con credenciales y palabras clave.</li> 
<li>Correos obtenidos mediante conexión IMAP.</li> </ol> 
<hr> <h2>Conceptos aplicados del curso</h2> 
<table> <tr><th>Concepto</th>
  <th>Aplicación</th></tr> 
  <tr><td>Variables y tipos de datos</td>
  <td>Almacenar correos, credenciales y listas de palabras clave.</td></tr> 
  <tr><td>Estructuras de control</td>
  <td>Validar la conexión y clasificar correos según criterios de spam.</td></tr> 
  <tr><td>Funciones</td>
  <td>Para conexión, lectura, análisis y eliminación de correos.</td>
  </tr> <tr><td>Funciones Lambda</td>
  <td>Filtrado rápido de mensajes con <code>map()</code> y <code>filter()</code>.</td></tr> 
  <tr><td>*args y **kwargs</td>
  <td>Para manejar listas flexibles de palabras clave y remitentes.</td></tr> 
  <tr><td>Pandas</td>
  <td>Creación de reportes y conteos de correos revisados.</td>
  </tr> <tr><td>Manejo de archivos</td>
  <td>Lectura y escritura del archivo de configuración (JSON o CSV).</td></tr> 
  <tr><td>Manejo de errores</td>
  <td>Uso de <code>try/except</code> para controlar fallos de conexión o acceso.</td></tr> </table> 
<hr> <h2>Resultados Esperados</h2> 
<ul> <li>Bot funcional que detecta y elimina correos spam.</li> 
<li>Reporte automático con estadísticas: revisados, eliminados y tiempo de ejecución.</li> 
<li>Código modular, limpio y documentado.</li> 
<li>Archivo externo editable desde consola con listas de spam.</li> </ul>
<h2>Instalación</h2>
<ol>
    <li>Clonar el repositorio:
        <pre class="command">git clone https://github.com/Sebast1023/Proyecto-python-acm.git</pre>
    </li>
    <li>Entrar a la carpeta del proyecto:
        <pre class="command">cd Proyecto-python-acm</pre>
    </li>
    <li>Crear un entorno virtual (opcional pero recomendado):
        <pre class="command">
        
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python -m venv venv
source venv/bin/activate
        </pre>
        </li>
        <li>Instalar dependencias:
            <pre class="command">pip install -r requirements.txt</pre>
        </li>
    </ol>

  <h2>Cómo ejecutar el proyecto</h2>
  <p>Desde la raíz del proyecto (Proyecto-python-acm), ejecutar el launcher:</p>
  <pre class="command">python -m src.Control.Launcher</pre>
