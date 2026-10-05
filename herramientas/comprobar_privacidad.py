#!/usr/bin/env python3
"""Detecta patrones sensibles antes de versionar archivos.

Es una barrera adicional, no una garantía de anonimización.
"""

from __future__ import annotations

import re
import sys
import subprocess
import io
import zipfile
from pathlib import Path


PATRONES = {
    "IBAN": re.compile(r"\bES\d{2}(?:[ -]?\d{4}){5}\b", re.IGNORECASE),
    "NIF_DNI": re.compile(r"\b\d{8}[A-Z]\b", re.IGNORECASE),
    "NIE": re.compile(r"\b[XYZ]\d{7}[A-Z]\b", re.IGNORECASE),
    "EMAIL": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "CLAVE_PRIVADA": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

EXTENSIONES_TEXTO = {
    ".md", ".txt", ".yaml", ".yml", ".json", ".csv", ".py", ".js", ".mjs", ".toml", ".xml"
}

CARPETAS_IGNORADAS = {".git", "node_modules", "__pycache__", "datos-usuario", "work", ".venv"}


def revisar_bytes(nombre, contenido):
    ruta = Path(nombre)
    if "datos-usuario" in ruta.parts and nombre != "datos-usuario/README.md":
        return [("ARCHIVO_PRIVADO", 0)]
    if ".local." in nombre or ruta.name.startswith(".env") or ruta.suffix.lower() in {".p12", ".pfx", ".pem", ".key", ".cer", ".crt", ".pdf"}:
        return [("ARCHIVO_SENSIBLE", 0)]
    if ruta.suffix == ".xlsx":
        if nombre != "plantillas/plantilla_autonomos.xlsx":
            return [("LIBRO_NO_AUTORIZADO", 0)]
        try:
            with zipfile.ZipFile(io.BytesIO(contenido)) as libro:
                texto = "\n".join(libro.read(n).decode("utf-8") for n in libro.namelist() if n.endswith(".xml"))
        except (ValueError, zipfile.BadZipFile, UnicodeDecodeError):
            return [("LIBRO_NO_LEIBLE", 0)]
    else:
        try:
            texto = contenido.decode("utf-8")
        except UnicodeDecodeError:
            return [("BINARIO_REQUIERE_REVISION", 0)]
    return [(tipo, texto.count("\n", 0, m.start()) + 1) for tipo, patron in PATRONES.items() for m in patron.finditer(texto)]


def revisar_archivo(ruta: Path):
    if ruta.suffix.lower() not in EXTENSIONES_TEXTO:
        return []
    try:
        texto = ruta.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []
    hallazgos = []
    for nombre, patron in PATRONES.items():
        for coincidencia in patron.finditer(texto):
            linea = texto.count("\n", 0, coincidencia.start()) + 1
            hallazgos.append((nombre, linea))
    return hallazgos


def recorrer(raiz: Path):
    for ruta in raiz.rglob("*"):
        if not ruta.is_file():
            continue
        if any(parte in CARPETAS_IGNORADAS for parte in ruta.parts):
            continue
        yield ruta


def main():
    if "--staged" in sys.argv:
        nombres = subprocess.check_output(["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"]).decode().split("\0")
    elif "--tracked" in sys.argv:
        nombres = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\0")
    else:
        nombres = None
    if nombres is not None:
        errores = []
        for nombre in filter(None, nombres):
            contenido = subprocess.check_output(["git", "show", ":" + nombre]) if "--staged" in sys.argv else Path(nombre).read_bytes()
            errores.extend(f"{nombre}:{linea}: posible {tipo}" for tipo, linea in revisar_bytes(nombre, contenido))
        print("\n".join(errores) if errores else "Control de privacidad completado sin coincidencias.")
        return int(bool(errores))
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errores = []
    for ruta in recorrer(raiz):
        for tipo, linea in revisar_archivo(ruta):
            errores.append(f"{ruta.relative_to(raiz)}:{linea}: posible {tipo}")
    if errores:
        print("Se detectaron patrones que deben revisarse:")
        print("\n".join(errores))
        return 1
    print("Control de privacidad completado sin coincidencias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
