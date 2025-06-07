class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        alerta = " (⚠️ Stock bajo)" if self.stock <= 5 else ""
        return f"{self.nombre} | {self.categoria} | ${self.precio:.2f} | Stock: {self.stock}{alerta}"

def mostrar_productos_con_indices(productos):
    categorias = {}
    for p in productos:
        categorias.setdefault(p.categoria, []).append(p)

    contador = 1
    productos_lista = []
    for categoria, prods in categorias.items():
        print(f"\nCategoría: {categoria}")
        for p in prods:
            print(f"  {contador}. {p}")
            productos_lista.append(p)
            contador += 1
    return productos_lista

def menu_administrador():
    print("\nMenú Administrador:")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Volver")

def menu_cliente():
    print("\nMenú Cliente:")
    print("1. Ver productos y agregar al carrito")
    print("2. Ver carrito")
    print("3. Salir")

def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría: ").strip()
    while True:
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            print("Precio inválido. Intenta de nuevo.")

    while True:
        try:
            stock = int(input("Stock inicial: "))
            if stock < 0:
                raise ValueError
            break
        except ValueError:
            print("Stock inválido. Intenta de nuevo.")

    # Validar que el producto no exista ya (por nombre)
    for p in productos:
        if p.nombre.lower() == nombre.lower():
            print("El producto ya existe.")
            return

    nuevo_producto = Producto(nombre, categoria, precio, stock)
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

def main():
    productos = [
        Producto("Jabon", "Limpieza", 20.0, 10),
        Producto("Shampoo", "Limpieza", 50.0, 3),
        Producto("Jamon", "Comida", 33.0, 13),
        Producto("Sal", "Comida", 15.5, 18),
        Producto("Mazapan", "Comida", 10.0, 10),
        Producto("Arroz", "Comida", 32.0, 20),
        Producto("Sandia", "Fruta", 50.0, 5),
        Producto("Aguacate", "Fruta", 40.0, 28),
        Producto("Uvas", "Fruta", 35.9, 13)
    ]

    carrito = []

    while True:
        print("\nMenú principal:")
        print("1. Administrador")
        print("2. Cliente")
        print("3. Salir")

        opcion = input("Selecciona opción: ")

        if opcion == "1":
            while True:
                menu_administrador()
                op_admin = input("Opción administrador: ")

                if op_admin == "1":
                    agregar_producto(productos)
                elif op_admin == "2":
                    mostrar_productos_con_indices(productos)
                elif op_admin == "3":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            while True:
                menu_cliente()
                op_cliente = input("Opción cliente: ")

                if op_cliente == "1":
                    productos_disponibles = [p for p in productos if p.stock > 0]
                    if not productos_disponibles:
                        print("No hay productos disponibles.")
                        continue

                    lista_mostrada = mostrar_productos_con_indices(productos_disponibles)

                    seleccion = input("\nSelecciona producto (número) para agregar al carrito (o 'x' para cancelar): ")
                    if seleccion.lower() == 'x':
                        continue

                    if seleccion.isdigit():
                        seleccion = int(seleccion)
                        if 1 <= seleccion <= len(lista_mostrada):
                            producto_seleccionado = lista_mostrada[seleccion - 1]
                            print(f"Seleccionaste: {producto_seleccionado.nombre}")

                            cantidad = input(f"Cantidad a comprar (stock: {producto_seleccionado.stock}): ")
                            if cantidad.isdigit():
                                cantidad = int(cantidad)
                                if 0 < cantidad <= producto_seleccionado.stock:
                                    carrito.append((producto_seleccionado, cantidad))
                                    producto_seleccionado.stock -= cantidad
                                    print(f"{cantidad} x {producto_seleccionado.nombre} agregado(s) al carrito.")
                                else:
                                    print("Cantidad inválida o mayor al stock disponible.")
                            else:
                                print("Cantidad inválida.")
                        else:
                            print("Número inválido.")
                    else:
                        print("Por favor ingresa un número válido.")

                elif op_cliente == "2":
                    if not carrito:
                        print("Carrito vacío.")
                    else:
                        print("\nCarrito:")
                        total = 0
                        for p, c in carrito:
                            subtotal = p.precio * c
                            total += subtotal
                            print(f"- {p.nombre} | Cantidad: {c} | Subtotal: ${subtotal:.2f}")
                        print(f"Total: ${total:.2f}")

                elif op_cliente == "3":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "3":
            print("Gracias por usar la tienda.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
