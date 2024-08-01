from gestion_productos import agregar_producto, eliminar_producto, actualizar_precio, listar_productos, buscar_producto
import archivos

productos = []
proveedores = archivos.cargar_proveedores("proveedores.txt")

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar precio de producto")
    print("4. Listar productos")
    print("5. Buscar producto")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")

while True:
    mostrar_menu()
    opcion = input("Elija una opción: ")
    
    if opcion == '1':
        agregar_producto(productos, proveedores)
    elif opcion == '2':
        codigo = input("Ingrese el código del producto a eliminar: ")
        eliminar_producto(productos, codigo)
    elif opcion == '3':
        codigo = input("Ingrese el código del producto a actualizar: ")
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        actualizar_precio(productos, codigo, nuevo_precio)
    elif opcion == '4':
        listar_productos(productos)
    elif opcion == '5':
        codigo = input("Ingrese el código del producto a buscar: ")
        buscar_producto(productos, codigo)
    elif opcion == '6':
        archivos.guardar_inventario(productos, "inventario.txt")
    elif opcion == '7':
        productos = archivos.cargar_inventario("inventario.txt")
    elif opcion == '8':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")

class Producto:
    def __init__(self, codigo, nombre, marca, precio, existencias, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.existencias = existencias
        self.proveedor = proveedor

def agregar_producto(productos, proveedores):
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    existencias = int(input("Ingrese las existencias del producto: "))
    proveedor = input("Ingrese el proveedor del producto: ")
    
    nuevo_producto = Producto(codigo, nombre, marca, precio, existencias, proveedor)
    productos.append(nuevo_producto)
    print("Producto agregado exitosamente.")

def eliminar_producto(productos, codigo):
    producto_eliminado = False
    for producto in productos:
        if producto.codigo == codigo:
            productos.remove(producto)
            producto_eliminado = True
            print("Producto eliminado exitosamente.")
            break
    if not producto_eliminado:
        print("Producto no encontrado.")

def actualizar_precio(productos, codigo, nuevo_precio):
    for producto in productos:
        if producto.codigo == codigo:
            producto.precio = nuevo_precio
            print("Precio actualizado exitosamente.")
            return
    print("Producto no encontrado.")

def listar_productos(productos):
    if productos:
        for producto in productos:
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Marca: {producto.marca}, Precio: {producto.precio}, Existencias: {producto.existencias}, Proveedor: {producto.proveedor}")
    else:
        print("No hay productos en el inventario.")

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto.codigo == codigo:
            print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Marca: {producto.marca}, Precio: {producto.precio}, Existencias: {producto.existencias}, Proveedor: {producto.proveedor}")
            return
    print("Producto no encontrado.")

def cargar_proveedores(ruta_archivo):
    proveedores = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                proveedores.append(linea.strip())
    except FileNotFoundError:
        print("Archivo de proveedores no encontrado.")
    return proveedores

def guardar_inventario(productos, ruta_archivo):
    try:
        with open(ruta_archivo, 'w') as archivo:
            for producto in productos:
                archivo.write(f"{producto.codigo},{producto.nombre},{producto.marca},{producto.precio},{producto.existencias},{producto.proveedor}\n")
        print("Inventario guardado exitosamente.")
    except Exception as e:
        print(f"Error guardando el inventario: {e}")

def cargar_inventario(ruta_archivo):
    productos = []
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                codigo, nombre, marca, precio, existencias, proveedor = linea.strip().split(',')
                productos.append(Producto(codigo, nombre, marca, float(precio), int(existencias), proveedor))
    except FileNotFoundError:
        print("Archivo de inventario no encontrado.")
    except Exception as e:
        print(f"Error cargando el inventario: {e}")
    return productos
