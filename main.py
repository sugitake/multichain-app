import mcrpc
from mcrpc import client
import json
# https://github.com/coblo/mcrpc


# addresse=17vCUo38rLsCwhSJt5i3EtfbRYSVxvDZPYFJ2c
client = mcrpc.RpcClient("127.0.0.1", "7748", "multichainrpc",
                         "7FRhAxf9iGNqVXwDJNWuVmwzEGgd1Bd1LFwcpnXcMeJw")
# print(client.getinfo())
# client.issue("17vCUo38rLsCwhSJt5i3EtfbRYSVxvDZPYFJ2c","asset1",100)
# print(client.listassets())


def vote(vaddress, caddress):
    client = mcrpc.RpcClient("127.0.0.1", "7748", "multichainrpc", vaddress)
    result=client.sendassetfrom(vaddress, caddress, "vote_point", 1)
    print(result)

def viewVote(vaddress):
    client = mcrpc.RpcClient("127.0.0.1", "7748", "multichainrpc", vaddress)
    result=client.getaddressbalances(vaddress)
    print(result)
    return result

voter_address="7FRhAxf9iGNqVXwDJNWuVmwzEGgd1Bd1LFwcpnXcMeJw"
candidate_address=""
vote(voter_address, candidate_address)
viewVote(voter_address)
