import unittest
from list import List

class TestList(unittest.TestCase):
    
#    def test_append(self):
#       tlist = List()
#        tlist.append(5)
#        tlist.append(20)
#        tlist.append(69)
#        tlist.append(-5)
#
#        self.assertEqual(tlist, exp)

    def test_get(self):
        tlist = List()
        tlist.append(5)
        tlist.append(20)
        tlist.append(69)
        
        self.assertEqual(tlist.get(2), 69)
        self.assertEqual(tlist.get(0), 5)
        with self.assertRaises(IndexError):
            tlist.get(15)
    
    def test_len(self):
        tlist = List()
        tlist.append(5)
        tlist.append(20)
        tlist.append(69)
        
        self.assertEqual(tlist.len(), 3)
        
    def test_insert(self):
        tlist = List()
        tlist.append(5)
        tlist.append(20)
        tlist.append(69)
        
        tlist.insert(2, 55)
        self.assertEqual(tlist.get(2), 55)
        
        with self.assertRaises(IndexError):
            tlist.insert(15, 55)
        
if __name__ == '__main__':
    unittest.main()