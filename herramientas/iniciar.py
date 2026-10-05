#!/usr/bin/env python3
"""Crea el espacio local sin sobrescribir datos existentes."""
from pathlib import Path
import shutil
import subprocess


def iniciar(raiz):
    raiz = Path(raiz)
    destino = raiz / 'datos-usuario'
    for carpeta in ['bancos', 'facturas-emitidas', 'facturas-recibidas', 'plataformas', 'declaraciones', 'resultados']:
        (destino / carpeta).mkdir(parents=True, exist_ok=True)
    for origen, salida in [
        ('configuration/perfil.example.yaml', 'perfil.local.yaml'),
        ('plantillas/plantilla_autonomos.xlsx', 'resultados/seguimiento.local.xlsx'),
    ]:
        final = destino / salida
        if not final.exists():
            shutil.copyfile(raiz / origen, final)
    return destino


if __name__ == '__main__':
    raiz = Path(__file__).resolve().parents[1]
    if subprocess.run(['git', 'check-ignore', '-q', 'datos-usuario/perfil.local.yaml'], cwd=raiz).returncode:
        raise SystemExit('No se ha confirmado la exclusión de Git. Revisa .gitignore.')
    iniciar(raiz)
    print('Espacio local preparado. Abre Codex o Claude y solicita el onboarding.')
