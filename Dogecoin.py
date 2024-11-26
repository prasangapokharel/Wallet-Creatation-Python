!pip install pycryptodome

import os
import ecdsa
import hashlib
import base58
from Crypto.Hash import RIPEMD160  # Import from pycryptodome

def generate_dogecoin_address():
    # Generate private key
    private_key = os.urandom(32)
    private_key_hex = private_key.hex()

    # Generate public key
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b"\x04" + vk.to_string()

    # Generate address (simplified for Dogecoin)
    sha256_1 = hashlib.sha256(public_key).digest()
    ripemd160 = RIPEMD160.new()
    ripemd160.update(sha256_1)
    hashed_public_key = ripemd160.digest()

    network_byte = b"\x1E"  # Prefix for Dogecoin mainnet
    network_key = network_byte + hashed_public_key

    checksum = hashlib.sha256(hashlib.sha256(network_key).digest()).digest()[:4]
    address = base58.b58encode(network_key + checksum).decode()

    print("Private Key (hex):", private_key_hex)
    print("Dogecoin Address:", address)

# Generate Dogecoin private key and address
generate_dogecoin_address()
