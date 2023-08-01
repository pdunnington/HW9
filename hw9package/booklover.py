import pandas
class BookLover():
    num_books=0
    book_list = pandas.DataFrame({'book_name':[],'book_rating':[]})
    def __init__(self,name,email,fav_genre): 
        self.name = str(name)
        self.email = str(email)
        self.fav_genre = str(fav_genre)
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name']:
            print("book's already here")
            self.num_books+=1
        else: 
            books = pandas.DataFrame({'book_name':[book_name],
                                     'book_rating':[rating]})
            self.book_list = pandas.concat([self.book_list, books], ignore_index=True)
            self.num_books+=1
    def has_read(self, book_name):
        books = book_name in self.book_list['book_name'].values
        return books
    def num_books_read(self):
        return self.num_books
    def fav_books(self):
        favorites = self.book_list['book_rating']>3
        return favorites
            
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()
