import json
import os
from datetime import datetime

class HistorialCompras:
    archivo = "historial_compras.json"

    @staticmethod
    # Cargar el historial de compras desde un archivo JSON
    def cargar_historial():
        if not os.path.exists(HistorialCompras.archivo):
            return []
        with open(HistorialCompras.archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_historial(historial):
       # Guardar el historial de compras en un archivo JSON
        with open(HistorialCompras.archivo, "w", encoding="utf-8") as f:
            json.dump(historial, f, indent=4, ensure_ascii=False)

    @staticmethod
    def guardar_compra(nombre_cliente, carrito, metodo_pago):
        #esto me sirve para guardar una compra en el historial
        historial = HistorialCompras.cargar_historial()

        # Convertir carrito a lista de dicts para guardar
        productos_guardar = []
        for producto, cantidad in carrito:
            productos_guardar.append({
                "nombre": producto.nombre,
                "categoria": producto.categoria,
                "precio_unitario": producto.precio,
                "cantidad": cantidad,
                "subtotal": producto.precio * cantidad
            })

        compra = {
            "cliente": nombre_cliente,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "productos": productos_guardar,
            "metodo_pago": metodo_pago,
            "total": sum(p["subtotal"] for p in productos_guardar)
        }

        historial.append(compra)
        HistorialCompras.guardar_historial(historial)

    @staticmethod
    # Mostrar el historial de compras de forma legible
    def mostrar_historial():
        historial = HistorialCompras.cargar_historial()
        if not historial:
            print("No hay compras registradas.")
            return

        # Mostrar el historial de compras
        for idx, compra in enumerate(historial, 1):
            print(f"Compra #{idx}")
            print(f"Cliente: {compra['cliente']}")
            print(f"Fecha: {compra['fecha']}")
            print(f"Método de pago: {compra['metodo_pago']}")
            print("Productos:")
            # Mostrar los productos de la compra 
            for p in compra["productos"]:
                print(f"  - {p['nombre']} ({p['categoria']}), "
                      f"Precio unitario: ${p['precio_unitario']:.2f}, "
                      f"Cantidad: {p['cantidad']}, "
                      f"Subtotal: ${p['subtotal']:.2f}")
            print(f"Total: ${compra['total']:.2f}")
            print("-" * 40)

