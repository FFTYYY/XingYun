from argparse import Namespace

a = Namespace(a = 12, b = "3")
a.__dict__["c.2"] = 100

print (a.c)