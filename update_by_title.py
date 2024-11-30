from save_to_file import save_books
def update_a_book(data):
    if data != []:
        print('Before update: ',data)
        update_by_title = input('Enter title to update: ')
        for item in data:
            if item['title'] == update_by_title:
                item['author'] = input('Enter author name: ')
                item['isbn']  = input('Enter isbn: ')
                item['year'] = int(input('Enter year(interger): '))
                item['price'] = int(input('Enter price(interger): '))
                item['quantity'] = int(input('Enter quantity(interger): '))
        save_books(data)
        print('After update a book: ',data)

    else:
        print('No book available for update, create first.')