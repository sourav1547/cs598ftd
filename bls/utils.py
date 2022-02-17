import random
from hashlib import sha256
from py_ecc import optimized_bls12_381 as bls12_381
from py_ecc.optimized_bls12_381 import FQ, FQ2, FQ12, G1, G2, add, neg, multiply, eq
from py_ecc.bls.hash_to_curve import hash_to_G2
from finitefield.finitefield import FiniteField


# Defining the field Fp of order equal to the order of the group G1
Fp = FiniteField(bls12_381.curve_order, 1)

def random_fp() -> Fp:
    return Fp(random.randint(0, Fp.p-1))