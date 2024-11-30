def save_books(books):
  with open('books.csv','w') as f:
    for b in books:
      f.write(f"{b['title']},{b['author']},{b['isbn']},{b['year']},{b['price']},{b['quantity']}\n")
