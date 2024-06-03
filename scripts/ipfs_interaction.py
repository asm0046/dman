import ipfshttpclient

def connect_to_ipfs():
    return ipfshttpclient.connect('/dns/localhost/tcp/5001/http')

def add_to_ipfs(data):
    client = connect_to_ipfs()
    result = client.add_bytes(data)
    return result['Hash']

def retrieve_from_ipfs(ipfs_hash):
    client = connect_to_ipfs()
    return client.cat(ipfs_hash)
