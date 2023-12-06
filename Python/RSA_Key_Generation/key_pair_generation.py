from Crypto.PublicKey import RSA
key = RSA.generate(2048)
with open("private_key.pem", "wb") as f:
    f.write(key.exportKey('PEM'))
public_key = key.publickey()
with open("public_key.pem", "wb") as f:
    f.write(public_key.exportKey('OpenSSH'))
