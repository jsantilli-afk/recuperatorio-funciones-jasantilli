def calcular_costo (precio_unitario, cantidad):
    calcular_costo = precio_unitario * cantidad
    print ("este es el total de la venta sin el descuento: ", calcular_costo)
    if calcular_costo >= 25000:
        print ("su compra es mayor a 25000 pesos")
        print ("se le aplicara un descuento del 15%")
        preciototal_condescuento = calcular_costo - calcular_costo/100*15
        print ("total con descuento: ",preciototal_condescuento)
        return preciototal_condescuento
    else:
        print ("se quedo sin descuento, panflin")
        return calcular_costo