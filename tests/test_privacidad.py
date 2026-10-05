import tempfile
import unittest
from pathlib import Path

from herramientas.comprobar_privacidad import revisar_archivo, revisar_bytes


class PrivacidadTests(unittest.TestCase):
    def test_bloquea_datos_privados_forzados(self):
        self.assertTrue(revisar_bytes('datos-usuario/real.csv', b'contenido'))

    def test_bloquea_certificado(self):
        self.assertTrue(revisar_bytes('certificado.pfx', b'contenido'))

    def test_bloquea_libro_ajeno(self):
        self.assertTrue(revisar_bytes('libro.xlsx', b'contenido'))

    def test_permite_readme_local(self):
        self.assertEqual(revisar_bytes('datos-usuario/README.md', b'Instrucciones'), [])

    def test_detecta_iban_ficticio(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "muestra.txt"
            ruta.write_text("Cuenta: ES" + "00" * 11, encoding="utf-8")
            hallazgos = revisar_archivo(ruta)
            self.assertTrue(any(item[0] == "IBAN" for item in hallazgos))

    def test_texto_generico_no_genera_hallazgo(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "muestra.txt"
            ruta.write_text("Plantilla genérica sin datos personales.", encoding="utf-8")
            self.assertEqual(revisar_archivo(ruta), [])


if __name__ == "__main__":
    unittest.main()
