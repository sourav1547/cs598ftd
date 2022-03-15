"""
-----------------------------------------
|        THIS IS AN EXAMPLE CODE        |
-----------------------------------------

This file implements best effort broadcast protocol.
"""

def besteffortbroadcast(sid, pid, N, leader, input, receive, send):
    
    def multicast(o):
        for i in range(N):
            send(i, o)

    if pid == leader:
        m = input()  # block until an input is received
        assert isinstance(m, (str, bytes))

        multicast(("PROPOSE", m))

    while True:  # main receive loop
        sender, msg = receive()
        if msg[0] == 'PROPOSE':            
            (_, proposal) = msg
            if sender != leader:
                print("PROPOSE message from other than leader:", sender)
                continue
            return proposal
