from utils import Fp, random_fp, bls12_381, G1, sha256, hash_to_G2

# TODO: To generate a secret key shares of each node and the threshold public keys of every node
# INPUT:: n: total number of nodes; t: fault threshold
# OUTPUT:: bls public key; [threshold secret keys]; [threshold public keys]
# NOTE: Although this function is also returning a list of private keys, in practice the key generation
# protocol will only return the i-th secret share to i-th node.  
def generate_bls_ths_keys(n: int, t: int) -> tuple[bls12_381.G1, list[Fp], list[bls12_381.G1]]:
    return None, None, None

# TODO: To generate a partial signature on the message
# INPUT:: msg: the message, tsk: threshold secret key
# OUTPUT:: partial signature on the message
def partial_sign(msg: str, tsk: Fp) -> bls12_381.G2:
    return None

# TODO: To aggregate a list of parital signatures
# INPUT:: msg: the message; [threshold keys of every node]; [partial signatures]
# OUTPUT:: the bls signature on the message
# NOTE: Some of the partial signatures may be potentially invalid. 
# Perform explicit checks to eliminate invalid partial signatures
def aggregate_signature(msg: str, tpks: list[bls12_381.G1], signatures: list[bls12_381.G2]) -> bls12_381.G2:
    return None

# TODO: Verify the aggregated signature
def verify(msg: str, signature: bls12_381.G2, pk: bls12_381.G1) -> bool:
    return None 


	
