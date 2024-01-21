class library:
    def __init__(self):
        self.count = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.count = len(self.books)

    def info(self):
        print(f"There are {self.count} books in library. They are")
        for book in self.books:
            print(book)

a = library()
a.addbook("HARRY POTTER1")
a.addbook("HARRY POTTER2")
a.addbook("HARRY POTTER3")
a.info()
            
