import csv
def view_from_file():
  try:
      with open('books.csv','r') as f:
        book_list =   csv.reader(f)
        if book_list != []:
          for index, book in enumerate(book_list, start=1):
            print(f"book-{index} info: {book}")
  except Exception as e:
     print(f"Books data are empty. Add Data first..")
