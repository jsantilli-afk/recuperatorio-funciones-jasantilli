import opraciones
importes_finales = []
for i in range (5):
    precio_unitario = int(input("ingrese el precio de las unidades: "))
    cantidad = int(input("ingrese la cantidad de productos: "))
    total = opraciones.calcular_costo (precio_unitario, cantidad)
    importes_finales.append(total)
print("Importes finales:", importes_finales)