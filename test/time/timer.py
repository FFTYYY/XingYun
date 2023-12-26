from xingyun.time.timer import Timer
import time
import unittest

class TestTimer(unittest.TestCase):
    def test_timer(self):
        
        for i in range(5):
            with Timer("test_1"):
                time.sleep(0.1)
        for j in range(10):
            with Timer("test_2"):
                time.sleep(0.01)

        print(Timer.output_all())

        self.assertTrue( 0.05 <= Timer.get_avg_time("test_1")  <= 0.2)
        self.assertTrue( 0.005 <= Timer.get_avg_time("test_2")  <= 0.02 )
        


if __name__ == "__main__":
    unittest.main()
