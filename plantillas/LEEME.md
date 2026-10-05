# Usar el libro de seguimiento

Ejecuta `python3 herramientas/iniciar.py` desde el repositorio para obtener una copia privada. Abre `datos-usuario/resultados/seguimiento.local.xlsx`.

1. Cambia el ejercicio en `Configuracion!B2`.
2. Registra movimientos originales sin alterar sus descripciones ni importes.
3. Completa ingresos y gastos con fechas de devengo, documentos y actividad.
4. Introduce base, cuota IVA y retenciones según los documentos. Una factura con varios tipos se desglosa en líneas vinculadas.
5. En Gastos, Q y R contienen importes aprobados de gasto IRPF e IVA deducible. Se determinan por separado y no se calculan automáticamente aplicando un porcentaje genérico.
6. Mantén las operaciones en Pendiente hasta su revisión. Solo Confirmado entra en los totales fiscales del resumen.
7. Registra bienes duraderos en Bienes. Traslada únicamente la amortización aprobada al registro de gastos; evita duplicar el coste de compra.
8. Guarda la copia cumplimentada dentro de `datos-usuario/`.

Las celdas grises contienen fórmulas. Cada registro admite 200 filas. Para ampliar, hay que extender tablas, fórmulas, validaciones y todos los rangos del resumen de forma conjunta.

El libro es de seguimiento: no constituye un libro oficial validado para importación en AEAT ni genera ficheros BOE. El resultado de ingresos menos gastos es provisional. El saldo de IVA y los pagos a cuenta requieren ajustes propios de cada modelo.

No uses un cero del resumen como prueba de que no existe obligación. Revisa documentos, registros pendientes, operaciones excluidas y cobertura de todas las cuentas.
