# Taller Interactivo: Colaboración con Git/GitHub en Proyectos oTree

## Información del Taller

| Campo | Valor |
|-------|-------|
| **Duración estimada** | 3-4 horas |
| **Participantes** | Mauricio, José Miguel, Sergio, Donovan |
| **Nivel** | Ninguno |
| **Proyecto base** | Public Goods Game (oTree) |
| **Referencia académica** | Fehr & Gächter (2000), "Cooperation and Punishment in Public Goods Experiments" |

---

# PARTE 1: FUNDAMENTOS DE GIT EN 5 MINUTOS

## 1.1 ¿Qué es Git y para qué sirve?

Git es como un "historial de cambios" muy poderoso para tus archivos. Imagina que puedes:
- Guardar "fotos" de tu proyecto en diferentes momentos
- Volver atrás si algo sale mal
- Trabajar en equipo sin pisarse los cambios

**GitHub** es simplemente un lugar en internet donde guardas ese historial para que todos puedan acceder.

---

## 1.2 Los 5 Comandos Esenciales (¡Solo 5!)

Aquí está TODO lo que necesitas saber para este taller:

### 🌿 1. CREAR UNA RAMA (tu espacio de trabajo)

```bash
git checkout -b nombre-de-tu-rama
```

**¿Qué hace?** Crea una "copia paralela" del proyecto donde puedes hacer cambios sin afectar el código principal. Es como tener tu propio borrador.

**Ejemplo real:**
```bash
git checkout -b instrucciones-comprension
```

---

### ➕ 2. AGREGAR TUS CAMBIOS (preparar para guardar)

```bash
git add .
```

**¿Qué hace?** Le dice a Git "estos son los archivos que quiero guardar". El punto (`.`) significa "todos los archivos que cambié".

**También puedes agregar archivos específicos:**
```bash
git add public_goods/__init__.py
git add public_goods/templates/public_goods/Introduction.html
```

---

### 💾 3. GUARDAR TUS CAMBIOS (commit)

```bash
git commit -m "descripción corta de lo que hiciste"
```

**¿Qué hace?** Guarda una "foto" de tus cambios con una descripción. Es como hacer "Guardar como..." con una nota.

**Ejemplos de buenos mensajes:**
```bash
git commit -m "agrega página de instrucciones"
git commit -m "corrige error en cálculo de payoff"
git commit -m "añade validación a preguntas de comprensión"
```

---

### ⬆️ 4. SUBIR TUS CAMBIOS (push)

```bash
git push -u origin nombre-de-tu-rama
```

**¿Qué hace?** Sube tus cambios guardados a GitHub para que otros puedan verlos.

**Ejemplo:**
```bash
git push -u origin feature/instrucciones-comprension
```

> **Nota:** La primera vez usas `-u origin nombre-rama`. Después, solo necesitas `git push`.

---

### 🔄 5. PULL REQUEST (pedir que integren tu trabajo)

**Esto se hace en GitHub (no en la terminal):**

1. Ve a tu repositorio en GitHub
2. Verás un botón amarillo que dice **"Compare & pull request"** → Haz clic
3. Escribe un título descriptivo
4. Escribe qué cambios hiciste
5. Haz clic en **"Create pull request"**

**¿Cuándo hacer Pull Request?** Solo cuando hayas terminado completamente tu issue asignado y verificado que funciona.

---

## 1.3 Flujo Completo: Del Clon al Pull Request

### Paso 1: Clonar el repositorio (solo una vez)


agregar la terminal donde tienen que correr esto.
```bash
# Ir a la carpeta donde quieres el proyecto
cd ~/proyectos

# Clonar (descargar) el repositorio
git clone git@github.com:[USUARIO]/taller-otree-pgg.git

# Entrar a la carpeta del proyecto
cd taller-otree-pgg

# Verificar que funciona
otree devserver
```

Abre tu navegador en `http://localhost:8000` y verifica que ves la interfaz de oTree.

---

### Paso 2: Crear tu rama de trabajo

```bash
# Asegúrate de estar en la rama principal actualizada
git checkout main

# dejarlo, ahorita no tiene sentido, es lo que normalmente se haría
git pull origin main

# Crea tu rama de trabajo
git checkout -b feature/tu-nombre-de-feature
```

---

### Paso 3: Trabajar y hacer commits

Mientras trabajas en tu código, haz commits cada vez que completes algo importante:

```bash
# Agregar cambios
git add .

# Guardar con mensaje descriptivo
git commit -m "descripción de lo que completaste"
```

**💡 ¿Cuándo hacer commit?** 
- Cuando termines una subtarea completa
- Cuando algo funcione correctamente
- Antes de hacer un cambio grande (por si necesitas volver atrás)

---

### Paso 4: Subir tus cambios

```bash
git push -u origin feature/tu-nombre-de-feature
```

---

### Paso 5: Crear Pull Request (al terminar todo)

1. Ve a GitHub → Tu repositorio
2. Clic en **"Compare & pull request"**
3. Llena el formulario y clic en **"Create pull request"**

---

## 📋 Resumen Visual del Flujo

```
┌─────────────────────────────────────────────────────────────────┐
│  1. git checkout -b mi-rama     → Crear espacio de trabajo      │
│                                                                 │
│  2. (trabajas en tu código...)                                  │
│                                                                 │
│  3. git add .                   → Preparar cambios              │
│                                                                 │
│  4. git commit -m "mensaje"     → Guardar cambios               │
│                                                                 │
│  5. (repite 2-4 varias veces hasta terminar)                    │
│                                                                 │
│  6. git push -u origin mi-rama  → Subir a GitHub                │
│                                                                 │
│  7. Pull Request en GitHub      → Pedir integración             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1.4 Estructura del Proyecto Base

Después de clonar, la estructura debe ser:

indicar que tienen que abrir  la carpeta del pryecto en visual studio y decirles como se abre una carpeta

```
taller-otree-pgg/
├── settings.py
├── public_goods/
│   ├── __init__.py
│   └── templates/
│       └── public_goods/
│           ├── Contribute.html
│           └── Results.html
├── [otras apps de ejemplo...]
└── .gitignore
```

---

---

## 1.5 ¡Prueba el programa antes de empezar!

Antes de comenzar con tu issue asignado, es importante que corras el programa base para entender cómo funciona:

1. Inicia el servidor: `otree devserver`
2. Abre `http://localhost:8000` en tu navegador
3. Haz clic en "Public Goods" y juega una sesión completa
4. Observa: la página de contribución, la espera, y los resultados

Esto te ayudará a entender qué parte del flujo vas a modificar con tu issue.

---

2. Modificaciones al juego basadas en Fehr & Gächter (2000)
El paper de Fehr & Gächter estudia cómo el castigo afecta la cooperación. Las modificaciones que implementan los 4 módulos son:
MóduloParticipanteQué agregaRelación con Fehr & Gächter1MauricioInstrucciones + ComprensiónEstándar en experimentos: asegurar que los sujetos entienden las reglas antes de jugar2José MiguelTratamientos con diferente MPCRFehr & Gächter comparan diferentes niveles de incentivo a cooperar (MPCR alto vs bajo)3SergioVisualización de resultadosLos sujetos deben ver claramente qué contribuyó cada quien antes de decidir si castigar4DonovanSistema de castigoEl corazón del paper: permitir que los jugadores paguen para reducir el payoff de otros
El mecanismo de castigo (lo central del paper):

Sin castigo: El equilibrio de Nash es contribuir 0 (todos son free-riders)
Con castigo: Los cooperadores pueden "castigar" a los free-riders
Resultado empírico: La cooperación aumenta significativamente cuando hay posibilidad de castigo

Parámetros del castigo (ratio 1:3):

Cuesta 1 punto enviar un punto de castigo
El castigado pierde 3 puntos por cada punto recibido
Este ratio hace que castigar sea "costoso" pero efectivo

Básicamente, el taller toma un Public Goods Game básico y lo transforma en la versión con castigo de Fehr & Gächter, que es uno de los diseños más citados en economía experimental.


# PARTE 2: EL JUEGO DEL BIEN PÚBLICO - EXPLICACIÓN

## 2.1 ¿Qué es el Juego del Bien Público?

El **Juego del Bien Público** (Public Goods Game) es uno de los experimentos más importantes en economía experimental. Sirve para estudiar cómo las personas cooperan (o no) cuando hay un beneficio colectivo.

### La situación básica

Imagina este escenario:
- Hay **3 personas** en un grupo
- Cada persona recibe **100 puntos** 
- Cada persona decide cuántos puntos **contribuir** a un "fondo común"
- El fondo común se **multiplica por 2** y luego se **divide entre todos por igual**

### El dilema

Aquí está lo interesante:
- **Si todos cooperan:** El grupo entero gana más
- **Si solo tú no cooperas:** Tú ganas más que los demás (pero el grupo pierde)
- **Si nadie coopera:** Todos ganan menos que si hubieran cooperado

### Ejemplo numérico

| Jugador | Dotación | Contribuye | Se queda | Recibe del fondo | **Total** |
|---------|----------|------------|----------|------------------|-----------|
| Ana     | 100      | 50         | 50       | 100              | **150**   |
| Bob     | 100      | 50         | 50       | 100              | **150**   |
| Carlos  | 100      | 50         | 50       | 100              | **150**   |

**Cálculo:**
- Total contribuido: 50 + 50 + 50 = 150
- Fondo multiplicado: 150 × 2 = 300
- Parte de cada uno: 300 ÷ 3 = 100

**Pero si Carlos decide no cooperar:**

| Jugador | Dotación | Contribuye | Se queda | Recibe del fondo | **Total** |
|---------|----------|------------|----------|------------------|-----------|
| Ana     | 100      | 50         | 50       | 66.67            | **116.67**|
| Bob     | 100      | 50         | 50       | 66.67            | **116.67**|
| Carlos  | 100      | 0          | 100      | 66.67            | **166.67**|

Carlos gana más, pero Ana y Bob pierden. El grupo en total tiene menos.

---

## 2.2 El Código Base Explicado

### Archivo clave: `public_goods/__init__.py`

```python
from otree.api import *  # Importa todas las funciones necesarias de oTree

# Descripción del experimento (aparece en la documentación)
doc = """
Public Goods Game - Taller Git/GitHub
"""


class C(BaseConstants):
    """
    CONSTANTES DEL JUEGO
    Aquí definimos los parámetros que NO cambian durante el experimento.
    Usamos 'C' como nombre corto para acceder fácilmente (ej: C.ENDOWMENT)
    """
    NAME_IN_URL = 'public_goods'  # Cómo aparece en la URL del navegador
    PLAYERS_PER_GROUP = 3         # Número de jugadores por grupo
    NUM_ROUNDS = 1                # Número de rondas del juego
    ENDOWMENT = cu(100)           # Dotación inicial (cu = currency units = puntos)
    MULTIPLIER = 2                # Factor por el que se multiplica el fondo común


class Subsession(BaseSubsession):
    """
    SUBSESIÓN
    Representa una "ronda" del juego. En este caso solo hay 1 ronda.
    Si tuviéramos múltiples rondas, cada una sería una subsession diferente.
    Por ahora la dejamos vacía porque no necesitamos configuración especial.
    """
    pass


class Group(BaseGroup):
    """
    GRUPO
    Almacena información compartida entre los jugadores de un mismo grupo.
    Aquí guardamos los totales que afectan a todos.
    """
    # Total que contribuyeron todos los jugadores del grupo
    total_contribution = models.CurrencyField()
    
    # Lo que le toca a cada jugador del fondo común (después de multiplicar y dividir)
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    """
    JUGADOR
    Almacena información individual de cada participante.
    Cada jugador tiene su propia copia de estos campos.
    """
    # Cuánto decide contribuir este jugador al fondo común
    # - min=0: no puede contribuir menos de 0
    # - max=C.ENDOWMENT: no puede contribuir más de lo que tiene (100)
    # - label: el texto que ve el participante en el formulario
    contribution = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuánto quieres contribuir al fondo común?"
    )


# ============ PÁGINAS ============
# Las páginas definen lo que ve el participante y en qué orden

class Contribute(Page):
    """
    PÁGINA DE CONTRIBUCIÓN
    Aquí el participante decide cuánto contribuir.
    """
    form_model = 'player'              # Los datos se guardan en el modelo Player
    form_fields = ['contribution']      # Qué campo(s) mostrar en el formulario


class ResultsWaitPage(WaitPage):
    """
    PÁGINA DE ESPERA
    Los participantes esperan aquí hasta que TODOS hayan contribuido.
    Una vez que todos llegan, se ejecuta 'set_payoffs' para calcular ganancias.
    """
    after_all_players_arrive = 'set_payoffs'  # Función a ejecutar cuando todos lleguen


class Results(Page):
    """
    PÁGINA DE RESULTADOS
    Muestra los resultados finales a cada participante.
    """
    pass  # No necesita configuración especial, solo muestra el template


# ============ FUNCIONES ============

def set_payoffs(group: Group):
    """
    CÁLCULO DE GANANCIAS
    Esta función se ejecuta automáticamente cuando todos los jugadores 
    han completado la página de contribución.
    
    Fórmula de ganancia:
    payoff = (lo que me quedé) + (mi parte del fondo común)
    payoff = (ENDOWMENT - contribution) + (total_contribution × MULTIPLIER / N)
    """
    # Obtener la lista de todos los jugadores del grupo
    players = group.get_players()
    
    # Obtener las contribuciones de cada jugador
    contributions = [p.contribution for p in players]
    
    # Calcular el total contribuido por el grupo
    group.total_contribution = sum(contributions)
    
    # Calcular cuánto le toca a cada uno del fondo común:
    # (total × multiplicador) ÷ número de jugadores
    group.individual_share = group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    
    # Asignar la ganancia final a cada jugador
    for p in players:
        # Ganancia = lo que no contribuí + mi parte del fondo
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share


# ============ SECUENCIA DE PÁGINAS ============
# Define el orden en que aparecen las páginas
page_sequence = [Contribute, ResultsWaitPage, Results]
```

---

# PARTE 3: MÓDULOS DE TRABAJO

Cada participante trabajará en su issue asignado. A continuación se detallan las instrucciones, hints, y soluciones para cada uno.

---

## 3.1 MÓDULO 1: Mauricio - Instrucciones y Comprensión

### Objetivo
Crear una página de instrucciones clara y una página de preguntas de comprensión que valide que el participante entiende el juego antes de comenzar.

### Flujo de trabajo Git

```bash
# 1. Asegurarse de estar en main actualizado
git checkout main
git pull origin main

# 2. Crear rama de feature
git checkout -b feature/instrucciones-comprension

# 3. Verificar que estás en la rama correcta
git branch
# Debe mostrar: * feature/instrucciones-comprension
```

### Prompt sugerido para IA

> **Modelo recomendado:** Claude Opus 4.5  
> **Justificación:** Esta tarea requiere coherencia entre múltiples archivos (HTML + Python) y conocimiento específico de oTree 5. Opus 4.5 destaca en tareas multi-archivo con frameworks específicos.

```
Actúa como un desarrollador experto en oTree 5 y economía experimental.

CONTEXTO:
Estoy implementando un Public Goods Game en oTree 5. Necesito crear:
1. Una página de instrucciones (Introduction.html)
2. Una página de preguntas de comprensión (Comprehension.html)

PARÁMETROS DEL JUEGO:
- PLAYERS_PER_GROUP = 3
- ENDOWMENT = 100 puntos
- MULTIPLIER = 2
- El fondo común se multiplica y divide equitativamente

REQUISITOS:
1. Las instrucciones deben explicar:
   - Cuánto tiene cada jugador inicialmente
   - Cómo funciona la contribución al fondo común
   - Cómo se calcula el payoff final
   - Un ejemplo numérico concreto

2. Las preguntas de comprensión deben incluir:
   - Pregunta sobre dotación inicial
   - Pregunta sobre qué pasa con las contribuciones
   - Pregunta de cálculo de payoff con números específicos

3. La validación debe:
   - Usar error_message() en oTree 5
   - Mostrar mensaje claro si hay error
   - Permitir reintentos

ESTRUCTURA DE ARCHIVOS EN OTREE 5:
- Todo está en public_goods/__init__.py (Pages, Models, etc.)
- Templates en public_goods/templates/public_goods/

OUTPUT ESPERADO:
1. Código completo para agregar a __init__.py (clases Player fields, Pages)
2. Template Introduction.html completo
3. Template Comprehension.html completo

Usa la estructura de oTree 5 (no oTree 3). Incluye comentarios explicativos.
```

### Descripción de la tarea

**Archivos a crear/modificar:**
- `public_goods/__init__.py` - Agregar campos y páginas
- `public_goods/templates/public_goods/Introduction.html` - Nuevo
- `public_goods/templates/public_goods/Comprehension.html` - Nuevo

**Especificaciones:**
1. La página de Introduction debe tener instrucciones claras en español
2. La página de Comprehension debe tener 3 preguntas con validación
3. Los participantes deben responder correctamente para continuar

---

### 💡 HINT (leer solo si llevas más de 15 minutos atascado)

<details>
<summary>Click para ver el hint</summary>

**Para las preguntas de comprensión en oTree 5:**

1. Define los campos en la clase `Player`:
```python
class Player(BasePlayer):
    # ... campos existentes ...
    comp_q1 = models.IntegerField(label="...")
    comp_q2 = models.IntegerField(label="...")
    comp_q3 = models.IntegerField(label="...")
```

2. Usa `error_message` a nivel de página para validar:
```python
class Comprehension(Page):
    form_model = 'player'
    form_fields = ['comp_q1', 'comp_q2', 'comp_q3']
    
    @staticmethod
    def error_message(player, values):
        # Validar aquí
        if values['comp_q1'] != RESPUESTA_CORRECTA:
            return 'La respuesta a la pregunta 1 es incorrecta.'
```

3. Para las páginas, recuerda agregarlas a `page_sequence`:
```python
page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]
```

</details>

---

### ✅ SOLUCIÓN COMPLETA

<details>
<summary>Click para ver la solución completa</summary>

#### Modificaciones a `public_goods/__init__.py`

Agregar estos campos a la clase `Player`:

```python
class Player(BasePlayer):
    """
    JUGADOR - Campos para contribución y comprensión
    """
    # Campo de contribución (ya existente)
    contribution = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuánto quieres contribuir al fondo común?"
    )
    
    # ============ PREGUNTAS DE COMPRENSIÓN ============
    # Estas preguntas verifican que el participante entendió las instrucciones
    
    # Pregunta 1: Verificar que saben la dotación inicial
    comp_q1 = models.IntegerField(
        label="¿Cuántos puntos recibe cada jugador al inicio de la ronda?"
    )
    
    # Pregunta 2: Verificar que entienden cómo se suma el fondo
    # Usamos choices para dar opciones y facilitar la respuesta
    comp_q2 = models.IntegerField(
        label="Si todos los jugadores contribuyen 50 puntos cada uno, ¿cuánto habrá en el fondo común ANTES de multiplicar?",
        choices=[
            [50, '50 puntos'],
            [100, '100 puntos'],
            [150, '150 puntos'],  # ← Respuesta correcta: 3 jugadores × 50 = 150
            [200, '200 puntos'],
        ]
    )
    
    # Pregunta 3: Verificar que entienden la división del fondo
    comp_q3 = models.IntegerField(
        label="Si el fondo común tiene 300 puntos después de multiplicar, ¿cuánto recibe cada jugador del fondo?",
        choices=[
            [50, '50 puntos'],
            [100, '100 puntos'],  # ← Respuesta correcta: 300 ÷ 3 = 100
            [150, '150 puntos'],
            [300, '300 puntos'],
        ]
    )
```

Agregar estas páginas:

```python
class Introduction(Page):
    """
    PÁGINA DE INSTRUCCIONES
    Muestra las reglas del juego al participante.
    No tiene formulario, solo información.
    """
    pass  # Solo muestra el template, no necesita lógica adicional


class Comprehension(Page):
    """
    PÁGINA DE COMPRENSIÓN
    Verifica que el participante entendió las instrucciones.
    Si responde mal, muestra un mensaje de error y debe intentar de nuevo.
    """
    form_model = 'player'
    form_fields = ['comp_q1', 'comp_q2', 'comp_q3']
    
    @staticmethod
    def error_message(player, values):
        """
        Valida las respuestas. Si alguna es incorrecta, retorna un mensaje de error.
        El participante debe corregir para continuar.
        """
        # Diccionario con las respuestas correctas
        solutions = {
            'comp_q1': C.ENDOWMENT,  # 100 puntos (usamos la constante para consistencia)
            'comp_q2': 150,           # 3 jugadores × 50 = 150
            'comp_q3': 100,           # 300 ÷ 3 = 100
        }
        
        # Lista para acumular mensajes de error
        errors = []
        
        # Verificar cada respuesta
        if values['comp_q1'] != solutions['comp_q1']:
            errors.append(f"Pregunta 1: La respuesta correcta es {solutions['comp_q1']} puntos.")
        
        if values['comp_q2'] != solutions['comp_q2']:
            errors.append("Pregunta 2: Recuerda que hay 3 jugadores y cada uno contribuye 50.")
        
        if values['comp_q3'] != solutions['comp_q3']:
            errors.append("Pregunta 3: El fondo se divide equitativamente entre los 3 jugadores.")
        
        # Si hay errores, retornar el mensaje (esto impide avanzar)
        if errors:
            return ' '.join(errors)
        # Si no hay errores, retornar None permite avanzar
```

Actualizar `page_sequence`:

```python
# El orden en que aparecen las páginas
page_sequence = [Introduction, Comprehension, Contribute, ResultsWaitPage, Results]
```

---

#### 📍 MOMENTO DE COMMIT #1
```bash
git add public_goods/__init__.py
git commit -m "feat(player): agrega campos de comprensión comp_q1, comp_q2, comp_q3"
```

---

#### Template: `Introduction.html`

Crear archivo `public_goods/templates/public_goods/Introduction.html`:

```html
{{ block title }}
    Instrucciones del Juego
{{ endblock }}

{{ block content }}
<div class="instructions">
    <h3>Bienvenido al Juego de Bienes Públicos</h3>
    
    <p>En este juego, formarás parte de un grupo de <strong>{{ C.PLAYERS_PER_GROUP }} jugadores</strong>.</p>
    
    <h4>Dotación Inicial</h4>
    <p>Cada jugador recibe <strong>{{ C.ENDOWMENT }} puntos</strong> al inicio de cada ronda.</p>
    
    <h4>Decisión</h4>
    <p>Debes decidir cuántos de tus {{ C.ENDOWMENT }} puntos quieres contribuir a un <strong>fondo común</strong>.</p>
    <ul>
        <li>Puedes contribuir cualquier cantidad entre 0 y {{ C.ENDOWMENT }} puntos.</li>
        <li>Los puntos que NO contribuyas se quedan contigo.</li>
    </ul>
    
    <h4>El Fondo Común</h4>
    <p>Las contribuciones de todos los jugadores se suman y se <strong>multiplican por {{ C.MULTIPLIER }}</strong>.</p>
    <p>Luego, el fondo multiplicado se <strong>divide equitativamente</strong> entre los {{ C.PLAYERS_PER_GROUP }} jugadores.</p>
    
    <h4>Tu Ganancia</h4>
    <p>Tu ganancia final será:</p>
    <div class="formula" style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; margin: 10px 0;">
        <strong>Ganancia = (Puntos que guardaste) + (Tu parte del fondo común)</strong>
    </div>
    
    <h4>Ejemplo</h4>
    <div class="example" style="background-color: #e8f4e8; padding: 15px; border-radius: 5px; margin: 10px 0;">
        <p>Supongamos que:</p>
        <ul>
            <li>Jugador 1 contribuye 40 puntos</li>
            <li>Jugador 2 contribuye 60 puntos</li>
            <li>Jugador 3 contribuye 20 puntos</li>
        </ul>
        <p><strong>Total contribuido:</strong> 40 + 60 + 20 = 120 puntos</p>
        <p><strong>Fondo después de multiplicar:</strong> 120 × {{ C.MULTIPLIER }} = 240 puntos</p>
        <p><strong>Parte de cada jugador:</strong> 240 ÷ 3 = 80 puntos</p>
        <p><strong>Ganancia del Jugador 1:</strong> (100 - 40) + 80 = <strong>140 puntos</strong></p>
        <p><strong>Ganancia del Jugador 2:</strong> (100 - 60) + 80 = <strong>120 puntos</strong></p>
        <p><strong>Ganancia del Jugador 3:</strong> (100 - 20) + 80 = <strong>160 puntos</strong></p>
    </div>
    
    <p style="margin-top: 20px;">
        <strong>A continuación, responderás algunas preguntas para verificar que entendiste las instrucciones.</strong>
    </p>
</div>

{{ next_button }}
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #2
```bash
git add public_goods/templates/public_goods/Introduction.html
git commit -m "feat(templates): crea página Introduction con instrucciones del juego"
```

---

#### Template: `Comprehension.html`

Crear archivo `public_goods/templates/public_goods/Comprehension.html`:

```html
{{ block title }}
    Preguntas de Comprensión
{{ endblock }}

{{ block content }}
<div class="comprehension">
    <p>Por favor responde las siguientes preguntas para verificar que entendiste las instrucciones.</p>
    <p><em>Debes responder correctamente todas las preguntas para continuar.</em></p>
    
    <div class="question" style="margin: 20px 0; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
        <label><strong>Pregunta 1:</strong></label>
        {{ formfields.comp_q1 }}
    </div>
    
    <div class="question" style="margin: 20px 0; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
        <label><strong>Pregunta 2:</strong></label>
        {{ formfields.comp_q2 }}
    </div>
    
    <div class="question" style="margin: 20px 0; padding: 15px; background-color: #f9f9f9; border-radius: 5px;">
        <label><strong>Pregunta 3:</strong></label>
        {{ formfields.comp_q3 }}
    </div>
</div>

{{ next_button }}
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #3
```bash
git add public_goods/templates/public_goods/Comprehension.html
git commit -m "feat(templates): crea página Comprehension con validación de respuestas"
```

---

#### 📍 MOMENTO DE COMMIT #4 (si actualizaste page_sequence por separado)
```bash
git add public_goods/__init__.py
git commit -m "feat(pages): actualiza page_sequence con Introduction y Comprehension"
```

---

#### Subir cambios y crear Pull Request
```bash
# Subir todos los cambios a GitHub
git push -u origin feature/instrucciones-comprension

# Luego ve a GitHub y crea el Pull Request
```

</details>

---

### Verificación local

Antes de hacer push, verificar que funciona:

```bash
# Iniciar servidor
otree devserver

# Abrir en navegador: http://localhost:8000
# Probar el flujo completo:
# 1. Introduction -> debe mostrar instrucciones
# 2. Comprehension -> probar con respuestas incorrectas (debe mostrar error)
# 3. Comprehension -> probar con respuestas correctas (debe continuar)
```

---

## 3.2 MÓDULO 2: José Miguel - Parámetros y Tratamientos

### Objetivo
Hacer los parámetros del juego configurables desde `settings.py` y crear dos tratamientos experimentales con diferentes valores de MPCR (Marginal Per Capita Return).

### Flujo de trabajo Git

```bash
# 1. Asegurarse de estar en main actualizado
git checkout main
git pull origin main

# 2. Crear rama de feature
git checkout -b feature/parametros-tratamientos

# 3. Verificar que estás en la rama correcta
git branch
# Debe mostrar: * feature/parametros-tratamientos
```

### Prompt sugerido para IA

> **Modelo recomendado:** GPT-5.1 Thinking  
> **Justificación:** Esta tarea requiere razonamiento sobre parámetros económicos (MPCR) y anticipar edge cases en la configuración. GPT-5.1 es mejor para tareas donde necesitas que el modelo "piense defensivamente" sobre posibles errores.

```
Eres un economista experimental experto en oTree 5 y diseño de experimentos.

CONTEXTO:
Tengo un Public Goods Game en oTree 5 con estos parámetros hardcodeados:
- PLAYERS_PER_GROUP = 3
- ENDOWMENT = 100
- MULTIPLIER = 2

OBJETIVO:
1. Hacer estos parámetros configurables desde settings.py
2. Crear dos tratamientos experimentales:
   - high_mpcr: multiplicador = 2.0 (MPCR = 0.67)
   - low_mpcr: multiplicador = 1.2 (MPCR = 0.40)

REQUISITOS TÉCNICOS EN OTREE 5:
- Los parámetros de sesión se definen en SESSION_CONFIGS en settings.py
- Se acceden en el código via self.session.config['param_name']
- Los valores por defecto deben estar en la clase C (Constants)

CONSIDERACIONES ECONÓMICAS:
- MPCR = multiplicador / n_jugadores
- MPCR > 1/n: contribuir es socialmente óptimo
- MPCR < 1: el equilibrio de Nash es contribuir 0
- Explica en comentarios por qué elegimos estos valores

OUTPUT ESPERADO:
1. Código modificado de settings.py con los dos tratamientos
2. Código modificado de __init__.py para leer parámetros de sesión
3. Documentación inline explicando el diseño experimental

Anticipa posibles errores (ej: qué pasa si un parámetro no está definido).
```

### Descripción de la tarea

**Archivos a modificar:**
- `settings.py` - Agregar configuraciones de sesión
- `public_goods/__init__.py` - Modificar para leer parámetros de sesión

**Especificaciones:**
1. Los parámetros deben tener valores por defecto sensatos
2. Crear tratamiento `high_mpcr` con multiplicador = 2.0
3. Crear tratamiento `low_mpcr` con multiplicador = 1.2
4. El código debe funcionar aunque no se especifique un parámetro

---

### 💡 HINT (leer solo si llevas más de 15 minutos atascado)

<details>
<summary>Click para ver el hint</summary>

**Para acceder a parámetros de sesión en oTree 5:**

1. En `settings.py`, define los parámetros en cada SESSION_CONFIG:
```python
SESSION_CONFIGS = [
    dict(
        name='public_goods_high',
        display_name="Public Goods - High MPCR",
        app_sequence=['public_goods'],
        num_demo_participants=3,
        multiplier=2.0,  # Este es tu parámetro custom
        endowment=100,
    ),
]
```

2. En `__init__.py`, accede a los parámetros usando `session.config`:
```python
# En una función o método
multiplier = player.session.config.get('multiplier', C.MULTIPLIER)
```

3. Para usarlo en cálculos de grupo, hazlo en la función `set_payoffs`:
```python
def set_payoffs(group: Group):
    multiplier = group.session.config.get('multiplier', C.MULTIPLIER)
    # ... resto del cálculo
```

4. Usa `.get()` con valor por defecto para evitar errores si el parámetro no existe.

</details>

---

### ✅ SOLUCIÓN COMPLETA

<details>
<summary>Click para ver la solución completa</summary>

#### Modificaciones a `settings.py`

```python
from os import environ

# ============================================================================
# CONFIGURACIÓN DE SESIONES EXPERIMENTALES
# ============================================================================
# Aquí definimos los diferentes "tratamientos" del experimento.
# Cada dict es una configuración diferente que aparecerá en el menú de oTree.

SESSION_CONFIGS = [
    # ────────────────────────────────────────────────────────────────────────
    # TRATAMIENTO 1: MPCR ALTO
    # ────────────────────────────────────────────────────────────────────────
    # MPCR (Marginal Per Capita Return) = multiplicador / n_jugadores
    # Con multiplicador=2.0 y 3 jugadores: MPCR = 2.0/3 = 0.67
    # 
    # Interpretación económica:
    # - Por cada punto que contribuyes, el grupo recibe 2 puntos
    # - Pero como se divide entre 3, tú recibes 0.67 puntos de vuelta
    # - Incentivo a cooperar: MODERADO-ALTO
    dict(
        name='public_goods_high_mpcr',
        display_name="Public Goods - High MPCR (0.67)",
        app_sequence=['public_goods'],
        num_demo_participants=3,
        # Parámetros configurables del experimento
        endowment=100,           # Dotación inicial de cada jugador
        multiplier=2.0,          # Factor de multiplicación del fondo común
        players_per_group=3,     # Jugadores por grupo
        doc="""
        Tratamiento con MPCR alto (0.67).
        Predicción: Mayor cooperación que en low_mpcr.
        """
    ),
    
    # ────────────────────────────────────────────────────────────────────────
    # TRATAMIENTO 2: MPCR BAJO
    # ────────────────────────────────────────────────────────────────────────
    # Con multiplicador=1.2 y 3 jugadores: MPCR = 1.2/3 = 0.40
    # 
    # Interpretación económica:
    # - Por cada punto que contribuyes, el grupo recibe 1.2 puntos
    # - Dividido entre 3, tú recibes solo 0.40 puntos de vuelta
    # - Incentivo a cooperar: BAJO (mejor guardar los puntos)
    dict(
        name='public_goods_low_mpcr',
        display_name="Public Goods - Low MPCR (0.40)",
        app_sequence=['public_goods'],
        num_demo_participants=3,
        # Parámetros configurables del experimento
        endowment=100,
        multiplier=1.2,          # Multiplicador más bajo
        players_per_group=3,
        doc="""
        Tratamiento con MPCR bajo (0.40).
        Predicción: Menor cooperación que en high_mpcr.
        """
    ),
]

# ============================================================================
# CONFIGURACIÓN GENERAL
# ============================================================================

LANGUAGE_CODE = 'es'                    # Idioma de la interfaz
REAL_WORLD_CURRENCY_CODE = 'MXN'        # Moneda (para mostrar equivalencias)
USE_POINTS = True                       # Usar "puntos" en lugar de dinero real
POINTS_CUSTOM_NAME = 'puntos'           # Nombre personalizado para los puntos

# Configuración de administrador
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD', 'admin')

# Texto que aparece en la página de demo
DEMO_PAGE_INTRO_HTML = """
<h2>Taller Git/GitHub - Public Goods Game</h2>
<p>Este experimento tiene dos tratamientos:</p>
<ul>
    <li><strong>High MPCR (0.67):</strong> Multiplicador = 2.0</li>
    <li><strong>Low MPCR (0.40):</strong> Multiplicador = 1.2</li>
</ul>
<p>Referencia: Fehr & Gächter (2000)</p>
"""

SECRET_KEY = '{{ secret_key }}'
```

---

#### 📍 MOMENTO DE COMMIT #1
```bash
git add settings.py
git commit -m "feat(settings): agrega tratamientos high_mpcr y low_mpcr"
```

---

#### Modificaciones a `public_goods/__init__.py`

```python
from otree.api import *

doc = """
Public Goods Game con parámetros configurables.
Implementa tratamientos High MPCR y Low MPCR.
Referencia: Fehr & Gächter (2000)
"""


class C(BaseConstants):
    """
    CONSTANTES DEL JUEGO
    Estos son valores POR DEFECTO que se usan si no se especifica
    otro valor en la configuración de la sesión.
    """
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 2  # Valor por defecto: MPCR = 2/3 = 0.67


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    """
    GRUPO - Información compartida
    """
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    
    # Guardamos el multiplicador usado para referencia en resultados
    multiplier_used = models.FloatField()


class Player(BasePlayer):
    """
    JUGADOR - Información individual
    """
    contribution = models.CurrencyField(
        min=0,
        label="¿Cuánto quieres contribuir al fondo común?"
    )
    
    # Guardamos el MPCR del tratamiento para análisis posterior
    treatment_mpcr = models.FloatField()

    @staticmethod
    def contribution_max(player):
        """
        Define el máximo de contribución dinámicamente.
        Esto permite que el endowment sea configurable.
        """
        # Obtiene el endowment de la configuración, o usa el valor por defecto
        endowment = player.session.config.get('endowment', C.ENDOWMENT)
        return endowment


# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def get_config_value(session, key, default):
    """
    Obtiene un valor de configuración de forma segura.
    Si el parámetro no existe en la sesión, retorna el valor por defecto.
    
    Esto evita errores si alguien corre el experimento sin configurar
    todos los parámetros.
    """
    return session.config.get(key, default)


def calculate_mpcr(multiplier, n_players):
    """
    Calcula el MPCR (Marginal Per Capita Return).
    
    MPCR = multiplicador / número de jugadores
    
    Interpretación:
    - MPCR > 1: Contribuir siempre es rentable individualmente (raro en experimentos)
    - 1/n < MPCR < 1: Cooperar es socialmente óptimo pero individualmente costoso
    - MPCR < 1/n: Nunca conviene contribuir (ni social ni individualmente)
    
    En nuestro caso:
    - High MPCR: 2/3 = 0.67 (cooperar es socialmente óptimo)
    - Low MPCR: 1.2/3 = 0.40 (cooperar es socialmente óptimo pero menos atractivo)
    """
    return multiplier / n_players


# ============================================================================
# PÁGINAS
# ============================================================================

class Contribute(Page):
    """Página donde el jugador decide su contribución."""
    form_model = 'player'
    form_fields = ['contribution']
    
    @staticmethod
    def vars_for_template(player):
        """
        Pasa variables al template.
        Incluye los parámetros configurados para mostrarlos al participante.
        """
        session = player.session
        endowment = get_config_value(session, 'endowment', C.ENDOWMENT)
        multiplier = get_config_value(session, 'multiplier', C.MULTIPLIER)
        n_players = get_config_value(session, 'players_per_group', C.PLAYERS_PER_GROUP)
        mpcr = calculate_mpcr(multiplier, n_players)
        
        return dict(
            endowment=endowment,
            multiplier=multiplier,
            n_players=n_players,
            mpcr=round(mpcr, 2),  # Redondeamos para mostrar bonito
        )


class ResultsWaitPage(WaitPage):
    """Espera a que todos contribuyan antes de calcular payoffs."""
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """Muestra los resultados finales."""
    @staticmethod
    def vars_for_template(player):
        """Variables para el template de resultados."""
        session = player.session
        multiplier = get_config_value(session, 'multiplier', C.MULTIPLIER)
        n_players = get_config_value(session, 'players_per_group', C.PLAYERS_PER_GROUP)
        mpcr = calculate_mpcr(multiplier, n_players)
        
        return dict(
            multiplier=multiplier,
            mpcr=round(mpcr, 2),
            treatment_name=session.config.get('name', 'default'),
        )


# ============================================================================
# FUNCIONES DE GRUPO
# ============================================================================

def set_payoffs(group: Group):
    """
    Calcula los payoffs de todos los jugadores del grupo.
    
    Usa los parámetros de la configuración de sesión en lugar de
    las constantes hardcodeadas, lo que permite tener diferentes
    tratamientos experimentales.
    
    Fórmula:
    payoff_i = (endowment - contribution_i) + (Σcontributions × multiplier / n)
    """
    session = group.session
    
    # Obtener parámetros de la configuración (con valores por defecto)
    endowment = get_config_value(session, 'endowment', C.ENDOWMENT)
    multiplier = get_config_value(session, 'multiplier', C.MULTIPLIER)
    n_players = get_config_value(session, 'players_per_group', C.PLAYERS_PER_GROUP)
    
    # Guardar el multiplicador usado para referencia
    group.multiplier_used = multiplier
    
    # Calcular contribución total del grupo
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    
    # Calcular la parte individual del fondo común
    # (total × multiplicador) ÷ número de jugadores
    group.individual_share = (group.total_contribution * multiplier) / n_players
    
    # Calcular MPCR para guardarlo en cada jugador (útil para análisis)
    mpcr = calculate_mpcr(multiplier, n_players)
    
    # Asignar payoffs a cada jugador
    for p in players:
        p.treatment_mpcr = mpcr  # Guardar MPCR para análisis
        p.payoff = endowment - p.contribution + group.individual_share


page_sequence = [Contribute, ResultsWaitPage, Results]
```

---

#### 📍 MOMENTO DE COMMIT #2
```bash
git add public_goods/__init__.py
git commit -m "feat(public_goods): implementa parámetros configurables desde sesión

- Agrega get_config_value para manejo seguro de parámetros
- Agrega calculate_mpcr con documentación económica
- Modifica set_payoffs para usar parámetros de sesión
- Agrega vars_for_template para mostrar info del tratamiento"
```

---

#### Actualizar template `Contribute.html` (opcional pero recomendado)

```html
{{ block title }}
    Contribución al Fondo Común
{{ endblock }}

{{ block content }}
<div class="contribute-page">
    <!-- Muestra información del tratamiento actual -->
    <div class="info-box" style="background-color: #f0f8ff; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
        <h4>Información del Tratamiento</h4>
        <ul>
            <li><strong>Tu dotación:</strong> {{ endowment }} puntos</li>
            <li><strong>Jugadores en tu grupo:</strong> {{ n_players }}</li>
            <li><strong>Multiplicador:</strong> {{ multiplier }}</li>
            <li><strong>MPCR:</strong> {{ mpcr }}</li>
        </ul>
    </div>
    
    <p>
        Tienes <strong>{{ endowment }} puntos</strong>. 
        ¿Cuántos puntos quieres contribuir al fondo común?
    </p>
    
    <p>
        Las contribuciones se multiplicarán por <strong>{{ multiplier }}</strong> 
        y se dividirán equitativamente entre los {{ n_players }} jugadores.
    </p>
    
    {{ formfields }}
    
    {{ next_button }}
</div>
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #3
```bash
git add public_goods/templates/public_goods/Contribute.html
git commit -m "feat(templates): muestra info del tratamiento en página Contribute"
```

---

#### Subir cambios y crear Pull Request
```bash
git push -u origin feature/parametros-tratamientos
```

</details>

---

### Verificación local

```bash
# Iniciar servidor
otree devserver

# En navegador: http://localhost:8000
# Verificar que aparecen los dos tratamientos:
# - "Public Goods - High MPCR (0.67)"
# - "Public Goods - Low MPCR (0.40)"

# Probar cada tratamiento y verificar que:
# 1. El multiplicador mostrado es correcto
# 2. Los payoffs se calculan con el multiplicador correcto
```

---

## 3.3 MÓDULO 3: Sergio - Resultados con Visualización

### Objetivo
Crear una página de resultados mejorada que muestre gráficamente las contribuciones de cada jugador usando Chart.js, con una tabla detallada y desglose del cálculo de payoff.

### Flujo de trabajo Git

```bash
# 1. Asegurarse de estar en main actualizado
git checkout main
git pull origin main

# 2. Crear rama de feature
git checkout -b feature/resultados-graficos

# 3. Verificar que estás en la rama correcta
git branch
# Debe mostrar: * feature/resultados-graficos
```

### Prompt sugerido para IA

> **Modelo recomendado:** Claude Sonnet 4.5  
> **Justificación:** Esta tarea es principalmente de frontend (HTML + JavaScript) sin lógica compleja de backend. Sonnet es más rápido y suficiente para generar código de visualización con Chart.js.

```
Eres un desarrollador frontend experto en visualización de datos con Chart.js y oTree.

CONTEXTO:
Tengo un Public Goods Game en oTree 5. Necesito mejorar la página de resultados para mostrar:
1. Tabla con contribuciones de cada jugador (anonimizadas como "Jugador 1, 2, 3")
2. Gráfico de barras con las contribuciones
3. Desglose claro del cálculo de payoff

DATOS DISPONIBLES EN EL TEMPLATE:
- player.contribution: contribución del jugador actual
- group.total_contribution: suma de todas las contribuciones
- group.individual_share: parte que recibe cada jugador del fondo
- player.payoff: ganancia final del jugador

PARA OBTENER CONTRIBUCIONES DE OTROS JUGADORES:
En vars_for_template puedo pasar:
- Lista de contribuciones de todos los jugadores
- El índice del jugador actual (para destacarlo)

REQUISITOS:
1. Usar Chart.js desde CDN (no instalar paquetes)
2. El gráfico debe ser un bar chart horizontal o vertical
3. Destacar la barra del jugador actual en color diferente
4. La tabla debe mostrar contribución y si es "Tú" o "Otro jugador"
5. El desglose del cálculo debe ser paso a paso

RESTRICCIONES DE OTREE:
- Los templates usan sintaxis Django/Jinja2
- Para pasar datos a JavaScript, usar {{ variable|json }}
- No puedo usar módulos ES6, solo script tags tradicionales

OUTPUT:
1. Función vars_for_template completa para Results page
2. Template Results.html completo con:
   - Tabla de contribuciones
   - Gráfico Chart.js
   - Desglose del cálculo
   - CSS inline para estilizar
```

### Descripción de la tarea

**Archivos a modificar:**
- `public_goods/__init__.py` - Agregar `vars_for_template` a Results
- `public_goods/templates/public_goods/Results.html` - Rediseñar completamente

**Especificaciones:**
1. Tabla con contribuciones anonimizadas
2. Gráfico de barras con Chart.js
3. Destacar al jugador actual en la visualización
4. Mostrar fórmula y cálculo paso a paso

---

### 💡 HINT (leer solo si llevas más de 15 minutos atascado)

<details>
<summary>Click para ver el hint</summary>

**Para pasar datos de contribuciones a JavaScript:**

1. En `vars_for_template`, crea una lista de contribuciones:
```python
@staticmethod
def vars_for_template(player):
    group = player.group
    players = group.get_players()
    
    contributions = []
    for i, p in enumerate(players):
        contributions.append({
            'player_number': i + 1,
            'contribution': float(p.contribution),
            'is_self': p.id == player.id,
        })
    
    return dict(
        contributions=contributions,
        # ... otros datos
    )
```

2. En el template, pasa los datos a JavaScript:
```html
<script>
    const contributions = {{ contributions|json }};
    // Ahora puedes usar 'contributions' en JavaScript
</script>
```

3. Para Chart.js, incluye el CDN:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

4. Para destacar al jugador actual, usa colores diferentes:
```javascript
const colors = contributions.map(c => 
    c.is_self ? '#4CAF50' : '#2196F3'
);
```

</details>

---

### ✅ SOLUCIÓN COMPLETA

<details>
<summary>Click para ver la solución completa</summary>

#### Modificaciones a `public_goods/__init__.py`

Reemplazar la clase Results:

```python
class Results(Page):
    """
    PÁGINA DE RESULTADOS CON VISUALIZACIÓN
    Muestra los resultados del juego con gráficos y desglose detallado.
    """
    @staticmethod
    def vars_for_template(player):
        """
        Prepara todos los datos necesarios para la visualización.
        Esto incluye datos para la tabla, el gráfico y el cálculo.
        """
        group = player.group
        session = player.session
        
        # Obtener parámetros de configuración
        endowment = session.config.get('endowment', C.ENDOWMENT)
        multiplier = session.config.get('multiplier', C.MULTIPLIER)
        n_players = session.config.get('players_per_group', C.PLAYERS_PER_GROUP)
        
        # ────────────────────────────────────────────────────────────────
        # Preparar datos de contribuciones para tabla y gráfico
        # ────────────────────────────────────────────────────────────────
        players_in_group = group.get_players()
        contributions_data = []
        
        for i, p in enumerate(players_in_group):
            contributions_data.append({
                'player_number': i + 1,
                'contribution': float(p.contribution),
                'is_self': p.id == player.id,  # True si es el jugador actual
                'label': 'Tú' if p.id == player.id else f'Jugador {i + 1}',
            })
        
        # Ordenar por número de jugador para consistencia
        contributions_data.sort(key=lambda x: x['player_number'])
        
        # ────────────────────────────────────────────────────────────────
        # Calcular desglose paso a paso del payoff
        # ────────────────────────────────────────────────────────────────
        kept = float(endowment - player.contribution)       # Lo que no contribuí
        total_contributed = float(group.total_contribution) # Total del grupo
        multiplied_fund = total_contributed * multiplier    # Fondo multiplicado
        share_from_fund = float(group.individual_share)     # Mi parte del fondo
        final_payoff = float(player.payoff)                 # Ganancia final
        
        # ────────────────────────────────────────────────────────────────
        # Datos específicos para Chart.js
        # ────────────────────────────────────────────────────────────────
        chart_labels = [d['label'] for d in contributions_data]
        chart_values = [d['contribution'] for d in contributions_data]
        # Verde para el jugador actual, azul para los demás
        chart_colors = ['#4CAF50' if d['is_self'] else '#2196F3' for d in contributions_data]
        
        return dict(
            # Parámetros del juego
            endowment=endowment,
            multiplier=multiplier,
            n_players=n_players,
            
            # Datos de contribuciones (para la tabla)
            contributions_data=contributions_data,
            
            # Desglose del cálculo
            my_contribution=float(player.contribution),
            kept=kept,
            total_contributed=total_contributed,
            multiplied_fund=multiplied_fund,
            share_from_fund=share_from_fund,
            final_payoff=final_payoff,
            
            # Datos para Chart.js (en formato que JavaScript entiende)
            chart_labels=chart_labels,
            chart_values=chart_values,
            chart_colors=chart_colors,
        )
```

---

#### 📍 MOMENTO DE COMMIT #1
```bash
git add public_goods/__init__.py
git commit -m "feat(Results): agrega vars_for_template con datos para visualización"
```

---

#### Template: `Results.html`

Reemplazar completamente `public_goods/templates/public_goods/Results.html`:

```html
{{ block title }}
    Resultados
{{ endblock }}

{{ block styles }}
<!-- Estilos personalizados para la página de resultados -->
<style>
    .results-container {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .section {
        background-color: #f9f9f9;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .section h3 {
        margin-top: 0;
        color: #333;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 10px;
    }
    
    /* Estilos para la tabla */
    .contributions-table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    
    .contributions-table th,
    .contributions-table td {
        padding: 12px;
        text-align: center;
        border: 1px solid #ddd;
    }
    
    .contributions-table th {
        background-color: #4CAF50;
        color: white;
    }
    
    /* Destacar la fila del jugador actual */
    .contributions-table tr.is-self {
        background-color: #E8F5E9;
        font-weight: bold;
    }
    
    .contributions-table tr:hover {
        background-color: #f5f5f5;
    }
    
    /* Contenedor del gráfico */
    .chart-container {
        position: relative;
        height: 300px;
        margin: 20px 0;
    }
    
    /* Estilos para el desglose del cálculo */
    .calculation-step {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px dashed #ddd;
    }
    
    .calculation-step:last-child {
        border-bottom: none;
        font-weight: bold;
        font-size: 1.2em;
        color: #4CAF50;
    }
    
    .calculation-step .label {
        color: #666;
    }
    
    .calculation-step .value {
        font-weight: bold;
    }
    
    /* Caja de información destacada */
    .highlight-box {
        background-color: #E3F2FD;
        border-left: 4px solid #2196F3;
        padding: 15px;
        margin: 15px 0;
    }
    
    /* Caja de ganancia final */
    .final-payoff {
        font-size: 1.5em;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #4CAF50, #8BC34A);
        color: white;
        border-radius: 8px;
        margin-top: 20px;
    }
</style>
{{ endblock }}

{{ block content }}
<div class="results-container">
    
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- SECCIÓN 1: RESUMEN DEL GRUPO -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="section">
        <h3>📊 Resumen del Grupo</h3>
        <div class="highlight-box">
            <p>
                <strong>Total contribuido por el grupo:</strong> {{ total_contributed }} puntos<br>
                <strong>Fondo después de multiplicar (×{{ multiplier }}):</strong> {{ multiplied_fund }} puntos<br>
                <strong>Parte de cada jugador:</strong> {{ share_from_fund }} puntos
            </p>
        </div>
    </div>
    
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- SECCIÓN 2: TABLA DE CONTRIBUCIONES -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="section">
        <h3>👥 Contribuciones del Grupo</h3>
        <table class="contributions-table">
            <thead>
                <tr>
                    <th>Jugador</th>
                    <th>Contribución</th>
                    <th>Puntos Guardados</th>
                </tr>
            </thead>
            <tbody>
                <!-- Iteramos sobre cada jugador -->
                {{ for item in contributions_data }}
                <tr class="{{ if item.is_self }}is-self{{ endif }}">
                    <td>{{ item.label }}</td>
                    <td>{{ item.contribution }} puntos</td>
                    <td>{{ endowment }} - {{ item.contribution }} = {{ endowment|subtract:item.contribution }} puntos</td>
                </tr>
                {{ endfor }}
            </tbody>
        </table>
    </div>
    
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- SECCIÓN 3: GRÁFICO DE CONTRIBUCIONES -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="section">
        <h3>📈 Visualización de Contribuciones</h3>
        <div class="chart-container">
            <canvas id="contributionsChart"></canvas>
        </div>
        <p style="text-align: center; color: #666; font-size: 0.9em;">
            <span style="color: #4CAF50;">■</span> Tu contribución &nbsp;&nbsp;
            <span style="color: #2196F3;">■</span> Otros jugadores
        </p>
    </div>
    
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- SECCIÓN 4: DESGLOSE DEL CÁLCULO -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="section">
        <h3>🧮 Cálculo de tu Ganancia</h3>
        
        <div class="calculation-step">
            <span class="label">Tu dotación inicial:</span>
            <span class="value">{{ endowment }} puntos</span>
        </div>
        
        <div class="calculation-step">
            <span class="label">Tu contribución al fondo:</span>
            <span class="value">- {{ my_contribution }} puntos</span>
        </div>
        
        <div class="calculation-step">
            <span class="label">Puntos que guardaste:</span>
            <span class="value">= {{ kept }} puntos</span>
        </div>
        
        <div class="calculation-step">
            <span class="label">Tu parte del fondo común:</span>
            <span class="value">+ {{ share_from_fund }} puntos</span>
        </div>
        
        <div class="calculation-step">
            <span class="label">TU GANANCIA FINAL:</span>
            <span class="value">{{ final_payoff }} puntos</span>
        </div>
    </div>
    
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <!-- GANANCIA FINAL DESTACADA -->
    <!-- ═══════════════════════════════════════════════════════════════════ -->
    <div class="final-payoff">
        🎉 Tu ganancia en esta ronda: <strong>{{ player.payoff }}</strong>
    </div>

</div>

{{ next_button }}
{{ endblock }}

{{ block scripts }}
<!-- Cargar Chart.js desde CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
    // ═══════════════════════════════════════════════════════════════════════
    // CONFIGURACIÓN DEL GRÁFICO
    // ═══════════════════════════════════════════════════════════════════════
    
    // Datos pasados desde Python usando el filtro |json
    const labels = {{ chart_labels|json }};
    const values = {{ chart_values|json }};
    const colors = {{ chart_colors|json }};
    
    // Obtener el contexto del canvas
    const ctx = document.getElementById('contributionsChart').getContext('2d');
    
    // Crear el gráfico de barras
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Contribución (puntos)',
                data: values,
                backgroundColor: colors,
                borderColor: colors.map(c => c),
                borderWidth: 2,
                borderRadius: 5,  // Esquinas redondeadas
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false  // Ocultamos la leyenda default
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.parsed.y + ' puntos';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: {{ endowment }},  // El máximo es la dotación
                    title: {
                        display: true,
                        text: 'Puntos Contribuidos'
                    },
                    ticks: {
                        stepSize: 20
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Jugadores'
                    }
                }
            }
        }
    });
</script>
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #2
```bash
git add public_goods/templates/public_goods/Results.html
git commit -m "feat(Results): rediseña página con tabla, gráfico Chart.js y desglose

- Agrega tabla de contribuciones con destacado del jugador actual
- Integra gráfico de barras con Chart.js desde CDN
- Muestra desglose paso a paso del cálculo de payoff
- Incluye CSS personalizado para mejor presentación"
```

---

#### Subir cambios y crear Pull Request
```bash
git push -u origin feature/resultados-graficos
```

</details>

---

### Verificación local

```bash
# Iniciar servidor
otree devserver

# En navegador: http://localhost:8000
# Completar el flujo del juego hasta Results
# Verificar:
# 1. La tabla muestra todas las contribuciones
# 2. Tu fila está destacada en verde claro
# 3. El gráfico renderiza correctamente
# 4. El desglose del cálculo es correcto
```

---

## 3.4 MÓDULO 4: Donovan - Sistema de Castigo (Punishment)

### Objetivo
Implementar una etapa de castigo después de ver los resultados iniciales, donde los participantes pueden pagar para reducir el payoff de otros jugadores, siguiendo el diseño de Fehr & Gächter (2000).

### Flujo de trabajo Git

```bash
# 1. Asegurarse de estar en main actualizado
git checkout main
git pull origin main

# 2. Crear rama de feature
git checkout -b feature/sistema-castigo

# 3. Verificar que estás en la rama correcta
git branch
# Debe mostrar: * feature/sistema-castigo
```

### Prompt sugerido para IA

> **Modelo recomendado:** Claude Opus 4.5  
> **Justificación:** Esta es la tarea más compleja del taller: requiere crear nuevas páginas, modificar la lógica de payoffs, manejar interacciones entre jugadores, y mantener coherencia con el diseño experimental de Fehr & Gächter. Opus 4.5 es superior para tareas multi-archivo con lógica compleja.

```
Eres un economista experimental y desarrollador oTree experto. Tu tarea es implementar el mecanismo de castigo del paper de Fehr & Gächter (2000).

CONTEXTO:
Tengo un Public Goods Game funcionando en oTree 5 con:
- 3 jugadores por grupo
- Dotación de 100 puntos
- Multiplicador configurable (1.2 o 2.0)
- Páginas: Contribute -> ResultsWaitPage -> Results

OBJETIVO:
Agregar una etapa de castigo entre los resultados iniciales y los resultados finales.

DISEÑO DEL CASTIGO (Fehr & Gächter 2000):
1. Después de ver las contribuciones de todos, cada jugador puede asignar "puntos de castigo" a otros jugadores
2. COSTO: Cada punto de castigo cuesta 1 unidad al que castiga
3. EFECTO: Cada punto de castigo reduce 3 unidades al castigado
4. ANONIMATO: Los jugadores no saben quién los castigó
5. LÍMITE: Máximo 10 puntos de castigo por jugador castigado

FLUJO NUEVO:
Contribute -> ResultsWaitPage -> IntermediateResults -> Punishment -> PunishmentWaitPage -> FinalResults

REQUISITOS TÉCNICOS:
1. En IntermediateResults: mostrar contribuciones (sin payoff final aún)
2. En Punishment: interfaz para asignar puntos de castigo a cada otro jugador
3. Necesito campos para:
   - punishment_sent_to_player_X (cuánto castigué a cada uno)
   - punishment_received (total que me castigaron)
   - cost_of_punishment (cuánto gasté castigando)
4. En FinalResults: mostrar payoff final = payoff_inicial - costo_castigo - castigo_recibido*3

CONSIDERACIONES:
- El castigo debe ser a jugadores identificados por número, no por nombre real
- Debo poder identificar a cada jugador sin revelar identidades
- Usar player.id_in_group para identificar jugadores (1, 2, 3)

OUTPUT ESPERADO:
1. Campos nuevos para Player
2. Código completo de las nuevas páginas
3. Templates para IntermediateResults, Punishment, y FinalResults
4. Función para calcular payoffs finales con castigo
5. page_sequence actualizado

Incluye comentarios que expliquen la lógica económica del mecanismo.
```

### Descripción de la tarea

**Archivos a crear/modificar:**
- `public_goods/__init__.py` - Agregar campos, páginas y lógica de castigo
- `public_goods/templates/public_goods/IntermediateResults.html` - Nuevo
- `public_goods/templates/public_goods/Punishment.html` - Nuevo
- `public_goods/templates/public_goods/FinalResults.html` - Nuevo

**Especificaciones:**
1. Ratio de castigo: 1:3 (cuesta 1, reduce 3)
2. Máximo 10 puntos de castigo por jugador
3. El castigo es anónimo
4. Mostrar claramente el impacto del castigo en el payoff final

---

### 💡 HINT (leer solo si llevas más de 15 minutos atascado)

<details>
<summary>Click para ver el hint</summary>

**Para manejar castigo entre jugadores en oTree 5:**

1. **Para el castigo enviado**, necesitas campos dinámicos. Una forma es usar campos separados:
```python
class Player(BasePlayer):
    # Castigo enviado a cada posición (no a IDs específicos)
    punishment_sent_1 = models.IntegerField(min=0, max=10, initial=0)
    punishment_sent_2 = models.IntegerField(min=0, max=10, initial=0)
    # (Para 3 jugadores, solo necesitas castigar a 2 otros)
```

2. **Para identificar a quién castigar**, mapea posiciones:
```python
@staticmethod
def vars_for_template(player):
    others = player.get_others_in_group()
    other_players_info = []
    for p in others:
        other_players_info.append({
            'id_in_group': p.id_in_group,
            'contribution': p.contribution,
        })
    return dict(others=other_players_info)
```

3. **Para calcular castigo recibido**, itera sobre el grupo:
```python
def calculate_punishment(group):
    players = group.get_players()
    for p in players:
        received = 0
        for other in p.get_others_in_group():
            # Obtener cuánto 'other' castigó a 'p'
            field_name = f'punishment_to_{p.id_in_group}'
            received += getattr(other, field_name, 0)
        p.punishment_received = received
```

4. **Alternativa más limpia**: Usa un campo JSON o ExtraModel para almacenar la matriz de castigo.

</details>

---

### ✅ SOLUCIÓN COMPLETA

<details>
<summary>Click para ver la solución completa</summary>

#### Modificaciones completas a `public_goods/__init__.py`

```python
from otree.api import *

doc = """
Public Goods Game con castigo (punishment).
Basado en Fehr & Gächter (2000): "Cooperation and Punishment in Public Goods Experiments"

Diseño del castigo:
- Costo: 1 punto por cada punto de castigo asignado
- Efecto: 3 puntos de reducción por cada punto recibido
- Ratio 1:3 es estándar en la literatura experimental
"""


class C(BaseConstants):
    """
    CONSTANTES DEL JUEGO
    Incluye parámetros del castigo además de los básicos.
    """
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 2
    
    # ═══════════════════════════════════════════════════════════════════════
    # PARÁMETROS DEL CASTIGO (Fehr & Gächter, 2000)
    # ═══════════════════════════════════════════════════════════════════════
    PUNISHMENT_COST = 1      # Lo que cuesta cada punto de castigo al castigador
    PUNISHMENT_EFFECT = 3    # Lo que pierde el castigado por cada punto recibido
    MAX_PUNISHMENT = 10      # Máximo de puntos de castigo que puedes dar a un jugador


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    """
    GRUPO - Información compartida
    """
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    """
    JUGADOR - Información individual
    Incluye campos para contribución, comprensión y castigo.
    """
    # Campo de contribución
    contribution = models.CurrencyField(
        min=0,
        max=C.ENDOWMENT,
        label="¿Cuánto quieres contribuir al fondo común?"
    )
    
    # Campos de comprensión (del módulo de Mauricio)
    comp_q1 = models.IntegerField(
        label="¿Cuántos puntos recibe cada jugador al inicio?"
    )
    comp_q2 = models.IntegerField(
        label="Si todos contribuyen 50 puntos, ¿cuánto habrá en el fondo antes de multiplicar?",
        choices=[[50, '50'], [100, '100'], [150, '150'], [200, '200']]
    )
    comp_q3 = models.IntegerField(
        label="Si el fondo multiplicado tiene 300 puntos, ¿cuánto recibe cada jugador?",
        choices=[[50, '50'], [100, '100'], [150, '150'], [300, '300']]
    )
    
    # ═══════════════════════════════════════════════════════════════════════
    # CAMPOS DE CASTIGO
    # ═══════════════════════════════════════════════════════════════════════
    
    # Payoff antes del castigo (para mostrar el desglose)
    intermediate_payoff = models.CurrencyField()
    
    # Castigo enviado a cada jugador (por su id_in_group: 1, 2, o 3)
    # Necesitamos un campo para cada posible jugador en el grupo
    punishment_to_1 = models.IntegerField(
        min=0, max=C.MAX_PUNISHMENT, initial=0,
        label="Puntos de castigo para Jugador 1"
    )
    punishment_to_2 = models.IntegerField(
        min=0, max=C.MAX_PUNISHMENT, initial=0,
        label="Puntos de castigo para Jugador 2"
    )
    punishment_to_3 = models.IntegerField(
        min=0, max=C.MAX_PUNISHMENT, initial=0,
        label="Puntos de castigo para Jugador 3"
    )
    
    # Totales (calculados automáticamente)
    total_punishment_sent = models.IntegerField(initial=0)      # Total que envié
    total_punishment_received = models.IntegerField(initial=0)  # Total que recibí
    cost_of_punishment = models.CurrencyField(initial=0)        # Costo de castigar
    punishment_deduction = models.CurrencyField(initial=0)      # Reducción por ser castigado


# ═══════════════════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════════════════════

def get_punishment_to(player, target_id):
    """
    Obtiene cuánto castigo envió 'player' al jugador con 'target_id'.
    target_id es el id_in_group (1, 2, o 3).
    """
    field_name = f'punishment_to_{target_id}'
    return getattr(player, field_name, 0)


def set_payoffs(group: Group):
    """
    Calcula payoffs INTERMEDIOS (antes del castigo).
    Esta función se ejecuta después de la contribución.
    """
    session = group.session
    endowment = session.config.get('endowment', C.ENDOWMENT)
    multiplier = session.config.get('multiplier', C.MULTIPLIER)
    n_players = session.config.get('players_per_group', C.PLAYERS_PER_GROUP)
    
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (group.total_contribution * multiplier) / n_players
    
    # Guardar payoff intermedio (antes del castigo)
    for p in players:
        p.intermediate_payoff = endowment - p.contribution + group.individual_share


def calculate_final_payoffs(group: Group):
    """
    Calcula payoffs FINALES incluyendo el castigo.
    
    Fórmula:
    Payoff Final = Payoff Intermedio 
                   - (Puntos de castigo enviados × PUNISHMENT_COST)
                   - (Puntos de castigo recibidos × PUNISHMENT_EFFECT)
    
    Ejemplo:
    - Si envié 5 puntos de castigo: pierdo 5 × 1 = 5 puntos
    - Si recibí 3 puntos de castigo: pierdo 3 × 3 = 9 puntos
    """
    players = group.get_players()
    
    # ───────────────────────────────────────────────────────────────────────
    # Paso 1: Calcular castigo enviado y recibido para cada jugador
    # ───────────────────────────────────────────────────────────────────────
    for player in players:
        # Calcular total de castigo enviado por este jugador
        sent = 0
        for other in player.get_others_in_group():
            sent += get_punishment_to(player, other.id_in_group)
        player.total_punishment_sent = sent
        player.cost_of_punishment = sent * C.PUNISHMENT_COST
        
        # Calcular total de castigo recibido por este jugador
        received = 0
        for other in player.get_others_in_group():
            received += get_punishment_to(other, player.id_in_group)
        player.total_punishment_received = received
        player.punishment_deduction = received * C.PUNISHMENT_EFFECT
    
    # ───────────────────────────────────────────────────────────────────────
    # Paso 2: Calcular payoff final
    # ───────────────────────────────────────────────────────────────────────
    for player in players:
        player.payoff = (
            player.intermediate_payoff 
            - player.cost_of_punishment 
            - player.punishment_deduction
        )
        # Asegurar que el payoff no sea negativo
        if player.payoff < 0:
            player.payoff = cu(0)


# ═══════════════════════════════════════════════════════════════════════════
# PÁGINAS
# ═══════════════════════════════════════════════════════════════════════════

class Introduction(Page):
    """Página de instrucciones."""
    pass


class Comprehension(Page):
    """Preguntas de comprensión."""
    form_model = 'player'
    form_fields = ['comp_q1', 'comp_q2', 'comp_q3']
    
    @staticmethod
    def error_message(player, values):
        solutions = {'comp_q1': 100, 'comp_q2': 150, 'comp_q3': 100}
        errors = []
        for field, correct in solutions.items():
            if values[field] != correct:
                errors.append(f"Revisa tu respuesta.")
        if errors:
            return ' '.join(errors)


class Contribute(Page):
    """Página de contribución."""
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    """Espera a que todos contribuyan."""
    after_all_players_arrive = set_payoffs


class IntermediateResults(Page):
    """
    RESULTADOS INTERMEDIOS
    Muestra las contribuciones ANTES de la etapa de castigo.
    Aquí los jugadores ven qué contribuyó cada uno.
    """
    @staticmethod
    def vars_for_template(player):
        group = player.group
        session = player.session
        
        multiplier = session.config.get('multiplier', C.MULTIPLIER)
        
        # Información de todos los jugadores
        players_info = []
        for p in group.get_players():
            players_info.append({
                'id': p.id_in_group,
                'contribution': float(p.contribution),
                'is_self': p.id == player.id,
                'label': 'Tú' if p.id == player.id else f'Jugador {p.id_in_group}',
            })
        
        return dict(
            players_info=players_info,
            total_contribution=group.total_contribution,
            multiplied_fund=float(group.total_contribution) * multiplier,
            individual_share=group.individual_share,
            intermediate_payoff=player.intermediate_payoff,
            multiplier=multiplier,
            punishment_cost=C.PUNISHMENT_COST,
            punishment_effect=C.PUNISHMENT_EFFECT,
            max_punishment=C.MAX_PUNISHMENT,
        )


class Punishment(Page):
    """
    PÁGINA DE CASTIGO
    Cada jugador decide cuántos puntos de castigo asignar a los otros.
    """
    form_model = 'player'
    
    @staticmethod
    def get_form_fields(player):
        """
        Genera dinámicamente los campos de formulario.
        Solo muestra campos para los OTROS jugadores (no para ti mismo).
        """
        others = player.get_others_in_group()
        return [f'punishment_to_{p.id_in_group}' for p in others]
    
    @staticmethod
    def vars_for_template(player):
        """Variables para mostrar información de los otros jugadores."""
        others = player.get_others_in_group()
        others_info = []
        for p in others:
            others_info.append({
                'id': p.id_in_group,
                'contribution': float(p.contribution),
                'field_name': f'punishment_to_{p.id_in_group}',
            })
        
        return dict(
            others_info=others_info,
            my_intermediate_payoff=player.intermediate_payoff,
            punishment_cost=C.PUNISHMENT_COST,
            punishment_effect=C.PUNISHMENT_EFFECT,
            max_punishment=C.MAX_PUNISHMENT,
        )
    
    @staticmethod
    def error_message(player, values):
        """
        Valida que el jugador tenga suficientes puntos para castigar.
        No puedes gastar más de lo que tienes.
        """
        total_punishment = sum(values.values())
        cost = total_punishment * C.PUNISHMENT_COST
        
        if cost > player.intermediate_payoff:
            return f'No tienes suficientes puntos. El costo total ({cost}) excede tu payoff ({player.intermediate_payoff}).'


class PunishmentWaitPage(WaitPage):
    """Espera a que todos decidan su castigo."""
    after_all_players_arrive = calculate_final_payoffs


class FinalResults(Page):
    """
    RESULTADOS FINALES
    Muestra el payoff final después del castigo con desglose completo.
    """
    @staticmethod
    def vars_for_template(player):
        group = player.group
        
        # Info de todos los jugadores para la tabla comparativa
        players_final = []
        for p in group.get_players():
            players_final.append({
                'id': p.id_in_group,
                'contribution': float(p.contribution),
                'intermediate_payoff': float(p.intermediate_payoff),
                'punishment_sent': p.total_punishment_sent,
                'punishment_received': p.total_punishment_received,
                'cost': float(p.cost_of_punishment),
                'deduction': float(p.punishment_deduction),
                'final_payoff': float(p.payoff),
                'is_self': p.id == player.id,
            })
        
        return dict(
            players_final=players_final,
            intermediate_payoff=player.intermediate_payoff,
            punishment_sent=player.total_punishment_sent,
            punishment_received=player.total_punishment_received,
            cost_of_punishment=player.cost_of_punishment,
            punishment_deduction=player.punishment_deduction,
            final_payoff=player.payoff,
            punishment_cost_ratio=C.PUNISHMENT_COST,
            punishment_effect_ratio=C.PUNISHMENT_EFFECT,
        )


# Página legacy (no se usa pero se mantiene por compatibilidad)
class Results(Page):
    @staticmethod
    def is_displayed(player):
        return False


# ═══════════════════════════════════════════════════════════════════════════
# SECUENCIA DE PÁGINAS
# ═══════════════════════════════════════════════════════════════════════════
page_sequence = [
    Introduction,
    Comprehension,
    Contribute,
    ResultsWaitPage,
    IntermediateResults,    # Nuevo: muestra contribuciones
    Punishment,              # Nuevo: decisión de castigo
    PunishmentWaitPage,      # Nuevo: espera para calcular
    FinalResults,            # Nuevo: resultados finales con castigo
]
```

---

#### 📍 MOMENTO DE COMMIT #1
```bash
git add public_goods/__init__.py
git commit -m "feat(punishment): implementa sistema de castigo Fehr-Gächter

- Agrega constantes PUNISHMENT_COST, PUNISHMENT_EFFECT, MAX_PUNISHMENT
- Agrega campos punishment_to_X para castigo entre jugadores
- Implementa calculate_final_payoffs con lógica de castigo
- Agrega páginas IntermediateResults, Punishment, FinalResults"
```

---

#### Template: `IntermediateResults.html`

```html
{{ block title }}
    Resultados de Contribuciones
{{ endblock }}

{{ block styles }}
<style>
    .results-box {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
    }
    .highlight {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 15px;
        margin: 15px 0;
    }
    .warning-box {
        background: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 15px;
        margin: 15px 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    th, td {
        padding: 12px;
        text-align: center;
        border: 1px solid #ddd;
    }
    th {
        background: #4caf50;
        color: white;
    }
    tr.is-self {
        background: #e8f5e9;
        font-weight: bold;
    }
</style>
{{ endblock }}

{{ block content }}
<div class="results-box">
    <h3>📊 Contribuciones del Grupo</h3>
    
    <table>
        <thead>
            <tr>
                <th>Jugador</th>
                <th>Contribución</th>
            </tr>
        </thead>
        <tbody>
            {{ for p in players_info }}
            <tr class="{{ if p.is_self }}is-self{{ endif }}">
                <td>{{ p.label }}</td>
                <td>{{ p.contribution }} puntos</td>
            </tr>
            {{ endfor }}
        </tbody>
    </table>
    
    <div class="highlight">
        <strong>Total contribuido:</strong> {{ total_contribution }}<br>
        <strong>Fondo multiplicado (×{{ multiplier }}):</strong> {{ multiplied_fund }} puntos<br>
        <strong>Tu parte del fondo:</strong> {{ individual_share }}
    </div>
    
    <p><strong>Tu payoff hasta ahora:</strong> {{ intermediate_payoff }}</p>
</div>

<div class="warning-box">
    <h4>⚠️ Etapa de Castigo</h4>
    <p>A continuación podrás <strong>castigar</strong> a otros jugadores si lo deseas.</p>
    <ul>
        <li><strong>Costo:</strong> Cada punto de castigo te cuesta {{ punishment_cost }} punto</li>
        <li><strong>Efecto:</strong> Cada punto reduce {{ punishment_effect }} puntos al castigado</li>
        <li><strong>Máximo:</strong> Hasta {{ max_punishment }} puntos por jugador</li>
        <li><strong>Anónimo:</strong> Nadie sabrá quién lo castigó</li>
    </ul>
</div>

{{ next_button }}
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #2
```bash
git add public_goods/templates/public_goods/IntermediateResults.html
git commit -m "feat(templates): crea IntermediateResults con info de castigo"
```

---

#### Template: `Punishment.html`

```html
{{ block title }}
    Etapa de Castigo
{{ endblock }}

{{ block styles }}
<style>
    .punishment-container {
        max-width: 600px;
        margin: 0 auto;
    }
    .player-card {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
        border-left: 4px solid #2196f3;
    }
    .info-box {
        background: #e3f2fd;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .cost-warning {
        color: #d32f2f;
        font-size: 0.9em;
        margin-top: 5px;
    }
    input[type="number"] {
        width: 80px;
        padding: 8px;
        font-size: 16px;
        text-align: center;
    }
</style>
{{ endblock }}

{{ block content }}
<div class="punishment-container">
    <div class="info-box">
        <p><strong>Tu payoff actual:</strong> {{ my_intermediate_payoff }}</p>
        <p>
            Cada punto de castigo te cuesta <strong>{{ punishment_cost }}</strong> 
            y reduce <strong>{{ punishment_effect }}</strong> puntos al castigado.
        </p>
    </div>
    
    <h3>¿Deseas castigar a algún jugador?</h3>
    <p><em>Puedes dejar en 0 si no deseas castigar.</em></p>
    
    {{ for other in others_info }}
    <div class="player-card">
        <h4>Jugador {{ other.id }}</h4>
        <p>Contribuyó: <strong>{{ other.contribution }} puntos</strong></p>
        
        <label>Puntos de castigo (0-{{ max_punishment }}):</label>
        {{ formfield other.field_name }}
        
        <p class="cost-warning">
            Costo para ti: <span id="cost_{{ other.id }}">0</span> puntos
        </p>
    </div>
    {{ endfor }}
    
    <div style="background: #ffebee; padding: 15px; border-radius: 5px; margin-top: 20px;">
        <strong>Costo total:</strong> <span id="total_cost">0</span> puntos
    </div>
    
    {{ next_button }}
</div>
{{ endblock }}

{{ block scripts }}
<script>
    // Actualizar costos en tiempo real
    const costPerPoint = {{ punishment_cost }};
    const inputs = document.querySelectorAll('input[type="number"]');
    
    function updateCosts() {
        let total = 0;
        inputs.forEach(input => {
            const value = parseInt(input.value) || 0;
            const playerId = input.name.split('_').pop();
            const costSpan = document.getElementById('cost_' + playerId);
            if (costSpan) {
                costSpan.textContent = value * costPerPoint;
            }
            total += value * costPerPoint;
        });
        document.getElementById('total_cost').textContent = total;
    }
    
    inputs.forEach(input => input.addEventListener('input', updateCosts));
    updateCosts();
</script>
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #3
```bash
git add public_goods/templates/public_goods/Punishment.html
git commit -m "feat(templates): crea Punishment con cálculo dinámico de costos"
```

---

#### Template: `FinalResults.html`

```html
{{ block title }}
    Resultados Finales
{{ endblock }}

{{ block styles }}
<style>
    .final-container {
        max-width: 800px;
        margin: 0 auto;
    }
    .section {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
    }
    .section h3 {
        margin-top: 0;
        border-bottom: 2px solid #4caf50;
        padding-bottom: 10px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
    }
    th, td {
        padding: 10px;
        text-align: center;
        border: 1px solid #ddd;
    }
    th {
        background: #4caf50;
        color: white;
    }
    tr.is-self {
        background: #e8f5e9;
        font-weight: bold;
    }
    .calc-row {
        display: flex;
        justify-content: space-between;
        padding: 10px 0;
        border-bottom: 1px dashed #ddd;
    }
    .calc-row:last-child {
        border-bottom: none;
        font-weight: bold;
        font-size: 1.2em;
        color: #4caf50;
    }
    .calc-row.negative {
        color: #d32f2f;
    }
    .final-payoff-box {
        background: linear-gradient(135deg, #4caf50, #8bc34a);
        color: white;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    .final-payoff-box h2 {
        margin: 0;
        font-size: 2em;
    }
</style>
{{ endblock }}

{{ block content }}
<div class="final-container">
    
    <!-- Tabla resumen -->
    <div class="section">
        <h3>📊 Resumen del Grupo</h3>
        <table>
            <thead>
                <tr>
                    <th>Jugador</th>
                    <th>Contribución</th>
                    <th>Castigo Enviado</th>
                    <th>Castigo Recibido</th>
                    <th>Payoff Final</th>
                </tr>
            </thead>
            <tbody>
                {{ for p in players_final }}
                <tr class="{{ if p.is_self }}is-self{{ endif }}">
                    <td>{{ if p.is_self }}Tú{{ else }}Jugador {{ p.id }}{{ endif }}</td>
                    <td>{{ p.contribution }}</td>
                    <td>{{ p.punishment_sent }} (costo: {{ p.cost }})</td>
                    <td>{{ p.punishment_received }} (deducción: {{ p.deduction }})</td>
                    <td><strong>{{ p.final_payoff }}</strong></td>
                </tr>
                {{ endfor }}
            </tbody>
        </table>
    </div>
    
    <!-- Desglose personal -->
    <div class="section">
        <h3>🧮 Tu Cálculo Detallado</h3>
        
        <div class="calc-row">
            <span>Payoff intermedio:</span>
            <span>{{ intermediate_payoff }}</span>
        </div>
        
        <div class="calc-row negative">
            <span>Costo de castigo enviado ({{ punishment_sent }} × {{ punishment_cost_ratio }}):</span>
            <span>- {{ cost_of_punishment }}</span>
        </div>
        
        <div class="calc-row negative">
            <span>Deducción por castigo recibido ({{ punishment_received }} × {{ punishment_effect_ratio }}):</span>
            <span>- {{ punishment_deduction }}</span>
        </div>
        
        <div class="calc-row">
            <span>TU PAYOFF FINAL:</span>
            <span>{{ final_payoff }}</span>
        </div>
    </div>
    
    <!-- Info del castigo -->
    <div class="section">
        <h3>📝 Información del Castigo</h3>
        <ul>
            <li><strong>Castigo que enviaste:</strong> {{ punishment_sent }} puntos (te costó {{ cost_of_punishment }})</li>
            <li><strong>Castigo que recibiste:</strong> {{ punishment_received }} puntos (te dedujeron {{ punishment_deduction }})</li>
        </ul>
        <p><em>El castigo es anónimo. No sabes quién te castigó.</em></p>
    </div>
    
    <!-- Payoff final destacado -->
    <div class="final-payoff-box">
        <p>Tu ganancia final:</p>
        <h2>{{ player.payoff }}</h2>
    </div>
    
</div>

{{ next_button }}
{{ endblock }}
```

---

#### 📍 MOMENTO DE COMMIT #4
```bash
git add public_goods/templates/public_goods/FinalResults.html
git commit -m "feat(templates): crea FinalResults con desglose de castigo"
```

---

#### Subir cambios y crear Pull Request
```bash
git push -u origin feature/sistema-castigo
```

</details>

---

### Verificación local

```bash
# Iniciar servidor
otree devserver

# Probar con 3 navegadores o pestañas
# 1. Cada jugador contribuye diferentes cantidades
# 2. Ver IntermediateResults muestra contribuciones
# 3. Asignar castigo y verificar cálculo de costos
# 4. Verificar FinalResults muestra cálculos correctos
```

---

# PARTE 4: REVISIÓN DE CÓDIGO Y PULL REQUESTS

## 4.1 ¿Qué son los conflictos? (Breve explicación)

Antes de continuar, es importante que sepan qué son los **conflictos** en Git, aunque en este taller y en la tarea de ignorancia pluralista **no tendrán conflictos**.

### ¿Cuándo ocurren conflictos?

Un conflicto ocurre cuando **dos personas modifican la misma línea del mismo archivo** al mismo tiempo. Git no sabe cuál versión conservar y te pide que decidas.

**Ejemplo:**
- Ana modifica la línea 10 del archivo `settings.py` para poner `ENDOWMENT = 100`
- Bob modifica la misma línea 10 para poner `ENDOWMENT = 200`
- Cuando intentan unir sus cambios, Git dice: "¡No sé cuál usar!"

### ¿Por qué NO tendremos conflictos en este taller?

En este taller y en la tarea de ignorancia pluralista, cada persona trabaja en **archivos diferentes** o en **secciones diferentes** del código. Por eso no habrá conflictos.

| Persona | Trabaja en | No conflicta con |
|---------|------------|------------------|
| Mauricio | Introduction.html, Comprehension.html | Los demás |
| José Miguel | settings.py, parámetros | Los demás |
| Sergio | Results.html, visualización | Los demás |
| Donovan | Punishment.html, FinalResults.html | Los demás |

Si en el futuro trabajan en proyectos más complejos donde **sí** haya conflictos, Git les mostrará exactamente dónde está el problema y podrán resolverlo manualmente.

---

## 4.2 Ejercicio: Revisar el código de tus compañeros

### Objetivo

Cada persona debe **descargar y probar** el código del Pull Request de un compañero para verificar que funciona correctamente.

### Asignación de revisiones

| Tú revisas el PR de | Que implementa |
|---------------------|----------------|
| **José Miguel** revisa a Mauricio | Instrucciones y Comprensión |
| **Sergio** revisa a José Miguel | Parámetros y Tratamientos |
| **Donovan** revisa a Sergio | Resultados con Gráficos |
| **Mauricio** revisa a Donovan | Sistema de Castigo |

### Pasos para revisar

#### Paso 1: Ve al Pull Request asignado

1. Abre GitHub
2. Ve a **Pull requests**
3. Encuentra el PR de tu compañero asignado
4. Lee la descripción para entender qué debería hacer

#### Paso 2: Descarga el código para probarlo

```bash
# 1. Guarda tus cambios actuales (si los tienes)
git stash

# 2. Descarga la información de todas las ramas
git fetch origin

# 3. Cambia a la rama del PR de tu compañero
git checkout origin/feature/NOMBRE-DE-LA-RAMA

# Ejemplo para revisar el PR de Mauricio:
git checkout origin/feature/instrucciones-comprension
```

#### Paso 3: Prueba que funcione

```bash
# Inicia el servidor
otree devserver

# Abre http://localhost:8000 y prueba:
```

**Checklist de pruebas:**

Para **Instrucciones y Comprensión** (Mauricio):
- [ ] ¿La página de Introduction muestra las instrucciones completas?
- [ ] ¿El ejemplo numérico es correcto?
- [ ] ¿Las preguntas de comprensión aparecen?
- [ ] ¿Si respondo mal, muestra error y no me deja continuar?
- [ ] ¿Si respondo bien, puedo continuar?

Para **Parámetros y Tratamientos** (José Miguel):
- [ ] ¿Aparecen los dos tratamientos en el menú?
- [ ] ¿El tratamiento High MPCR usa multiplicador 2.0?
- [ ] ¿El tratamiento Low MPCR usa multiplicador 1.2?
- [ ] ¿Los payoffs se calculan correctamente en cada tratamiento?

Para **Resultados con Gráficos** (Sergio):
- [ ] ¿La tabla muestra las contribuciones de todos?
- [ ] ¿Mi fila está destacada?
- [ ] ¿El gráfico de barras aparece?
- [ ] ¿Mi barra tiene color diferente?
- [ ] ¿El desglose del cálculo es correcto?

Para **Sistema de Castigo** (Donovan):
- [ ] ¿IntermediateResults muestra contribuciones antes del castigo?
- [ ] ¿Puedo asignar puntos de castigo a otros jugadores?
- [ ] ¿El costo se calcula correctamente?
- [ ] ¿FinalResults muestra el impacto del castigo?
- [ ] ¿El payoff final es correcto?

#### Paso 4: Deja tu comentario en GitHub

1. Ve al PR en GitHub
2. Haz clic en **"Files changed"**
3. Revisa el código
4. Haz clic en **"Review changes"**
5. Escribe tu opinión:
   - ✅ Si todo funciona: **Approve** + "Todo funciona correctamente, probé X, Y, Z"
   - ❌ Si algo falla: **Request changes** + "Encontré este problema: [descripción]"

#### Paso 5: Regresa a tu trabajo

```bash
# Vuelve a tu rama
git checkout feature/TU-RAMA

# Recupera tus cambios guardados (si los tenías)
git stash pop
```

---

## 4.3 Después de la revisión

Una vez que tu PR tenga una aprobación:

1. **El autor del PR** hace clic en **"Merge pull request"**
2. Confirma el merge
3. (Opcional) Elimina la rama después del merge

**¡Felicidades!** Tu código ahora es parte del proyecto principal.

---

# APÉNDICES

## A. Comandos Git de referencia rápida

```bash
# Los 5 comandos esenciales
git checkout -b rama        # Crear rama nueva
git add .                   # Agregar cambios
git commit -m "mensaje"     # Guardar cambios
git push -u origin rama     # Subir a GitHub
# Pull Request              # En GitHub

# Comandos útiles adicionales
git status                  # Ver estado actual
git branch                  # Ver ramas
git checkout main           # Ir a main
git pull origin main        # Actualizar main
git log --oneline           # Ver historial
```

## B. Estructura final del proyecto

```
taller-otree-pgg/
├── public_goods/
│   ├── __init__.py
│   └── templates/
│       └── public_goods/
│           ├── Introduction.html
│           ├── Comprehension.html
│           ├── Contribute.html
│           ├── IntermediateResults.html
│           ├── Punishment.html
│           ├── FinalResults.html
│           └── Results.html
├── settings.py
├── README.md
├── .gitignore
└── requirements.txt
```

## C. Solución de problemas comunes

| Problema | Solución |
|----------|----------|
| `otree: command not found` | `pip install otree` |
| "Template not found" | Verifica la ruta de carpetas |
| El gráfico no aparece | Verifica conexión a internet (CDN) |
| Push rechazado | Crea Pull Request en lugar de push directo |
| "No estoy en la rama correcta" | `git checkout nombre-rama` |

---

**¡Fin del taller! 🎉**

*Documento generado para el taller interactivo de Git/GitHub con oTree*

