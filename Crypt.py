from cryptography.fernet import Fernet


def generate_key():
    msg_key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(msg_key)


def load_key():
    return open("secret-key", "rb").read()


def encrypt_message(message):
    msg_key = load_key()
    encoded_message = message.encode()
    f = Fernet(msg_key)
    encrypted_msg = f.encrypt(encoded_message)
    return encrypted_msg


def decrypt_message(enc_msg):
    msg_key = load_key()
    f = Fernet(msg_key)
    dec_msg = f.decrypt(enc_msg)
    return dec_msg.decode()


generate_key()
key = load_key()

user_message = input("ENTER A TEXT TO ENCRYPT :\n")
enc = encrypt_message(user_message)
dec = decrypt_message(enc)
