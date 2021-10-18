import mcrpc
from mcrpc import client
import json
# https://github.com/coblo/mcrpc


# addresse=17vCUo38rLsCwhSJt5i3EtfbRYSVxvDZPYFJ2c
# client = mcrpc.RpcClient("127.0.0.1", "7748", "multichainrpc","F4rnMKe6rnpYEJuqgt7bjEyo8tcsipPe6tb2pXjRmfmq")
# print(client.getinfo())
# client.issue("17vCUo38rLsCwhSJt5i3EtfbRYSVxvDZPYFJ2c","asset1",100)
# print(client.listassets())


def vote(vaddress, caddress, ruser, rpass):
    client = mcrpc.RpcClient("127.0.0.1", "7748", ruser, rpc_pass)
    result=client.sendassetfrom(vaddress, caddress, "vote_point", 1)
    print(result)

def viewVote(vaddress, ruser, rpass):
    client = mcrpc.RpcClient("127.0.0.1", "7748",  ruser, rpc_pass)
    result=client.getaddressbalances(vaddress)
    print(result)
    return result


rpc_user="multichainrpc"
rpc_pass="F4rnMKe6rnpYEJuqgt7bjEyo8tcsipPe6tb2pXjRmfmq"

# server04
voter_address="1MgT29yYwNvMCxoLNjeC7adDrc2G16qfqjYg7q"

# server01
candidate_address="1KskJXTqNtsE4sLP5maQ6DJvTFYHqLn9fkPZY8"

vote(voter_address, candidate_address, rpc_user, rpc_pass)
viewVote(voter_address)

