import unittest
from xingyun.universal.import_module import my_import_module as import_module
import warnings
class TestImportModule(unittest.TestCase):
    def test_main(self):
        
        torch = import_module("torch")
        cuda  = import_module("torch.cuda")
        backends = import_module("torch.backends")

        assert torch is not None
        assert cuda is not None
        assert backends is not None

        torch.manual_seed(2333)
        cuda.manual_seed_all(2333)
        backends.cudnn.deterministic = True
        backends.cudnn.benchmark = False

        import torch as tc
        a = tc.randint(0,123,(5,))
        torch.manual_seed(2333)
        b = tc.randint(0,123,(5,))

        self.assertTrue( (a == b).all() )

    def test_not_exists(self):
        def _sub():
            haha = import_module("haha")
            self.assertTrue(haha is None)

        self.assertWarns(UserWarning, _sub )


if __name__ == "__main__":
    unittest.main()
