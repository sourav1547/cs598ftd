

def reliablebroadcast(sid, pid, N, t, leader, input, predicate, receive, send):
    """
    :param int pid: ``0 <= pid < N``
    :param int N:  at least 3
    :param int t: maximum number of malicious nodes , ``N >= 3t + 1``
    :param int leader: ``0 <= leader < N``
    :param input: if ``pid == leader``, then :func:`input()` is called
        to wait for the input value
    :param receive: :func:`receive()` blocks until a message is
        received; message is of the form::
            (i, (tag, ...)) = receive()

        where ``tag`` is one of ``{"PROPOSE", "ECHO", "READY"}``
    :param send: sends (without blocking) a message to a designed
        recipient ``send(i, (tag, ...))``

    :return str: ``m``
    """
    
    def multicast(o):
        for i in range(N):
            send(i, o)

    if pid == leader:
        m = input()  # block until an input is received
        multicast(("PROPOSE", m))

    while True:  # main receive loop
        sender, msg = receive()
        if msg[0] == 'PROPOSE':            
            (_, proposal) = msg
            if sender != leader:
                print("PROPOSE message from other than leader:", sender)
                continue
            return proposal
