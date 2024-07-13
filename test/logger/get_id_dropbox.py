from xingyun.logger.getid import get_id
from xingyun.logger import get_dropbox_dataacess
import unittest

class TestGetID(unittest.TestCase):
    def test_main(self):
        data_acc = get_dropbox_dataacess().cd("test/xingyun/get_id")
        id_1 = get_id("test", data_acc)
        id_2 = get_id("test", data_acc)

        print (id_1)
        print (id_2)

        assert int(id_2) == int(id_1) + 1

        print("getid dropbox version good.")

if __name__ == "__main__":
    unittest.main()