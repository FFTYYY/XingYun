import unittest
from xingyun.logger.globaldata import GlobalDataManager, make_hook_logger
from xingyun.logger.globaldata import Logger
from xingyun.logger import get_dropbox_dataacess
from random import randint
from egorovsystem import set_variable
import pdb
import os

class TestGlobalDataDropbox(unittest.TestCase):
    def test_main(self):

        logger = Logger()
        G = GlobalDataManager("test/2", [make_hook_logger(logger)], data_access = get_dropbox_dataacess().cd("test/xingyun/globdata"))

        G.set("haha", 233, force_timestamp = 0)
        G.set("haha", 1234)

        self.assertTrue( G.get("haha") == 1234 )
        self.assertTrue( G.get("haha", time_stamp = 0) == 233 )
        self.assertTrue( G.get_timestamp("haha") == 1 )

        G.log("fuck!")
        self.assertTrue( G.get(G.LOGGER_KEY) == "fuck!" )

        v_1 = G.log_code()
        v_2 = G.log_code()
        self.assertTrue( v_1 == v_2 )

        code = G.get(G.CODE_KEY)
        assert isinstance(code, dict)
        assert isinstance(code["test/logger/test.txt"], str)
        self.assertTrue( code["test/logger/test.txt"].strip() == "haha!" )

        sub_name = randint(0,2333333)
        os.system(f"python -m test.logger.globaldata_dropbox_sub {sub_name}")
        GG = GlobalDataManager(f"test/test_sub_{sub_name}", [make_hook_logger(logger)], data_access = get_dropbox_dataacess().cd("test/xingyun/globdata"))
        self.assertTrue( GG.get("fuck_sub") == 111 )
        self.assertTrue( GG.get_timestamp("fuck_sub") == 0 )

        print("globaldata dropbox version good.")

if __name__ == "__main__":
    unittest.main()
