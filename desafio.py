def consultar_productos_usuario(numUsuario):
    arrProductos = []
    inputProductos = ''

    while (inputProductos != "Basta"):
        inputProductos = input(f"USUARIO {numUsuario}: Ingrese un producto. Si desea no ingresar más productos ingrese 'Basta'")
        if not inputProductos == "Basta":
            arrProductos.append(inputProductos)
        
    return arrProductos



productos1 = consultar_productos_usuario(1)
productos2 = consultar_productos_usuario(2)


def consultar_productos_iguales():
    arrProductosIguales = []

    for producto1 in productos1:
         for producto2 in productos2:
            if producto1 == producto2:
                arrProductosIguales.append(producto1)
    return arrProductosIguales

productosIguales = consultar_productos_iguales()
print((f"Los productos iguales de ambos usuarios son {productosIguales}"))


def consultar_productos_distintos():
    arrProductosDistintosUsuario1 = []

    for producto1 in productos1:
        if producto1 not in productos2:
            arrProductosDistintosUsuario1.append(producto1)

    arrProductosDistintosUsuario2 = []

    for producto2 in productos2:
        if producto2 not in productos1:
            arrProductosDistintosUsuario2.append(producto2)

    arrProductosDistintosTotal = arrProductosDistintosUsuario1 + arrProductosDistintosUsuario2

    return arrProductosDistintosTotal


productosDistintos = consultar_productos_distintos()

print(f"Los productos distintos entre ambos usuarios son {productosDistintos}")

print (f"Los productos totales entre ambos usuarios son {productos1 + productos2}")





