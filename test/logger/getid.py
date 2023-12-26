from xingyun.logger.getid import get_id
import unittest

class TestGetID(unittest.TestCase):
    def test_main(self):
        id_1 = get_id("test")
        id_2 = get_id("test")

        print (id_1)
        print (id_2)

        assert int(id_2) == int(id_1) + 1

        print("getid good.")

if __name__ == "__main__":
    unittest.main()