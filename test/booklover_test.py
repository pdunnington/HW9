import unittest
from booklover import BookLover
student1 = BookLover('Patrick','ped9zgx@virginia.edu','Scifi') 

class BookLoverTestSuite(unittest.TestCase):
        def test_1_add_book(self):
            student1.add_book('To Kill a Mockingbird',5)
            self.assertTrue(student1.has_read('To Kill a Mockingbird'))
        def test_2_add_book(self):
            student1.add_book('To Kill a Mockingbird',5)
            expected = 1
            self.assertEqual(len(student1.book_list['book_name']),expected)
        def test_3_has_read(self):
            student1.has_read('To Kill a Mockingbird')
            self.assertTrue(student1.has_read)
        def test_4_has_read(self):
            self.assertFalse(student1.has_read('Harry Potter'))
        def test_5_num_books_read(self):
            student1.add_book('What If',2)
            student1.add_book('Physics for Dummies',3)
            student1.add_book('Warmth Disperses and Time Passes',5)
            expected = 5
            self.assertEqual(student1.num_books_read(), expected)
        def test_6_fav_books(self):
            student1.add_book('James and the Giant Peach',4)
            self.assertTrue(len(student1.book_list['book_rating']>3), 2)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)       