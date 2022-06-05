def calculoDESC (precio,descuento):
    total = (precio -(precio*(descuento/100)))
    print("el precio a pagar con el descuento de","%",descuento,"es de: $",total)
    
def IVA (precio):
    totalIVA = precio* 1.19
    print("el total del producto con valor",precio,"con IVA es de: ",totalIVA)
    return totalIVA

precio = int(input("ingrese el precio del producto:\n"))
desc = int(input("ingrese descuento (0-100):\n"))
calculoDESC(precio,desc)

precio= int(input("ingrese precio prodcto neto:\n"))
IVA(precio)
