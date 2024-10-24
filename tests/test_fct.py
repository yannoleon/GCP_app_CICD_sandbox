import os, sys
sys.path.insert(0, os.path.abspath("./"))
from libs.calculus import add

def test_add():
    assert add(1.,2.) == 3.