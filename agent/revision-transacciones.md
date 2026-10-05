# Revisión de transacciones

## Principio de conservación

Nunca elimines ni sobrescribas el archivo original. Importa cada fila con un `id_origen`, conserva el texto íntegro y añade columnas derivadas.

## Flujo

1. Identifica cuenta, moneda, rango de fechas y saldo cuando exista.
2. Detecta duplicados sin borrarlos automáticamente.
3. Identifica traspasos por coincidencia de importe, fechas, cuentas y concepto.
4. Distingue cobros, pagos, devoluciones, comisiones y liquidaciones agrupadas.
5. Relaciona la operación con factura o justificante.
6. Propón categoría y tratamiento fiscal por separado.
7. Marca nivel de revisión y explica la razón.
8. Pide confirmación solo para partidas que cambian materialmente el resultado.
9. Concilia totales con el origen.

## Categorías mínimas

- ingreso_actividad
- otro_ingreso_actividad
- gasto_operativo
- existencias
- bien_inversion
- gasto_mixto
- personal_no_deducible
- traspaso_propio
- prestamo_financiacion
- impuesto
- seguridad_social
- devolucion_reembolso
- liquidacion_plataforma
- retencion
- pendiente_revision

## Evaluación separada

Para cada operación registra:

- inclusión en ingresos o gastos;
- base imponible, cuota y total cuando haya factura;
- tratamiento IRPF;
- tratamiento IVA;
- porcentaje de afectación;
- documento disponible;
- período de devengo y período bancario;
- explicación y fuente;
- decisión del usuario.

## Evidencia

Un movimiento bancario prueba un pago o cobro, pero normalmente no sustituye una factura. Marca expresamente `factura_pendiente`, `justificante_parcial` o `evidencia_completa`.

## Traspasos

Los traspasos entre cuentas propias no son ingresos ni gastos. Exclúyelos de totales fiscales, pero consérvalos en la conciliación con su pareja vinculada. Nunca los borres del origen.

## Plataformas y marketplaces

No trates el abono neto como ingreso cuando la plataforma agrupa ventas, comisiones, devoluciones e impuestos. Reconstruye la liquidación cuando exista detalle y marca la diferencia pendiente si no es posible.
