# Compra de caucho

Cantidad = int(input("Ingrese la cantidad de cauchos: "))

Precio = int(input("Ingrese Precio del Caucho: "))
if Cantidad > 6:
    #Descuento 15%
    Descuento15 = Precio * .15 * Cantidad 
    print Descuento15
else:
    #Descuento 10%
    Descuento10 = Precio * .1 * Cantidad
    print Descuento10

SubTotal = Precio * Cantidad
print "Precio Lista:         ", Precio
print "Cantidad Comprada:    ", Cantidad
print  "Total de compra:     ", SubTotal
if Cantidad > 6:
    DescuentoTotal = Precio * .15
    print "Descuento de la compra", DescuentoTotal
else:
    DescuentoTotal = Precio * .1
    print "Descuento de la compra: ", DescuentoTotal
print "Total De Compra Neto: ", SubTotal - DescuentoTotal







