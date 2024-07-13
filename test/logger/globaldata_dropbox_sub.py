from xingyun.logger.globaldata import GlobalDataManager, make_hook_logger
from xingyun.logger.globaldata import Logger
import pdb
import sys
from xingyun.logger import get_dropbox_dataacess
from random import randint
from egorovsystem import set_variable

def main():
    name = sys.argv[1]


    logger = Logger()
    G = GlobalDataManager(f"test/test_sub_{name}", [make_hook_logger(logger)], data_access = get_dropbox_dataacess().cd("test/xingyun/globdata"))

    G.set("fuck_sub", 111, force_timestamp = 0)
    G.upload_data()


if __name__ == "__main__":
    main()