import gnupg

def encrypt_flag(key_data):
    gpg = gnupg.GPG(gnupghome='.gnupg')
    flag = "PermCTF{everybody_needs_encryption}"

    # read a private key from filesystem
    priv_key = open("bot.priv", "r").read()

    # import key to the keychaing
    gpg.import_keys(priv_key)
    signer_fp = '318AABA28B09D9C5C98CD40EEA9A63DFD1432F34'
    
    # import recieved keys into keychain
    gpg.import_keys(key_data)
    key_obj = gpg.list_keys()[-1]

    recipient = key_obj['fingerprint']

    # encrypt flag and sign it
    encrypted_data = gpg.encrypt(flag, recipient, always_trust=True, sign=signer_fp)
    gpg.delete_keys(recipient)

    return encrypted_data


if __name__ == '__main__':
    encrypt_flag(input("insert key in armored format:\n"))
