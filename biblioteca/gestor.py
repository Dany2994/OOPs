class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True # Inicialmente, el libro esta disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False
    
    def devolver(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def __str__(self):
        estado = 'disponible' if self.disponible else "prestado"
        return f"'{self.titulo}'por {self.autor}, (ISBN: {self.isbn}) - {estado}"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libro_prestados = []

    def prestar_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro):
        if libro in self.libro_prestados and libro.devolver():
            self.libro_prestados.remove(libro)

    def __str__(self):
        libros = ", ".join([libro.titulo for libro in self.libro_prestados])
        return f"Usuario: {self.nombre} (ID: {self.user_id}) - Libros prestados: {libros}"

class Biblioteca:
    def __init__(self, nombre, direccion, catalogo, usuarios):
        self.nombre = nombre
        self.direccion = direccion
        self.catalogo = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for titulo in self.catalogo:
            if  libro.titulo.lower() == titulo.lower():
                return libro
            return None
        
    def prestar_libro(self, usuario, libro):
        if usuario.prestar_libro(libro):
            return  f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}."
        return f"El libro '{libro.titulo}' no está disponible."
    
    def devolver_libro(self, usuario, libro):
        if usuario.devolver_libro(libro):
            return f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}."
        return f"El libro '{libro.titulo}' no fue prestado a {usuario.nombre}."
