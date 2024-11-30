import csv
def book_info():
  try:
    with open('books.csv','r') as f:
      content = list(csv.reader(f))
    book_arr =[]
    for item in content:
      item_rcv_by_line ={}
      item_rcv_by_line['title'] = item[0]
      item_rcv_by_line['author'] = item[1]
      item_rcv_by_line['isbn'] = item[2]
      item_rcv_by_line['year'] = item[3]
      item_rcv_by_line['price'] = item[4]
      item_rcv_by_line['quantity'] = item[5]
      book_arr.append(item_rcv_by_line)
    return book_arr
  except Exception as e:
    return []