from xingyun.time.my_clock import my_clock
import time
import unittest

class TestMyClock(unittest.TestCase):
    def test_main(self):
        my_1 = my_clock()
        time.sleep(1.2)
        my_2 = my_clock()

        self.assertTrue(1.15 <= my_2 - my_1 <= 1.25)

        print ("my_clock good.")

if __name__ == "__main__":
    unittest.main()