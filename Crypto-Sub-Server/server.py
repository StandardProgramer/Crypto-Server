from socket import *
from threading import Thread
import random
import Crypto
from Crypto.Cipher import AES

def clientHandler():
    conn, addr = s.accept()
    print addr, "is connected"
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print "Received Message", repr(data)

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

HOST = "" #localhost
PORT = 15000


s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    flipped = {v: k for k, v in key.items()}
    return ''.join(flipped[l] for l in ciphertext)

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def show_result(plaintext):
    """Generate a resulting cipher with elements shown"""
    key = generate_key()
    encrypted = encrypt(key, plaintext)

    print 'Key: %s' % key
    print 'Encrytped: %s' % encrypted
    print 'Decrypt: %s' % decrypt

"""START HERE"""
def do_decrypt(ciphertext):
    obj2 = AES.new('test_key', AES.MODE_CBC, 'test_IV')
    message = obj2.decrypt(ciphertext)
    return message

    print 'Text: %s' % message

"""END HERE"""

print "Server is running"
#Thread(target=clientHandler).start()
#Thread(target=clientHandler).start()
#Thread(target=clientHandler).start()

for i in range(10):
    Thread(target=clientHandler).start()

s.close()
