import unittest
from xingyun.universal.convert import convert_size_to_bytes

class TestConvert(unittest.TestCase):
    def test_main(self):
        
        self.assertEqual( convert_size_to_bytes("123mb") , 123 * 1024 * 1024 )
        self.assertEqual( convert_size_to_bytes("73 kb") , 73 * 1024 )

        print ("convert good.")

if __name__ == "__main__":
    unittest.main()