#Crearemos un sistema de gestión de una biblioteca.
#Este proyecto será un buen ejercicio para practicar la programación orientada a objetos y otras habilidades como el manejo de excepciones y la persistencia de datos.

#Clases
#Book: Representa un libro en la biblioteca.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = True
            return True
        return False
    
    def return_book(self):
        self.available = True

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else 'Borrowed'
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"
    
#Member, representa un miembro de la biblioteca
class member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"
    
#Esta clase gestionará la colección de libros y miembros, y permitirá operaciones como agregar libros, registrar miembros, prestar libros, etc.

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return book
    
    def register_member(self, name):
        member = member(name)
        self.members.append(member)
        return member
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
            return None
    
    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        
    def list_books(self):
        for book in self.books:
            print(book)
        
    def list_members(self):
        for member in self.members:
            print(member)

#Denifir la funcion principal 

def main():
    library = Library()

    while True:
        print("\nLibrary Managent System")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Book")
        print("6. List Members")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print("Book added successfully.")
        elif choice == "2":
            name = input("Enter member name: ")
            library.register_member(name)
            print("Member registered successfully.")
        elif choice == "3":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = library.find_book(book_title)
            if member and book:
                if member.borrow_book(book):
                    print("Book borrowed sucessfully")
                else:
                    print("Member or book not found.")
            else:
                print("Member or Book not: ")
        elif choice == "4":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            member = library.find_member(member_name)
            book = library.find_book(book_title)
            if member and book:
                if member.return_book(book):
                    print("Book Retirned successfully.")
                else:
                    print("The member does not have this book.")
            else:
                print("Member or book not found.")
        elif choice == "5":
            print("Listing  all books")
            library.list_books()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()