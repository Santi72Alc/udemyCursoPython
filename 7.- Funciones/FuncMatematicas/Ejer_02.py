"""
Ejercicio 2

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def conIva(importe = 0, iva = 21):
    totalFra = 0
    impIva = 0
    if importe>0:
        impIva = importe*iva/100
        totalFra = importe + impIva
    print(f"Importe: {importe} es con IVA del {iva}% ({impIva:.0f}) = {totalFra:.0f}")



# Prueba
conIva(1000)
conIva(8400, 10)