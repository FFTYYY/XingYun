import unittest
from .universal import *
from .random import *
from .time import *
from .cloud import *
from .logger import *

if __name__ == "__main__":
    testsuite = unittest.TestLoader().discover(".")
    unittest.TextTestRunner(verbosity = 2).run(testsuite)