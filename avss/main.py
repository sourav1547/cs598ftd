from tests.test_rbc import test_rbc
from tests.test_avss import test_avss_share

def test_rbc_main(N, t, seed):
    test_rbc(N=N, t=t, msg=b'Welcome to CS598FTD', seed=seed)

def test_avss_main(N, t, seed):
    test_avss_share(N=N, t=t, g=None, secret=5, seed = seed)

if __name__ == '__main__':
    test_rbc_main(4, 1, None)
    # test_avss_main(4, 1, None)