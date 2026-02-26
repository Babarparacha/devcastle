class Books:
 def __init__(self,pages):
    self.pages=pages
class Library:
    def __init__(self,books):
        self.books=books
    def add_new(self):
        total=0
        for book in self.books:
            total+=book.pages
        return total
b1=Books(300)
b2=Books(600)
lib=Library([b1,b2])
print(lib.add_new())
    