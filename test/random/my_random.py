import random
import torch
from xingyun.random.set_random_seed import set_random_seed
from xingyun.random.my_random import MyRandom
import unittest

def randomint():
    a = random.randint(0,23333)
    b = int( float( torch.randn(1) ) * 1000 )
    return a * 23333 + b

class TestMyRandom(unittest.TestCase):
    def test_main(self):
        set_random_seed(2333)
        rn_1 = randomint()
        rn_2 = randomint()

        set_random_seed(2333)
        rn_3 = randomint()
        with MyRandom():
            rand_list = [randomint() for _ in range(10)]
        rn_4 = randomint()

        self.assertTrue( rn_1 == rn_3 )
        self.assertTrue( rn_2 == rn_4 )

        print ("my_random good.")
        

if __name__ == "__main__":
    unittest.main()
