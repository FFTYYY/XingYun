from xingyun.argparser.mynamespace import MyNamespace
import unittest

class MyClass:
    def __init__(self, v):
        self.v = v
    def __str__(self):
        return str(self.v)
    

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
            "no_activation": True , 
            "a_val": MyClass(12) , 
            "a_val/sub": 7 , 
        }

        C = MyNamespace(d)


        self.assertTrue( C.model == "UGNN" )
        self.assertTrue( C.num_layers == 3 )
        self.assertTrue( C.model.GNN_spec.prop_method == "message" )
        self.assertTrue( C.model.CNN_spec.bn == None )
        self.assertTrue( C.optim.lr == 0.1 )
        self.assertTrue( C.optim.wd == 5e-5 )
        self.assertTrue( C.no_activation == True )

        self.assertTrue( str( C.a_val ) == "12" )
        self.assertTrue( C.a_val.sub == 7 )

        self.assertTrue( C.__dict__["model"] == "UGNN" )

        print (C.__dict__)

        C.ass = 12
        self.assertTrue( C.ass == 12 )

        Q = C.a_val
        Q.another_sub = 8
        self.assertTrue( str( Q ) == "12" )
        self.assertTrue( Q.another_sub == 8 )
        Q.v = 9
        self.assertTrue( str( Q ) == "9" )
        self.assertTrue( Q.v == 9 )
        self.assertTrue( Q.__dict__.get("v") is None )



        print ("mynamespace good.")

    
if __name__ == "__main__":
    unittest.main()
