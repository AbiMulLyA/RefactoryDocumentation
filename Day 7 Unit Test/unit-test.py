import unittest
from code import Kalkulator as K

class KalkulatorTest(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(K.tambah(1,2), 3)

    def test_kuadrat(self):
        self.assertEqual(K.kuadrat(2), 4)

    def test_value(self):
        self.assertRaises(ValueError, K.kuadrat, -1)
    
    def test_type(self):
        self.assertRaises(TypeError, K.kuadrat, "1")

# cek = help(unittest.TestCase)

if __name__ == "__main__":
    unittest.main()
        