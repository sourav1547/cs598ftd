from utils import Fp, bls12_381

# Uncomment below if you want to work with field of smaller size.
# Fp = FiniteField(53,1)

# TODO: return a vector of shares [s1, s2, ..., sn]
# INPUT:: n: number of nodes, t: threshold, secret, and a field
# OUTPUT:: Shamir secret shares [s1, s2, ..., sn] where each si is a field element
def gen_share(n: int, t: int, secret: Fp, field=Fp) -> list[Fp]:
    return None

# TODO: interpolate and return the point at 0
# INPUT:: shares: a list of tuples [(1,a), (2,b), (4,c)]
# OUTPUT:: P(0): here P(x) is the polynomial defined by the shares
def interpolate_at_0(shares : list[(int, Fp)]) -> Fp:
    return None

# TODO: interpolate and return the point at an j
# INPUT:: shares: a list of tuples [(1,a), (2,b), (4,c)] and an index j
# OUTPUT:: P(j): the polynomial defined by the shares
def interpolate_at_j(shares: list[(int, Fp)], j: int) -> Fp:
    return None

# TODO: Interpolate in the exponent at 0, i.e., compute G1^{P(0)} 
# where P(x) is the polynomial defined by the shares
# INPUT:: shares: a list of tuples [(1,G1^a), (2,G1^b), (4,G1^c)] and index j
# OUTPUT:: G1^P(0): here P(x) is the polynomial defined by the shares
# NOTE: You need to work with `Fp = FiniteField(bls12_381.curve_order, 1)` for this function
def interpolate_at_g0(shares: list[(int, bls12_381.G1)]) -> bls12_381.G1:
    return None

# TODO: Interpolate in the exponent at an index j, i.e., compute G1^{P(j)} 
# where P(x) is the polynomial defined by the shares
# INPUT:: shares: a list of tuples [(1,G1^a), (2,G1^b), (4,G1^c)] and index j
# OUTPUT:: G1^P(j): here P(x) is the polynomial defined by the shares
# NOTE: You need to work with `Fp = FiniteField(bls12_381.curve_order, 1)` for this function
def interpolate_at_gj(shares: list[(int, bls12_381.G1)], j: int) -> bls12_381.G1:
    return None