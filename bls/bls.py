#---------------------------------------------------------------#
#          THIS IS AN EXAMPLE CODE TO HELP YOU GET STARTED      #
#---------------------------------------------------------------#
from utils import Fp, random_fp, bls12_381, G1, sha256, hash_to_G2

# Defining the field Fp of order equal to the order of the group G1
# Fp = FiniteField(bls12_381.curve_order, 1)

# Generating a pair of bls (non-threshold) key pair (sk, pk)
def generate_bls_keys() -> 'tuple[Fp, bls12_381.G1]':
    sk = random_fp()
    pk = bls12_381.multiply(G1, sk.n) 
    return sk, pk

# Signing a message msg with signing/secret key sk
def sign(msg: str, sk: Fp) -> bls12_381.G2:
    hg2 = hash_to_G2(msg, b'', sha256)
    return bls12_381.multiply(hg2, sk.n)

# Verifying a signature for a message msg using the public key pk 
# NOTE: In the py_ecc library the notation for pairing is e(g2, g1) 
# i.e., the first element belongs to G2 and the second element belongs to G1
def verify(msg: str, signature: bls12_381.G2, pk: bls12_381.G1) -> bool:
    hg2 = hash_to_G2(msg, b'', sha256)
    return bls12_381.pairing(signature, G1) == bls12_381.pairing(hg2, pk)
