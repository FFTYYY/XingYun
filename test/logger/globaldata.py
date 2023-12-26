import unittest
from xingyun.logger.globaldata import GlobalDataManager, make_hook_logger
from xingyun.logger.globaldata import Logger
from random import randint
import pdb
import os

class TestGlobalData(unittest.TestCase):
    def test_main(self):
        logger = Logger()
        G = GlobalDataManager("test/1", [make_hook_logger(logger)])

        G.set("haha", 233, force_timestamp = 0)
        G.set("haha", 1234)

        assert G.get("haha") == 1234
        assert G.get("haha", time_stamp = 0) == 233
        assert G.get_timestamp("haha") == 1

        G.log("fuck!")
        assert G.get(G.LOGGER_KEY) == "fuck!"

        v_1 = G.log_code()
        v_2 = G.log_code()
        assert v_1 == v_2

        code = G.get(G.CODE_KEY)
        assert isinstance(code, dict)
        assert isinstance(code["test/logger/test.txt"], str)
        assert code["test/logger/test.txt"].strip() == "haha!"

        sub_name = randint(0,2333333)
        os.system(f"python -m test.logger.globaldata_sub {sub_name}")
        GG = GlobalDataManager(f"test/test_sub_{sub_name}", [make_hook_logger(logger)])
        assert GG.get("fuck") == 111
        assert GG.get_timestamp("fuck") == 0

        print("globaldata good.")

if __name__ == "__main__":
    unittest.main()
