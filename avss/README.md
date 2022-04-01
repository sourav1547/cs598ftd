# Asynchronous Reliable Broadcast and Asynchronous Verifiable Secret Sharing

## Introduction
In this assignment, we will first implement the Asynchronous Reliable Broadcast (RBC) protocol due to Bracha [1, 2]. In particular, we will implement the verifiable variant of Bracha's RBC. We will then use the verifiable RBC to implement an Asynchronous Verifiable Secret Sharing (AVSS) protocol. 

Throughout the assignment, we will use `n`, the total number of nodes (including the dealer), as `3t+1`. Here `t` is the maximum number of nodes an adversary can corrupt.

## Reliable Broadcast
A protocol for a set of nodes `{1,....,n}`, where a distinguished node called the broadcaster holds an initial input `M`, is a reliable broadcast (RBC) protocol if the following properties hold:

- **Agreement**: If an honest node outputs a message `M'` and another honest node outputs `M"`, then `M'=M"`. 

- **Validity**: If the broadcaster is honest, all honest nodes eventually output the message `M`.

- **Totality**: If an honest node outputs a message, then every honest node eventually outputs a message. 


### Pseudocode of Bracha's RBC protocol
```
# Only leader node
send <PROPOSE, M> to all

# All node i
Upon receiving <PROPOSE, M> from leader:
    # unless otherwise specified, P(M) always returns true
    if P(M) is true:
        send <ECHO, M> to all

Upon receiving 2t+1 <ECHO, M> for matching M:
    if have not sent <READY, M> yet:
        send <READY, M> to all

Upon receiving t+1 <READY, M> for matching M:
    if have not sent <READY, M> yet:
        send <READY, M> to all

Upon receiving 2t+1 <READY, M> for matching M:
    Output M and return
```

## Asynchronous Verifiable Secret Sharing (AVSS)
An AVSS protocol consists of two phases: Sharing and Reconstruction. A dealer `D` shares a secret `s` during the sharing phase using the `Share()` protocol. During the reconstruction phase, nodes use `Rec(.)` to recover the secret. We say that `(Share(), Rec())` is a `t`-resilient AVSS protocol if the following properties hold with high probability against an adversary controlling up to `t` nodes: 
%

- **Termination**: 
    - If the dealer `D` is honest, then each honest node will eventually terminate the `Share()` protocol.
    - If an honest node terminates the `Share()` protocol, then every honest node will eventually terminate `Share()`. 
    - If all honest nodes start `Rec()`, then each honest node will eventually terminate `Rec()`. 

- **Correctness**:
    - If `D` is honest, then each honest node, upon terminating `Rec()`, outputs the shared secret `s`. 
    - If some honest node terminates `Share()`, then there exists a fixed secret `s`, such that each honest node, upon completing `Rec()`, will output `s`.

- **Secrecy**: If `D` is honest and no honest node has begun executing `Rec()`, then an adversary that corrupts up to `t` nodes has no information about `s` other than whatever is revealed from `g^s`.

### Pseudocode of the Sharing phase i.e., `Share()`
```
# Only leader node
- Let s be the secret
- Let p(x) = s + a1x + a2*x^2 + ...  + at*x^t be a degree t 
   polynomial where ai's are random for i=1,2,...,t. 
- Let v = [g^s, g^{a1}, g^{a2},..., g^{at}]
- RBC(v)
- Send <SHARE, p(i)> to node i for i=1,2,...,n

# During RBC(v), i-th node use the following predicate
P(v):
    - Wait for <SHARE, p'(i)>
    - Compute g^{p(i)} using v
    - Return true g^{p(i)} matches g^{p'(i)}

# All node i
Upon RBC(v) termination, Output v and p'(i) (if any)
```

### Pseudocode of the Reconstruction phase i.e., `Rec()`
```
# each node i
send <RECONSTRUCT, p'(i)> to all

upon receiving t+1 valid RECONSTRUCT message: 
    reconstruct and return p(0)
``` 

## Code Structure
The code skeleton has the following code structure.

```bash
.
├── Dockerfile
├── docker-compose.yml
├── README.md
├── core
│   ├── avss.py
│   ├── rbc.py
│   └── utils.py
├── main.py
├── network
│   └── router.py
└── tests
    ├── test_avss.py
    └── test_rbc.py
```

As the name suggests, the files `Dockerfile` and `docker-compose.yml` are docker related. Very briefly, the `Dockerfile` contains the environment specifications of the docker image and instructions to download and install them. You can think of  `docker-compose.yml` as the configuration file.


The `main.py` is the entry point of the code. The `network/` library implements `router.py` which provides the basic communication interface between nodes. See `tests/test_rbc.py` for an example on how to use the communication interface. 

The `core/` directory consists of three files: `rbc.py`, `avss.py` and `utils.py` is what you will be making changes to. Currently, the `rbc.py` implements a non fault tolerant broadcast protocol where the leader simply sends its proposal to all the nodes. You can use this as a starting point to implement the fault tolerant `rbc.py` and `avss.py`. You can implement any helper functions in `utils.py`.

The `tests/` directory consists of files to test the reliable broadcast (`test_rbc.py`) and AVSS scheme (`test_avss.py`).


## Assignment Requirements
You will implement the validated Reliable Broadcast in `core/rbc.py` and AVSS protocol described above in `core/avss.py`. 

Throughout this assignment, we will use the `prime192v1` elliptic curve for cryptographic operations. See `tests/test_avss.py` for a brief example. You can assume that the channels between any pair of nodes are authenticated and private.

NOTE: Your code must handle malicious behavior such as equivocation, message omission, etc., by a subset of nodes (including the leader).

## Setup and Installation
This skeleton uses `docker`. Thus you have to first install `docker` in your machine. You can get `docker` from https://docs.docker.com/get-docker/

Once the docker is installed and running, you can build the docker image of this homework by running.
```
docker-compose build avss 
```

NOTE: Make sure to run the docker application before executing the previous command. If your docker application is not running, you will get the following error.
```
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', ConnectionRefusedError(61, 'Connection refused'))
[32537] Failed to execute script docker-compose
``` 

After building the `avss` docker image, run the docker image and attach a bash to it using
```
docker-compose run --rm avss bash 
```

Upon successful execution of the above command, you will be inside the docker image. Also, your terminal should appear something like below. 

```bash 
root@18016f043b9d:/usr/src/avss#
root@18016f043b9d:/usr/src/avss#
``` 

Once you are inside the docker image, you can test the installation by running
``` 
python main.py
```

## Submission Instructions
This is an individual assignment. Please submit a `zip` file named as `[your uiuc net id]_hw3.zip` that unzips to the `cs598ftd` directory. 

For example, I will submit a zip file named `souravd2_hw3.zip` so that the following holds:
```
$ ls
souravd2_hw3.zip
$ unzip souravd2_hw3.zip
$ ls
souravd2_hw3.zip        cs598ftd
$ cd cs598ftd
$ ls
README.md       avss            bls
$ cd avss
$ ls
Dockerfile              __init__.py             docker-compose.yml      network                 tests                   README.md               core                    main.py                 
```

## Additional Resources
### `charm` resources
- How to use charm  https://jhuisi.github.io/charm/cryptographers.html
- Implemented schemes https://jhuisi.github.io/charm/schemes.html

### `docker` resources
 - Basics: https://docker-curriculum.com/
 - Debug inside a docker in `vscode` https://www.youtube.com/watch?v=qCCj7qy72Bg


 ## References
[1] Bracha, Gabriel. "An asynchronous [(n-1)/3]-resilient consensus protocol." Proceedings of the third annual ACM symposium on Principles of distributed computing. 1984.

[2] Living with Asynchrony: Bracha's Reliable Broadcast, https://decentralizedthoughts.github.io/2020-09-19-living-with-asynchrony-brachas-reliable-broadcast/