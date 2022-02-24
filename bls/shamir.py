from utils import Fp, bls12_381

# Uncomment below if you want to work with field of smaller size.
# Fp = FiniteField(53,1)

# TODO: return a vector of shares [s1, s2, ..., sn]
# INPUT:: n: number of nodes, t: threshold, secret, and a field
# OUTPUT:: Shamir secret shares [(1, s1), (2,s2), ..., (n,sn)] where each si is a field element
def gen_share(n: int, t: int, secret: Fp, field=Fp) -> 'list[(int, Fp)]':
    return None

# TODO: interpolate and return the point at 0
# INPUT:: shares: a list of tuples [(x1,a), (x2,b),...]
# OUTPUT:: P(0): here P(x) is the polynomial defined by the shares
def interpolate_at_0(shares : 'list[(int, Fp)]') -> Fp:
    return None