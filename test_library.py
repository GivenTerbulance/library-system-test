import pytest 

from library import Book, Member, Library

#Unit testing 
def test_is_available():
    b = Book("Atomic Habits", "James Clear", 3)
    assert b.is_available() is True
    b.borrow()
    b.borrow()
    b.borrow()
    assert b.is_available() is False
    
def test_book_negative_copies():
    with pytest.raises(ValueError):
        Book("Spells", "Unknown", -1)
#logic testing
def test_member_cannot_borrow_more_than_3():
    m = Member("Given")
    books = [Book(f"Book{i}", "Author", 1) for i in range(3)]
    for book in books:
        m.borrow_book(book)
    with pytest.raises(ValueError):
        m.borrow_book(Book("Extra Book", "Author", 1))

# Boundary test 
def test_boundary_exactly_3_books_alllowed():
    m = Member("Wamaanda")
    books = [Book(f"Book{i}", "Author", 1) for i in range(3)]
    for book in books:
        m.borrow_book(book)
        assert len(m.borrowed_books) == 3

#error handling tests 
def test_borrow_book_not_found():
    lib = Library()
    lib.register_member("Elias")
    with pytest.raises(ValueError, match="Book 'Missing Book' not found"):
        lib.borrow_book("Elias", "Missing Book")

def test_member_not_found():
    lib = Library()
    with pytest.raises(ValueError, match="Member 'Calvin' not found"):
        lib.borrow_book("Calvin", "Some Book")

#Intergration-OOP test
def test_library_borrow_and_return():
    lib = Library()
    lib.add_book("richdadpoordad", "Robert Kiyosaki", 1)
    lib.register_member("Kabisi")

    lib.borrow_book("Kabisi", "richdadpoordad")
    assert lib.books["richdadpoordad"].copies == 0

    lib.return_book("Kabisi", "richdadpoordad")
    assert lib.books["richdadpoordad"].copies == 1

print("Debug: Imported Book class:", Book)

    