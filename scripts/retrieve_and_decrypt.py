from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import ipfshttpclient

def load_private_key(filepath):
    with open(filepath, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

def decrypt_message(encrypted_message, private_key):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def retrieve_from_ipfs(ipfs_hash):
    client = ipfshttpclient.connect('/dns/localhost/tcp/5001/http')
    return client.cat(ipfs_hash)

def main():
    private_key = load_private_key("keys/bob_private_key.pem")
    ipfs_hash = "YOUR_IPFS_HASH_HERE"
    encrypted_message = retrieve_from_ipfs(ipfs_hash)
    message = decrypt_message(encrypted_message, private_key)
    print(f"Decrypted message: {message}")

if __name__ == "__main__":
    main()
