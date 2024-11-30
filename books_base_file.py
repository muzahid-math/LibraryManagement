import add_books
import save_to_file
import view_all_books
import delete_by_title
import book_info_from_file
import update_by_title

print('Welcome to Library Management System.')
books = []
while True:
    print('\t0. Exit. ')
    print('\t1. Add a Book. ')
    print('\t2. Save book to a file. ')
    print('\t3. View all books. ')
    print('\t4. Delete a book. ')
    print('\t5. Update a book. ')
    choice = input("\nSelect your choice: \n")
    
    if choice == "0":
        print("Thanks for using Library Management System.")
        break
    elif choice == "1":
        add_books.added_book(books)
        print('Books were added succesfully...')
    elif choice == "2":
        save_to_file.save_books(books)
        print('Books were saved into a file succesfully...')
    elif choice == "3":
        view_all_books.view_from_file()
    elif choice == "4":
        data = book_info_from_file.book_info()
        delete_by_title.delete_a_book(data)
    elif choice == '5':
        data = book_info_from_file.book_info()
        update_by_title.update_a_book(data)
    else:
        print('Enter a valid choice between 0 to 5.')

