import random

import gevent
from gevent import Greenlet
from gevent.queue import Queue

from network.router import simple_router
from core.beb import besteffortbroadcast

def test_beb(N=4, f=1, msg=b"Hello!", leader=None, seed=None):
    # Test everything when runs are OK
    #if seed is not None: print 'SEED:', seed
    sid = 'sidA'
    rnd = random.Random(seed)

    if leader is None: leader = rnd.randint(0,N-1)
    sends, recvs = simple_router(N, seed=seed)
    threads = []
    leader_input = Queue(1)

    for i in range(N):
        input = leader_input.get if i == leader else None
        th = Greenlet(besteffortbroadcast, sid, i, N, leader, input, recvs[i], sends[i])
        th.start()
        threads.append(th)

    leader_input.put(msg)
    gevent.joinall(threads)
    for th in threads:
        print(th.value)



