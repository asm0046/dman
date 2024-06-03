from web3 import Web3

def connect_to_blockchain(url):
    return Web3(Web3.HTTPProvider(url))

def send_transaction(w3, from_address, to_address, data):
    tx_hash = w3.eth.sendTransaction({
        'from': from_address,
        'to': to_address,
        'data': w3.toHex(text=data)
    })
    return tx_hash

def main():
    w3 = connect_to_blockchain('http://localhost:8545')
    from_address = "YOUR_FROM_ADDRESS"
    to_address = "YOUR_TO_ADDRESS"
    ipfs_hash = "YOUR_IPFS_HASH_HERE"
    tx_hash = send_transaction(w3, from_address, to_address, ipfs_hash)
    print(f"Transaction hash: {tx_hash}")

if __name__ == "__main__":
    main()
