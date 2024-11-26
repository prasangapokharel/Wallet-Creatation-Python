from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def generate_tron_wallet_with_mnemonic():
    # Step 1: Generate a mnemonic (seed phrase)
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)  # 12-word mnemonic
    print("Mnemonic (Seed Phrase):", mnemonic)

    # Step 2: Generate a seed from the mnemonic
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

    # Step 3: Derive a Tron wallet using BIP-44 standard
    bip44_wallet = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)
    account = bip44_wallet.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    # Step 4: Retrieve the private key and address
    private_key = account.PrivateKey().Raw().ToHex()
    address = account.PublicKey().ToAddress()

    print("Tron Address:", address)
    print("Tron Private Key:", private_key)

# Generate a Tron wallet with mnemonic
generate_tron_wallet_with_mnemonic()
