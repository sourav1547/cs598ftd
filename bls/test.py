import bls
from utils import Fp, bls12_381, multiply, G1

# test_keygen tests whether the key generation process is followed correctly or not
def test_keygen():
    sk, pk = bls.generate_bls_keys()
    assert(pk == multiply(G1, sk.n))

# test_bls signs a message and then verifies the signature. It also test the signature with a differnt message
def test_bls():
    sk, pk = bls.generate_bls_keys()
    msg = str.encode("hello")
    sigma = bls.sign(msg, sk)
    assert(bls.verify(msg, sigma, pk))
    msg = str.encode("world")
    assert(not bls.verify(msg, sigma, pk))

def test_bls_ths_keygen():
    # Feel free to write your own test case (NOT MANDETORY for homework)
    assert(True)

def test_bls_ths():
    # Feel free to write your own test case (NOT MANDETORY for homework)
    assert(True)

if __name__ == "__main__":
    test_keygen()
    test_bls()

