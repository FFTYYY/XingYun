from xingyun.logger.globaldata import GlobalDataManager, make_hook_logger
from xingyun.logger.globaldata import Logger
import pdb
import sys

def main():
    name = sys.argv[1]

    logger = Logger()
    G = GlobalDataManager(f"test/test_sub_{name}", [make_hook_logger(logger)])

    G.set("fuck_sub", 111, force_timestamp = 0)
    G.upload_data()


if __name__ == "__main__":
    main()