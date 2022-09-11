"""
    Script de demostración de uso. Recuerda que debes configurar la impresora y el conector.
    1. Descarga el conector:  https://github.com/parzibyte/ejemplos-plugin-impresoras-termicas-v2/releases/latest
    2. Configura tu impresora y compártela
    3. Ejecuta el conector (no abre ventanas)
    4. Ejecuta este script.
    Ante cualquier duda: https://parzibyte.me/blog/2021/02/09/presentando-plugin-impresoras-termicas-version-2/
"""
from ConectorPlugin import Conector, AccionBarcodeJan13, AlineacionCentro

# Esto es para obtener las impresoras. No es obligatorio hacerlo siempre que se quiera imprimir
impresoras = Conector.obtenerImpresoras()
print(f"Las impresoras son: {impresoras}")

c = Conector()
c.imagenLocal("C:\\Users\\aldai\\Desktop\\logo2.png")
c.texto("\n")
c.textoConAcentos("Refaccionaria Raya\n")
c.establecerEnfatizado(1)
c.texto("Año 2021\n")
c.establecerEnfatizado(0)
c.texto("Sin enfatizado\n")
c.establecerTamanioFuente(2, 2)
c.texto("Texto de 2, 2\n")
c.establecerTamanioFuente(1, 1)
c.establecerJustificacion(AlineacionCentro)
c.texto("Texto centrado\n")
c.qrComoImagen("Parzibyte")
c.texto("Imagen de URL:\n")
c.imagenDesdeUrl("https:/github.com/parzibyte.png")
# Recuerda que la imagen debe existir y debe ser legible para el plugin. Si no, comenta las líneas
c.feed(5)
c.cortar()
c.abrirCajon()
print("Imprimiendo...")
# Recuerda cambiar por el nombre de tu impresora
respuesta = c.imprimirEn("Impresora chida")
if respuesta == True:
    print("Impresión correcta")
else:
    print(f"Error. El mensaje es: {respuesta}")