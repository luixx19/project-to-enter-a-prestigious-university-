from producto import Producto
from usuario import Administrador, Cliente
from archivo_productos import ArchivoProductos
from menu import menu_principal
from colores import RESET, ROJO, VERDE, AMARILLO, AZUL, CYAN, MAGENTA 

def ejecutar_admin():
    productos = ArchivoProductos.cargar()
    admin = Administrador("Admin")

    while True:
        admin.mostrar_menu()  
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            nuevo = Producto(nombre, categoria, precio, stock)
            productos.append(nuevo)
            ArchivoProductos.guardar(productos)
            print(f"{VERDE}Producto agregado.{RESET}")
        elif opcion == "2":
            for p in productos:
                print(p)
        elif opcion == "3":
            filtro = input("Buscar por nombre o categoría: ").lower()
            encontrados = [p for p in productos if filtro in p.nombre.lower() or filtro in p.categoria.lower()]
            for p in encontrados:
                print(p)
        elif opcion == "4":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            seleccion = int(input("Selecciona el número del producto a reabastecer: ")) - 1
            if 0 <= seleccion < len(productos):
                cantidad = int(input("Cantidad a agregar: "))
                productos[seleccion].stock += cantidad
                ArchivoProductos.guardar(productos)
                print(f"{VERDE}Stock actualizado.{RESET}")
            else:
                print(f"{ROJO}Selección inválida.{RESET}")
        elif opcion == "5":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
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
                if nuevo_precio: producto.precio = float(nuevo_precio)
                if nuevo_stock: producto.stock = int(nuevo_stock)

                ArchivoProductos.guardar(productos)
                print(f"{VERDE}Producto actualizado.{RESET}")
            else:
                print(f"{ROJO}No valida.{RESET}")
        elif opcion == "6":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            seleccion = int(input("Selecciona el número del producto a eliminar: ")) - 1
            if 0 <= seleccion < len(productos):
                productos.pop(seleccion)
                ArchivoProductos.guardar(productos)
                print(f"{VERDE}Producto eliminado.{RESET}")
            else:
                print(f"{ROJO}Selección inválida.{RESET}")
        elif opcion == "7":
            break

def ejecutar_cliente():
    productos = ArchivoProductos.cargar()
    cliente = Cliente("Cliente")
    carrito = []

    while True:
        cliente.mostrar_menu()  
        opcion = input("Opción: ")

        if opcion == "1":
            for idx, p in enumerate(productos):
                print(f"{idx + 1}. {p}")
            seleccion = int(input(" Escoje el número del producto: ")) - 1
            if 0 <= seleccion < len(productos):
                cantidad = int(input("Cantidad a comprar: "))
                if productos[seleccion].stock >= cantidad:
                    carrito.append((productos[seleccion], cantidad))
                    print(f"{VERDE}Producto agregado al carrito.{RESET}")
                else:
                    print(f"{ROJO}Stock insuficiente.{RESET}")
            else:
                print(f"{ROJO}Producto no válido.{RESET}")
        elif opcion == "2":
            if not carrito:
                print(f"{AMARILLO}Carrito vacío.{RESET}")
            else:
                print(f"Carrito de compras:")
                for idx, (prod, cant) in enumerate(carrito):
                    print(f"{idx + 1}. {prod.nombre} x{cant} = ${prod.precio * cant:.2f}")
                subopcion = input("¿Deseas (M)odificar cantidad, (E)liminar producto o (N)ada?: ").lower()
                if subopcion == "m":
                    index = int(input("Número del producto a modificar: ")) - 1
                    if 0 <= index < len(carrito):
                        nueva_cant = int(input("Nueva cantidad: "))
                        carrito[index] = (carrito[index][0], nueva_cant)
                        print(f"{VERDE}Cantidad modificada.{RESET}")
                elif subopcion == "e":
                    index = int(input("Número del producto a eliminar: ")) - 1
                    if 0 <= index < len(carrito):
                        carrito.pop(index)
                        print(f"{VERDE}Producto eliminado del carrito.{RESET}")
        elif opcion == "3":
            filtro = input("Buscar por nombre o categoría: ").lower()
            encontrados = [p for p in productos if filtro in p.nombre.lower() or filtro in p.categoria.lower()]
            for p in encontrados:
                print(p)
        elif opcion == "4":  # Pagar
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
                        carrito.clear()
                        print(f"{VERDE}¡Pago con tarjeta exitoso! Gracias por su compra.{RESET}")
                    else:
                        print(f"{ROJO}NIP incorrecto. Pago cancelado.{RESET}")
                elif forma_pago == "e":
                    for prod, cant in carrito:
                        prod.stock -= cant
                    ArchivoProductos.guardar(productos)
                    carrito.clear()
                    print(f"{VERDE}¡Pago en efectivo exitoso! Gracias por su compra.{RESET}")
        elif opcion == "5":
            break

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            ejecutar_admin()
        elif opcion == "2":
            ejecutar_cliente()
        elif opcion == "3":
            print(f"{AMARILLO}Saliendo Gracias por su compra...{RESET}")
            break

if __name__ == "__main__":
    main()
