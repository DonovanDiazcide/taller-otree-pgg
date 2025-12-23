# Prompt 2 – Tarea 3: Página de comprensión

## Cambios realizados
- Se creó el archivo `Comprehension.html` dentro de `public_goods/templates/public_goods/`.
- El template extiende `global/Page.html`.
- Se utiliza `{{ formfields }}` para mostrar automáticamente las preguntas de comprensión definidas en `Player`.
- Se incluye un botón `{{ next_button }}` para continuar el flujo del experimento.

## Justificación
Este template permite verificar que los participantes comprendan las reglas del juego
antes de avanzar, sin afectar sus pagos, siguiendo la estructura recomendada por oTree.
