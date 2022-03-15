import random

import gevent
from gevent import Greenlet
from gevent.queue import Queue

from network.router import simple_router
from core.rbc import reliablebroadcast

def test_rbc(N=4, t=1, msg=b"Hello!", leader=None, seed=None):
    # Test everything when runs are OK
    #if seed is not None: print 'SEED:', seed
    sid = 'sidA'
    rnd = random.Random(seed)

    if leader is None: leader = rnd.randint(0,N-1)
    sends, recvs = simple_router(N, seed=seed)
    threads = []
    leader_input = Queue(1)

    def predicate(msg):
        return True
        
    for i in range(N):
        input = leader_input.get if i == leader else None
        th = Greenlet(reliablebroadcast, sid, i, N, t, leader, input, predicate, recvs[i], sends[i])
        th.start()
        threads.append(th)

    leader_input.put(msg)
    gevent.joinall(threads)
   

    for th in threads:
        print(th.value)
    assert [th.value for th in threads] == [msg]*N



