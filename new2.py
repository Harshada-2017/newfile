books = {}

def add_book():
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

    print("Book added successfully!")

def display_books():
    if not books:
        print("No books available.")
        return

    for book_id, details in books.items():
        print("\nBook ID:", book_id)
        print("Title:", details["title"])
        print("Author:", details["author"])
        print("Available:", details["available"])

def search_book():
    book_id = int(input("Enter Book ID: "))

    if book_id in books:
        print("Book Name:", books[book_id]["title"])
        print("Author:", books[book_id]["author"])
    else:
        print("Book not found!")

def borrow_book():
    book_id = int(input("Enter Book ID: "))

    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book borrowed successfully!")
        else:
            print("Book is already borrowed.")
    else:
        print("Book not found!")

def return_book():
    book_id = int(input("Enter Book ID: "))

    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully!")
    else:
        print("Book not found!")

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        borrow_book()
    elif choice == 5:
        return_book()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")