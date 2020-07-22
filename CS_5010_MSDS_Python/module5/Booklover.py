
class BookLover():

    def __init__(self, name, email, numBooks = 0, favGenre = "", bookLst = []):
        self.name = name
        self.email = email
        self.numBooks = numBooks
        self.favGenre = favGenre
        self.bookLst = bookLst 
        if len(self.bookLst) != self.numBooks:
            self.numBooks = len(self.bookLst)
            print(f"FYI we only counted {self.numBooks} in their book list")
    
    def __str__(self):
        retstr = f"Name: {self.name} | Email: {self.email} | " \
            + f"numBooks: {self.numBooks} | favGenre: {self.favGenre}"
        return retstr
    
    def addBook(self, bookName, rating):
        book_names = [x[0] for x in self.bookLst]
        if not isinstance(rating, int):
            print("The Rating must be a number between 0 and 5.")
        elif bookName in book_names:
            self.bookLst.append((bookName, rating))
            self.numBooks += 1
            print(f"{bookName} has been added to {self.name}'s book list!")
        if len(self.bookLst) != self.numBooks:
            self.numBooks = len(self.bookLst)

    def hasRead(self, bookName):
        book_names = [x[0] for x in self.bookLst]
        bisin = bookName in book_names
        return bisin
    
    def numBooksRead(self):
        return self.numBooks

    def favBooks(self):
        return [x[0] for x in self.bookLst if x[1] > 3]

