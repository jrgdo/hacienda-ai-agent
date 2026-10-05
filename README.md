# Hacienda AI Agent

Plantilla abierta, local y sector-agnóstica para convertir un asistente de IA en una ayuda organizada para autónomos en España.

El proyecto ayuda a:

- realizar un onboarding fiscal guiado;
- ordenar movimientos bancarios sin borrar los originales;
- separar ingresos, gastos, traspasos, operaciones personales, existencias y bienes de inversión;
- comprobar facturas y justificantes pendientes;
- preparar borradores revisables de declaraciones;
- mantener un libro Excel anual con resumen trimestral;
- verificar reglas cambiantes en fuentes oficiales.

No presenta declaraciones automáticamente y no sustituye a una persona profesional habilitada. La responsabilidad de la clasificación, los datos y la presentación corresponde al contribuyente.

## Privacidad por diseño

Este repositorio público no contiene datos personales reales. Los datos de cada usuario deben guardarse únicamente en `datos-usuario/`, cuyos contenidos están excluidos de Git.

Nunca subas al repositorio:

- NIF, NIE, nombre completo, domicilio o IBAN;
- extractos bancarios, facturas o tickets reales;
- certificados electrónicos, claves o copias de declaraciones;
- libros registro cumplimentados;
- conversaciones que contengan información personal.

Incluso en un repositorio privado, se recomienda conservar los documentos fiscales fuera de Git y cifrados.

## Inicio rápido

1. Usa este repositorio como plantilla o clónalo localmente.
2. Ejecuta `python3 herramientas/iniciar.py` y abre la carpeta con Codex o Claude Code. Si no utilizas Python, pide al agente que copie las plantillas al espacio local sin sobrescribir archivos.
3. Pide: `Inicia mi onboarding fiscal siguiendo AGENTS.md`.
4. El agente creará `datos-usuario/perfil.local.yaml` y nunca deberá versionarlo.
5. Añade tus archivos únicamente dentro de `datos-usuario/`.
6. Pide al agente que importe y clasifique los movimientos, sin borrar el archivo original.
7. Revisa y confirma manualmente cada clasificación antes de preparar una declaración.

## Compatibilidad

- `AGENTS.md`: entrada para Codex y agentes compatibles.
- `CLAUDE.md`: entrada para Claude Code.
- `agent/`: instrucciones compartidas y fuente de verdad.

Ambos agentes deben seguir las mismas reglas. No dupliques reglas fiscales dentro de los archivos de entrada.

## Flujo recomendado

1. Onboarding y mapa provisional de obligaciones.
2. Importación de movimientos originales.
3. Clasificación preliminar con explicación y nivel de revisión.
4. Vinculación con facturas y otros justificantes.
5. Conciliación de banco, caja y plataformas de pago.
6. Revisión humana de partidas dudosas.
7. Borrador de cada modelo, casilla por casilla.
8. Comparación con declaraciones anteriores.
9. Confirmación expresa antes de cualquier presentación externa.
10. Archivo local del justificante presentado.

## Alcance inicial

La primera versión está orientada a personas físicas autónomas en España y a la preparación documental de obligaciones frecuentes. La aplicabilidad de cada modelo depende del perfil fiscal y debe confirmarse para el ejercicio correspondiente.

## Plantilla Excel

`plantillas/plantilla_autonomos.xlsx` contiene:

- configuración y selector de ejercicio;
- dashboard anual y trimestral;
- movimientos originales;
- ingresos y gastos;
- bienes de inversión;
- facturas pendientes;
- control de declaraciones;
- desplegables incorporados en los registros.

El archivo es una plantilla vacía. No incluye información real.

Consulta [las instrucciones del Excel](plantillas/LEEME.md). Incluye 200 filas por registro; ampliar tablas exige ampliar también los rangos del resumen.

## Conversaciones y datos locales

Puedes pedir: «Revisa los movimientos pendientes», «Explica qué falta para justificar este gasto», «Prepara un borrador del trimestre» o «Comprueba los bienes de inversión». El agente debe leer el perfil local y pedir solo los datos que falten.

Guardar archivos localmente no implica que su procesamiento sea local: si utilizas un proveedor de IA en la nube, el contenido que compartas podrá enviarse a ese proveedor. Revisa sus opciones de privacidad y comparte solo lo necesario. Un chat web necesita recibir las instrucciones y archivos explícitamente; no lee esta carpeta automáticamente.

## Protección antes de publicar cambios

Instala `pre-commit` si deseas activar el control local y ejecuta `pre-commit install`. Antes de cada publicación ejecuta también `python3 herramientas/comprobar_privacidad.py --staged` y revisa el diff. El control de GitHub actúa después de subir los archivos: no evita por sí solo una filtración inicial. Los detectores son heurísticos y no reconocen todos los nombres, domicilios o datos sensibles.

## Desarrollo

Consulta `CONTRIBUTING.md`. Las reglas fiscales nuevas deben indicar ejercicio, vigencia, fecha de comprobación y enlace oficial. No se aceptan ejemplos con información real.

## Licencia y limitaciones

El código se distribuye bajo licencia MIT. Consulta `DISCLAIMER.md` antes de usarlo para preparar una obligación tributaria.
