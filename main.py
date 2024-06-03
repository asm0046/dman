import scripts.encrypt_and_store as encrypt_and_store
import scripts.retrieve_and_decrypt as retrieve_and_decrypt
import scripts.blockchain_interaction as blockchain_interaction

def main():
    # Encrypt and store message
    encrypt_and_store.main()

    # Send IPFS hash to blockchain
    blockchain_interaction.main()

    # Retrieve and decrypt message
    retrieve_and_decrypt.main()

if __name__ == "__main__":
    main()
