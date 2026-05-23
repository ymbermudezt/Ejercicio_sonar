# Análisis Sonnarqube

Integrantes

- Yhoan Mauricio Bermudez Tique (20242020242)

- Sebastian David Trujillo Vargas (20242020217)

- David Felipe Batanero Molina (20241020092)

# Comparación entre SonarQube y el análisis de malas prácticas

El análisis realizado con SonarQube complementa el análisis de malas prácticas del proyecto **Bot de Correo Spam**, ya que ambos enfoques evalúan la calidad del software desde perspectivas diferentes.

El análisis de malas prácticas se centró en aspectos como:
- Organización general del código
- Exceso de responsabilidades en controladores
- Acoplamiento entre módulos
- Patrones de diseño mejorables
- Oportunidades de refactorización

Por otro lado, SonarQube analiza directamente el código fuente para detectar problemas técnicos relacionados con:
- Mantenibilidad
- Complejidad del código
- Legibilidad
- Convenciones de programación
- Buenas prácticas en Python

---

## Principales issues detectados por SonarQube

### 1. Alta complejidad cognitiva
Se detectaron funciones demasiado complejas, especialmente en:
- `ControlCorreo.py`
- `ControlPrincipal.py`

Esto indica métodos con demasiadas decisiones, condicionales y responsabilidades mezcladas.

---

### 2. Variables no utilizadas
Se encontraron variables declaradas pero no utilizadas, como:
- `status`
- `result`
- `nombre`

Esto reduce la claridad y limpieza del código.

---

### 3. Problemas de estilo Python
Se detectó uso de estructuras menos recomendadas:
- Uso de `map` en lugar de list comprehensions

---

### 4. Convenciones de nombres
Algunas variables no siguen el estándar `snake_case` de Python.

Ejemplo:
```python
correosLimpio
```

Debería ser:
```python
correos_limpio
```

---

## 🔗 Relación con el análisis de malas prácticas

Los resultados de SonarQube refuerzan directamente las malas prácticas identificadas en el proyecto.

En particular, ambos análisis coinciden en que existe:

- Alta complejidad en controladores, especialmente en `ControlPrincipal`
- Exceso de responsabilidades en métodos largos
- Dificultad de mantenimiento por falta de modularidad
- Necesidad de refactorización para mejorar legibilidad

Mientras el análisis de malas prácticas identifica los problemas desde una perspectiva de diseño y arquitectura, SonarQube los valida con evidencia técnica dentro del código fuente.

---

## Conclusión

Ambos enfoques se complementan:

- El análisis de malas prácticas identifica problemas estructurales del sistema.
- SonarQube detecta problemas técnicos concretos en la implementación.

La combinación de ambos permite obtener una visión más completa del proyecto y mejorar su mantenibilidad, claridad y escalabilidad.
```