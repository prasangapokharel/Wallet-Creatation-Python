!pip install ecdsa base58 pycryptodome


import os
import ecdsa
import hashlib
import base58
from Crypto.Hash import RIPEMD160  # pycryptodome library

def generate_bitcoin_address():
    # Step 1: Generate a private key
    private_key = os.urandom(32)  # 32 bytes = 256 bits
    private_key_hex = private_key.hex()
    
    # Step 2: Generate the public key from the private key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b"\x04" + vk.to_string()  # Uncompressed public key format
    
    # Step 3: Perform SHA-256 and RIPEMD-160 hashing on the public key
    sha256_hash = hashlib.sha256(public_key).digest()
    ripemd160 = RIPEMD160.new()
    ripemd160.update(sha256_hash)
    hashed_public_key = ripemd160.digest()

    # Step 4: Add network byte (0x00 for Bitcoin Mainnet)
    network_byte = b"\x00"  # Mainnet prefix for Bitcoin
    network_key = network_byte + hashed_public_key

    # Step 5: Calculate checksum (double SHA-256)
    checksum = hashlib.sha256(hashlib.sha256(network_key).digest()).digest()[:4]

    # Step 6: Generate the Bitcoin address (Base58Check encoding)
    address = base58.b58encode(network_key + checksum).decode()

    print("Bitcoin Private Key (hex):", private_key_hex)
    print("Bitcoin Address:", address)

# Generate Bitcoin private key and address
generate_bitcoin_address()
