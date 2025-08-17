class Book:
    def __init__(self, title, author, copies):
        if copies < 0:
            raise ValueError("Number of copies can not be negative")
        self.title = title
        self.author = author
        self.copies = copies

        def is_available(self):
            return self.copies > 0
        
        def borrow(self):
            if self.copies <= 0:
                raise ValueError(f"No copies of this book, {self.title}, available")
            self.copies -= 1
        def return_book(self):
            self.copies += 1

class Member:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= 3: #constraint
            raise ValueError(f"{self.name} cannot borrow more than 3 books")
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise ValueError(f"{self.name} has not borrowed this book: {book.title}")
        book.return_book()

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title,author, copies):
        if title in self.books:
            self.books[title].copies += copies
        else:
            self.books[title] = Book(title, author, copies)
    def register_member(self, name):
        if name in self.members:
            raise ValueError(f"The member, {name} already exist")
        self.members[name] = Member(name)

    def borrow_book(self, member_name, book_title):
        if member_name not in self.members:
            raise ValueError(f"Member {member_name}, not found")

        if book_title not in self.books:
            raise ValueError(f"Book '{book_title}', not found")
        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)
    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            raise ValueError(f"Member, '{member_name}' not found ")
        if book_title not in self.books:
            raise ValueError(f"Book, '{book_title}', not found")
        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)


        






