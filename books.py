# Library Management System

library = []

# Function to add books
def add_book():
    book = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    data = {
        "book": book,
        "author": author
    }

    library.append(data)
    print("Book Added Successfully!\n")


# Function to search books
def search_book():
    search = input("Enter Book Name to Search: ")

    found = False

    for item in library:
        if item["book"].lower() == search.lower():
            print("\nBook Found")
            print("Book Name :", item["book"])
            print("Author    :", item["author"])
            found = True
            break

    if not found:
        print("Book Not Found!\n")


# Main Program
while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. View Books")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        print("\nLibrary Books")

        if len(library) == 0:
            print("No Books Available\n")
        else:
            for i, item in enumerate(library, start=1):
                print(i, ".", item["book"], "-", item["author"])
            print()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice!\n")
