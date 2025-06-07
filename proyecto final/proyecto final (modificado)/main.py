from producto import Producto
from usuario import Administrador, Cliente
from archivo_productos import ArchivoProductos
from historial_compras import HistorialCompras
from menu import menu_principal
from colores import RESET, ROJO, VERDE, AMARILLO, AZUL

def mostrar_productos_con_numeros(productos):
    categorias = {}
    for p in productos:
        categorias.setdefault(p.categoria, []).append(p)

    lista_ordenada = []
    contador = 1
    for categoria, prods in categorias.items():
        print(f"\nCategoría: {categoria}")
        for p in prods:
            alerta_stock = " (⚠️ Stock bajo)" if p.stock <= 5 else ""
            print(f"  {contador}. {p.nombre} | ${p.precio:.2f} | Stock: {p.stock}{alerta_stock}")
            lista_ordenada.append(p)
            contador += 1 
    print()
    return lista_ordenada

def ejecutar_admin(nombre_admin):
    productos = ArchivoProductos.cargar()
    admin = Administrador(nombre_admin)

    while True:
        admin.mostrar_menu()
        print(f"{VERDE}8.{RESET} Ver historial de compras")
        print(f"{VERDE}9.{RESET} Agregar nuevo producto")
        opcion = input("Opción: ")

        if opcion == "1":
            productos_disponibles = [p for p in productos if p.stock > 0]
            print("Productos disponibles:")
            lista_ordenada = mostrar_productos_con_numeros(productos_disponibles)
            try:
                indice = int(input("Seleccione el número del producto: ")) - 1
                if 0 <= indice < len(lista_ordenada):
                    producto_seleccionado = lista_ordenada[indice]
                    print(f"Seleccionaste: {producto_seleccionado.nombre}")
                else:
                    print("Selección fuera de rango.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "2":
            mostrar_productos_con_numeros(productos)

        elif opcion == "3":
            filtro = input("Buscar por nombre o categoría: ").lower()
            encontrados = [p for p in productos if filtro in p.nombre.lower() or filtro in p.categoria.lower()]
            if encontrados:
                mostrar_productos_con_numeros(encontrados)
            else:
                print("No se encontraron productos con ese filtro.")

        elif opcion == "4":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            try:
                seleccion = int(input("Selecciona el número del producto a reabastecer: ")) - 1
                if 0 <= seleccion < len(productos):
                    cantidad = int(input("Cantidad a agregar: "))
                    if cantidad > 0:
                        productos[seleccion].stock += cantidad
                        ArchivoProductos.guardar(productos)
                        print(f"{VERDE}Stock actualizado.{RESET}")
                    else:
                        print("Cantidad debe ser mayor que cero.")
                else:
                    print(f"{ROJO}Selección inválida.{RESET}")
            except ValueError:
                print(f"{ROJO}Entrada inválida.{RESET}")

        elif opcion == "5":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            try:
                seleccion = int(input("Selecciona el número del producto a editar: ")) - 1
                if 0 <= seleccion < len(productos):
                    producto = productos[seleccion]
                    print("Dejar en blanco si no quieres cambiar un campo.")
                    nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ") or producto.nombre
                    nueva_categoria = input(f"Nueva categoría ({producto.categoria}): ") or producto.categoria
                    nuevo_precio = input(f"Nuevo precio ({producto.precio}): ")
                    nuevo_stock = input(f"Nuevo stock ({producto.stock}): ")

                    producto.nombre = nuevo_nombre
                    producto.categoria = nueva_categoria
                    if nuevo_precio:
                        producto.precio = float(nuevo_precio)
                    if nuevo_stock:
                        producto.stock = int(nuevo_stock)

                    ArchivoProductos.guardar(productos)
                    print(f"{VERDE}Producto actualizado.{RESET}")
                else:
                    print(f"{ROJO}Selección inválida.{RESET}")
            except ValueError:
                print(f"{ROJO}Entrada inválida.{RESET}")

        elif opcion == "6":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            try:
                seleccion = int(input("Selecciona el número del producto a eliminar: ")) - 1
                if 0 <= seleccion < len(productos):
                    eliminado = productos.pop(seleccion)
                    ArchivoProductos.guardar(productos)
                    print(f"{VERDE}Producto '{eliminado.nombre}' eliminado.{RESET}")
                else:
                    print(f"{ROJO}Selección inválida.{RESET}")
            except ValueError:
                print(f"{ROJO}Entrada inválida.{RESET}")

        elif opcion == "7":
            break

        elif opcion == "8":
            print(f"\n{AZUL}Historial de Compras:{RESET}")
            HistorialCompras.mostrar_historial()
            print()

        elif opcion == "9":
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
                    stock = int(input("Stock: "))
                    if stock < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Stock inválido. Intenta de nuevo.")

            nuevo_producto = Producto(nombre, categoria, precio, stock)
            productos.append(nuevo_producto)
            ArchivoProductos.guardar(productos)
            print(f"{VERDE}Producto '{nombre}' agregado correctamente.{RESET}")

        else:
            print(f"{ROJO}Opción no válida.{RESET}")

def ejecutar_cliente(nombre_cliente):
    productos = ArchivoProductos.cargar()
    cliente = Cliente(nombre_cliente)
    carrito = []

    while True:
        cliente.mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            productos_disponibles = [p for p in productos if p.stock > 0]
            if not productos_disponibles:
                print(f"{AMARILLO}No hay productos disponibles en este momento.{RESET}")
            else:
                lista_ordenada = mostrar_productos_con_numeros(productos_disponibles)
                try:
                    seleccion = int(input("Escoge el número del producto: ")) - 1
                    if 0 <= seleccion < len(lista_ordenada):
                        cantidad = int(input("Cantidad a comprar: "))
                        if cantidad > 0:
                            if lista_ordenada[seleccion].stock >= cantidad:
                                carrito.append((lista_ordenada[seleccion], cantidad))
                                print(f"{VERDE}Producto agregado al carrito.{RESET}")
                            else:
                                print(f"{ROJO}Stock insuficiente.{RESET}")
                        else:
                            print("Cantidad debe ser mayor que cero.")
                    else:
                        print(f"{ROJO}Producto no válido.{RESET}")
                except ValueError:
                    print(f"{ROJO}Entrada inválida.{RESET}")

        elif opcion == "2":
            if not carrito:
                print(f"{AMARILLO}Carrito vacío.{RESET}")
            else:
                print(f"Carrito de compras:")
                for idx, (prod, cant) in enumerate(carrito):
                    print(f"{idx + 1}. {prod.nombre} x{cant} = ${prod.precio * cant:.2f}")
                subopcion = input("¿Deseas (M)odificar cantidad, (E)liminar producto o (N)ada?: ").lower()
                if subopcion == "m":
                    try:
                        index = int(input("Número del producto a modificar: ")) - 1
                        if 0 <= index < len(carrito):
                            nueva_cant = int(input("Nueva cantidad: "))
                            if nueva_cant > 0:
                                carrito[index] = (carrito[index][0], nueva_cant)
                                print(f"{VERDE}Cantidad modificada.{RESET}")
                            else:
                                print("Cantidad debe ser mayor que cero.")
                        else:
                            print(f"{ROJO}Índice inválido.{RESET}")
                    except ValueError:
                        print(f"{ROJO}Entrada inválida.{RESET}")
                elif subopcion == "e":
                    try:
                        index = int(input("Número del producto a eliminar: ")) - 1
                        if 0 <= index < len(carrito):
                            carrito.pop(index)
                            print(f"{VERDE}Producto eliminado del carrito.{RESET}")
                        else:
                            print(f"{ROJO}Índice inválido.{RESET}")
                    except ValueError:
                        print(f"{ROJO}Entrada inválida.{RESET}")

        elif opcion == "3":
            filtro = input("Buscar por nombre o categoría: ").lower()
            encontrados = [p for p in productos if filtro in p.nombre.lower() or filtro in p.categoria.lower()]
            if encontrados:
                mostrar_productos_con_numeros(encontrados)
            else:
                print("No se encontraron productos con ese filtro.")

        elif opcion == "4":  # Finalizar compra
            if not carrito:
                print(f"{AMARILLO}No hay productos en el carrito.{RESET}")
            else:
                total = sum(p.precio * c for p, c in carrito)
                print(f"Total a pagar: ${total:.2f}")
                forma_pago = input("¿Pagar con (E)fectivo o (T)arjeta?: ").lower()
                if forma_pago == "t":
                    nip = input("Ingresa tu NIP de 4 dígitos: ")
                    if len(nip) == 4 and nip.isdigit():
                        for prod, cant in carrito:
                            prod.stock -= cant
                        ArchivoProductos.guardar(productos)
                        HistorialCompras.guardar_compra(cliente.nombre, carrito, "Tarjeta")
                        carrito.clear()
                        print(f"{VERDE}¡Pago con tarjeta exitoso! Gracias por su compra.{RESET}")
                    else:
                        print(f"{ROJO}NIP incorrecto. Pago cancelado.{RESET}")
                elif forma_pago == "e":
                    for prod, cant in carrito:
                        prod.stock -= cant
                    ArchivoProductos.guardar(productos)
                    HistorialCompras.guardar_compra(cliente.nombre, carrito, "Efectivo")
                    carrito.clear()
                    print(f"{VERDE}¡Pago en efectivo exitoso! Gracias por su compra.{RESET}")

        elif opcion == "5":
            break

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            nombre_admin = input("Ingresa tu nombre de administrador: ")
            ejecutar_admin(nombre_admin)
        elif opcion == "2":
            nombre_cliente = input("Ingresa tu nombre de cliente: ")
            ejecutar_cliente(nombre_cliente)
        elif opcion == "3":
            print(f"{AMARILLO}Saliendo... Gracias por su compra.{RESET}")
            break
        else:
            print(f"{ROJO}Opción no válida.{RESET}")

if __name__ == "__main__":
    main()
