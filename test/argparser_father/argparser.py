from xingyun.argparser import ArgumentParser, PreCondition, MyDict
import unittest
import pdb

def make_parser():
    argp = ArgumentParser()

    # ---- model ---- 
    argp.add_argument("model/model"     , type = str, default = "TWIRLS", verify = lambda v: v in ["TWIRLS", "UGNN", "IGNN", "CNN"] )
    argp.add_alias   ("model" , "model/model")

    argp.add_argument("model/num_layers", type = int, default = 12  , aliases = ["num_layers"])

    with PreCondition(["model"], lambda model: model in ["TWIRLS" , "UGNN", "IGNN"]):
        argp.add_argument("model/GNN_spec/prop_method", type = str, default = "message", verify = lambda v: v in ["message", "identity"]  )

    with PreCondition(["model"], lambda model: model in ["CNN"]):
        argp.add_bool    ("model/CNN_spec/bn")
    

    # ---- optim ---- 
    argp.add_argument("optim/lr", type = float, default = 0.1, verify = lambda v: v >= 0  )
    argp.add_argument("optim/wd", type = float, default = 0.0, verify = lambda v: v >= 0  )

    # ---- general ----
    argp.add_bool    ("no_activation")

    return argp

class TestArgParser(unittest.TestCase):
    def setUp(self) -> None:
        self.argp = make_parser()
        return super().setUp()
    
    def test_main(self):
        argv = [
            "--model=UGNN" , 
            "--num_layers=3", 
            "--model/GNN_spec/prop_method=message", 
            "--model/CNN_spec/bn", 
            "--optim/lr=0.1", 
            "--optim/wd=5e-5", 
            "--no_activation"
        ]

        C = self.argp.parse(argv)

        print (C.sub("model"))

        self.assertTrue( C.sub("model")["model"] == "UGNN" )
        self.assertTrue( C["model"] == "UGNN" )
        self.assertTrue( C.sub("model")["num_layers"] == 3 )
        self.assertTrue( C.sub("model")["GNN_spec/prop_method"] == "message" )
        self.assertTrue( C.sub("model")["CNN_spec/bn"] == None )
        self.assertTrue( C("model")["CNN_spec/bn"] == C("model")("CNN_spec")["bn"] )
        self.assertTrue( C.sub("optim")["lr"] == 0.1)
        self.assertTrue( C.sub("optim")["wd"] == 5e-5 )
        self.assertTrue( C["no_activation"] == True )

        CN = self.argp.parse_namespace(argv)
        self.assertTrue( CN.model == "UGNN" )
        self.assertTrue( CN.num_layers == 3 )
        self.assertTrue( CN.model.GNN_spec.prop_method == "message" )
        self.assertTrue( CN.model.CNN_spec.bn == None )
        self.assertTrue( CN.optim.lr == 0.1 )
        self.assertTrue( CN.optim.wd == 5e-5 )
        self.assertTrue( CN.no_activation == True )

    def test_raise(self):
        argv = [
            "--model=UGNN" , 
            "--model/num_layers=3", 
            "--model/GNN_spec/prop_method=UGNN_message", 
            "--model/CNN_spec/bn", 
            "--optim/lr=0.1", 
            "--optim/wd=5e-5", 
            "--no_activation"
        ]
        self.assertRaises(RuntimeError, lambda : self.argp.parse(argv))

    def test_default(self):
        argv = [
            "--model=CNN" , 
            "--num_layers=12", 
            "--model/GNN_spec/prop_method=UGNN_message", 
            "--model/CNN_spec/bn", 
            "--optim/lr=0.1", 
        ]
        C = self.argp.parse(argv)

        self.assertTrue( C.sub("model")["model"] == "CNN" )
        self.assertTrue( C.sub("model")["num_layers"] == 12 )
        self.assertTrue( C.sub("model")["GNN_spec/prop_method"] == None )
        self.assertTrue( C.sub("model")["CNN_spec/bn"] == True )
        self.assertTrue( C.sub("optim")["lr"] == 0.1)
        self.assertTrue( C.sub("optim")["wd"] == 0.0 )
        self.assertTrue( C["no_activation"] == False )

        CN = self.argp.parse_namespace(argv)

        self.assertTrue( str(CN) == "<xingyun: Arguments>" )
        self.assertTrue( CN.model == "CNN" )
        self.assertTrue( CN.num_layers == 12 )
        self.assertTrue( CN.model.GNN_spec.prop_method == None )
        self.assertTrue( CN.model.CNN_spec.bn == True )
        self.assertTrue( CN.optim.lr == 0.1 )
        self.assertTrue( CN.optim.wd == 0.0 )
        self.assertTrue( CN.no_activation == False )

    
if __name__ == "__main__":
    unittest.main()
