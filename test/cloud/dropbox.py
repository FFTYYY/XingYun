import unittest
from xingyun.cloud import Dropbox, setdropbox, getdropbox

class TestDropbox(unittest.TestCase):
    def test_main(self):

        data = {"u": 1, "c": 2}

        self.assertTrue( setdropbox( data, "test/uuu/test.pkl")  )
        self.assertTrue( getdropbox("test/uuu/test.pkl")["u"] == 1 )

        print ("dropbox good.")

if __name__ == "__main__":
    unittest.main()