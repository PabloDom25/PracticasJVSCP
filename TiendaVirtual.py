catalogo = {
    "Camiseta": 20,
    "Jeans": 40,
    "Zapatos": 60,
    "Sombrero": 10
}

while True:
    print("\nMenu:")
    print("1. Agregar productos al carrito")
    print("2. Ver carrito")
    print("3. Realizar el pago y salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        print("\nProductos disponibles:")
        [print(f"* (producto) $(precio)") for producto, precio in catalogo.items()]
        producto = input("Ingrese el nombre del producto que desea agregar: ").title()

        if producto in catalogo:
            carrito.append(producto)
            print(f"Producto '(producto)' agregado al carrito.")

    if opcion == "2":
        print("\nCarrito:")
        for producto in set(carrito):
            cantidad = carrito.count(producto)
            precio_unitario = catalogo[producto]
            print(f"{cantidad} {producto} - ${precio_unitario} c/u")

    if opcion == "3":
        total_a_pagar = sum(catalogo[producto] for producto in carrito)
        print(f"Total a pagar: ${total_a_pagar}")

        try:

            monto_pagado = float(input("Ingrese el monto con el que pagara: "))
            cambio = monto_pagado - total_a_pagar

            if cambio >= 0:
                mensaje_cambio = f"Su cambio es: ${round(cambio, 2)}" if cambio > 0 else "¡Exacto! No se requier cambio."
                print(f"Gracias por su compra. {mensaje_cambio}")
                break
            else:
                print("El monto ingresado es insuficiente. Por favor, ingrese un monto valido.")    

        except Exception as e:
            print("Monto invalido. Por favor, ingrese un monto valido.")

    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")                        