
class Proveedor:
    def __init__(self, codigo, nombre, pais):
        self.codigo = codigo
        self.nombre = nombre
        self.pais = pais

    def __str__(self):
        return f"{self.nombre} ({self.pais})"
    
class Producto:
    def __init__(self, codigo, nombre, marca, precio, existencias, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.existencias = existencias
        self.proveedor = proveedor

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio:.2f} ({self.existencias} unidades)"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, codigo):
        self.productos = [p for p in self.productos if p.codigo != codigo]
    def listar_productos(self):
        for p in self.productos:
            print(p)

    def buscar_producto(self, codigo):
        for p in self.productos:
            if p.codigo == codigo:
                return p
        return None

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            for p in self.productos:
                archivo.write(f"{p.codigo},{p.nombre},{p.marca},{p.precio},{p.existencias},{p.proveedor.codigo}\n")

    def cargar_desde_archivo(self, nombre_archivo):
        self.productos = []
        try:
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    campos = linea.strip().split(",")
                    codigo, nombre, marca, precio, existencias, proveedor_codigo = campos
                    proveedor = self.buscar_proveedor(proveedor_codigo)
                    if proveedor:
                        self.agregar_producto(Producto(codigo, nombre, marca, float(precio), int(existencias), proveedor))
        except FileNotFoundError:
            print("El archivo no existe.")
def buscar_proveedor(self, codigo):
        # Implementa la búsqueda de proveedores según su código
        #  Mantener una lista de proveedores en esta clase o cargarlos desde un archivo similar al inventario
        # Retorna el proveedor encontrado o None si no existe
        pass





