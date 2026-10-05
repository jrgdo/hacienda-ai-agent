# Contribuir

Se aceptan mejoras de documentación, plantillas, pruebas y reglas verificables.

## Requisitos

- Todo contenido debe estar en español claro.
- No incluyas información personal real.
- Utiliza personas y operaciones ficticias en las pruebas.
- Cada regla fiscal debe indicar ejercicio, vigencia, fuente oficial y fecha de comprobación.
- Diferencia una obligación legal, una recomendación y una hipótesis.
- Añade pruebas para cálculos y límites cuando corresponda.
- No introduzcas automatización de presentación sin una revisión específica de seguridad.

## Antes de enviar cambios

Ejecuta:

```bash
python3 herramientas/comprobar_privacidad.py .
python3 -m unittest discover -s tests
```

Revisa también `git diff --cached` antes del commit.
