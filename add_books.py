def added_book(books):
  title = input('Enter title: ')
  author = input('Enter author name: ')
  isbn = input('Enter ISBN number: ')
  year = int(input('Enter publishing year(integer): '))
  price = int(input('Enter book"s price(integer): '))
  quantity = int(input('Enter book"s quantity(integer): '))

  book_info = {
    'title': title,
    'author': author,
    'isbn': isbn,
    'year': year,
    'price': price,
    'quantity': quantity
  }
  books.append(book_info)
  return books