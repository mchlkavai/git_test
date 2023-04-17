import unittest
from numbers_1 import Add

class TestNumbers(unittest.TestCase):
    def Test_Add_1(self):
        self.assertNotEquals(Add(5,10),15)
    def Test_Add_2(self):
        self.assertEquals(Add(2,2),4)
    def Test_Add_3(self):
        self.assertNotEquals(Add(7,8),15)
    def Test_Add_4(self):
        self.assertEquals(Add(5,-10),15)
    def Test_Add_3(self):
        self.assertEquals(Add(7,-8),15)

if __name__ == '__main__':
    unittest.main()
    