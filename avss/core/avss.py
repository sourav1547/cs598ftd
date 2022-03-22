from charm.toolbox.ecgroup import ZR


def avss_share(sid, pid, N, t, g, leader, input, receive, send):
    """Asynchronous Verifiable Secret Sharing

    :param int pid: ``0 <= pid < N``
    :param int N:  at least 3
    :param int t: maximum number of malicious nodes , ``N >= 3t + 1``
    :param group g: a generator of the elliptic curve group
    :param int leader: ``0 <= leader < N``
    :param input: if ``pid == leader``, then :func:`input()` is called
        to wait for the input value
    :param receive: :func:`receive()` blocks until a message is
        received; message is of the form::

            (i, (tag, ...)) = receive()
    :param send: sends (without blocking) a message to a designed
        recipient ``send(i, (tag, ...))``

    :return commitments and share
    """
    raise NotImplementedError

def avss_reconstruct(sid, pid, N, t, g, input, receive, send) -> ZR:
    """Asynchronous Verifiable Secret Sharing
    
    :param string sid: session id
    :param int pid: ``0 <= pid < N``
    :param int N:  at least 3
    :param int t: maximum number of malicious nodes , ``N >= 3t + 1``
    :param group g: a generator of the elliptic curve group
    :param input: func:`input()` is called to wait for the input value
    :param receive: :func:`receive()` blocks until a message is
        received; message is of the form::
            (i, (tag, ...)) = receive()
    :param send: sends (without blocking) a message to a designed
        recipient ``send(i, (tag, ...))``

    :return reconstructed secret 
    """
    raise NotImplementedError