from xingyun.argparser.mynamespace import MyNamespace
import unittest

class TestMyNamespace(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def test_main(self):
        d = {
            "model": "UGNN",
            "num_layers": 3,
            "model/GNN_spec/prop_method": "message",
            "model/CNN_spec/bn": None,
            "optim/lr": 0.1,
            "optim/wd": 5e-5,
            "no_activation": True
        }

        C = MyNamespace(d)

        self.assertTrue( C.model == "UGNN" )
        self.assertTrue( C.num_layers == 3 )
        self.assertTrue( C.model.GNN_spec.prop_method == "message" )
        self.assertTrue( C.model.CNN_spec.bn == None )
        self.assertTrue( C.optim.lr == 0.1 )
        self.assertTrue( C.optim.wd == 5e-5 )
        self.assertTrue( C.no_activation == True )

        print (C.to_dict())

    
if __name__ == "__main__":
    unittest.main()
