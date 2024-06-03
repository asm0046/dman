from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import ipfshttpclient

def load_public_key(filepath):
    with open(filepath, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

def encrypt_message(message, public_key):
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def store_to_ipfs(encrypted_message):
    client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
    result = client.add_bytes(encrypted_message)
    return result['Hash']

def main():
    public_key = load_public_key("keys/bob_public_key.pem")
    message = b"Hello Bob!"
    encrypted_message = encrypt_message(message, public_key)
    ipfs_hash = store_to_ipfs(encrypted_message)
    print(f"Stored message with IPFS hash: {ipfs_hash}")

if __name__ == "__main__":
    main()
