from save_to_file import save_books
def delete_a_book(data):
    if data != []:
        print('Before delete: ',data)
        remove_by_title = input('Enter a title to delete: ')
        data = [item for item in data if item['title'] != remove_by_title]
        print('After delete a book: ',data)
        save_books(data)
        print('all book status changed and saved to file successfully')
    else:
        print('No book available for remove, create first.')