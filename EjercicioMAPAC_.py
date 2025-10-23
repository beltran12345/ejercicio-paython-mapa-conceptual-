# Clase Servidor
class Servidor:
    def muestra_pagina(self):
        return "Página mostrada."

    def envia_sugerencia(self):
        return "Sugerencia enviada desde el servidor."

    def envia_datos_de_compra(self):
        return "Datos de compra enviados al servidor."

    def envia_datos_de_venta(self):
        return "Datos de venta enviados al servidor."


# Clase Procesador
class Procesador:
    def mandar_datos_de_venta(self):
        return "Datos de venta enviados por el procesador."

    def mandar_articulo_online(self):
        return "Artículo online enviado por el procesador."

    def envia_sugerencia_administrador(self):
        return "Sugerencia enviada al administrador."

    def modificar_stock(self):
        return "Stock modificado."

    def realizar_cobro(self):
        return "Cobro realizado."

    def realizar_pago(self):
        return "Pago realizado."

    def actualiza_catalogo(self):
        return "Catálogo actualizado."

    def realiza_busqueda(self):
        return "Búsqueda realizada por el procesador."


# Clase Recolector
class Recolector:
    def envia_novedades(self):
        return "Novedades enviadas por el recolector."


# Clase Indexador
class Indexador:
    def actualiza_almacen(self):
        return "Almacén actualizado por el indexador."

    def envia_resultado_busqueda(self):
        return "Resultado de búsqueda enviado."


# Clase Usuario
class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        return "Sugerencia enviada por el usuario."

    def comprar(self):
        return "Compra realizada por el usuario."

    def vender(self):
        return "Usuario vendió un producto."

    def realizar_clamacion(self):
        return "Reclamación realizada por el usuario."

    def ver_info(self):
        return (
            f"Nombre: {self.nombre} {self.apellido}\n"
            f"Número de cuenta: {self.cuenta}\n"
            f"Dirección: {self.direccion}\n"
            f"Login: {self.login}\n"
            f"Contraseña: {self.password}"
        )


# Clase Producto
class Producto:
    def __init__(self, nombre, precio, editorial, fecha_edicion, preferencias):
        self.nombre = nombre
        self.precio = precio
        self.editorial = editorial
        self.fecha_edicion = fecha_edicion
        self.preferencias = preferencias

    def ver_catalogo(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Editorial: {self.editorial}\n"
            f"Fecha de edición: {self.fecha_edicion}\n"
            f"Preferencias: {self.preferencias}"
        )

    def vender(self):
        return "Producto vendido."

    def comprar(self):
        return "Producto comprado."


# Clase Libro
class Libro:
    def __init__(self, genero):
        self.genero = genero

    def ver_genero(self):
        return f"Género del libro: {self.genero}"


# Clase Revista
class Revista:
    def __init__(self, categoria):
        self.categoria = categoria

    def ver_categoria(self):
        return f"Categoría de la revista: {self.categoria}"


# Clase ArticuloDeSegundaMano
class ArticuloDeSegundaMano:
    def __init__(self, clasificacion, tema, vendedor):
        self.clasificacion = clasificacion
        self.tema = tema
        self.vendedor = vendedor

    def cambiar_clasificacion(self):
        return "Clasificación del artículo de segunda mano cambiada."


# Clase Novedades
class Novedades:
    def __init__(self, tema):
        self.tema = tema

    def cambiar_clasificacion(self):
        return "Clasificación de novedades cambiada."


# Clase ArticuloOnline
class ArticuloOnline:
    def __init__(self, clasificacion, tema):
        self.clasificacion = clasificacion
        self.tema = tema

    def publicar(self):
        return "Artículo online publicado."


# Clase Editorial
class Editorial:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def vender(self):
        return "Editorial vendió un producto."


# Clase Hilo
class Hilo:
    def busca_novedades(self):
        return "Buscando novedades en segundo plano."


# -------------------- Código Principal --------------------
if __name__ == "__main__":
    # Instancias de clases
    servidor = Servidor()
    procesador = Procesador()
    recolector = Recolector()
    indexador = Indexador()

    usuario = Usuario("aabel", "beltran", "100100010", "Calle12pizarro", "abel666", "password123")
    producto = Producto("Libro de Python", 340000.99, "Editorial JABB", "2024-05-10", "Programación")
    libro = Libro("Educativo")
    revista = Revista("Ciencia")
    articulo_segunda = ArticuloDeSegundaMano("Usado", "Tecnología", "Carlos")
    novedades = Novedades("PROBELMAS DE LA VIDA 2025")
    articulo_online = ArticuloOnline("Nuevo", "IA y TECNOLOGIA")
    editorial = Editorial("MOTOMAMIs", "Av.456", "587-7012")
    hilo = Hilo()

    # Mostrar información
    print(usuario.ver_info())
    print(producto.ver_catalogo())
    print(servidor.muestra_pagina())
    print(servidor.envia_sugerencia())
    print(procesador.realizar_pago())
    print(procesador.realiza_busqueda())
    print(recolector.envia_novedades())
    print(indexador.actualiza_almacen())
    print(usuario.enviar_sugerencia())
    print(usuario.comprar())
    print(usuario.realizar_clamacion())
    print(articulo_segunda.cambiar_clasificacion())
    print(novedades.cambiar_clasificacion())
    print(articulo_online.publicar())
    print(editorial.vender())
    print(hilo.busca_novedades())
    print(libro.ver_genero())
    print(revista.ver_categoria())