from socket import *
import random
from Crypto.Cipher import AES

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

"""AES ENCRYPT"""

def do_encrypt(message):
    obj = AES.new('test_key', AES.MODE_CBC, 'test_IV')
    ciphertext = obj.encrypt(message)
    return ciphertext

"""END HERE"""

def generate_key():
    """Generate an key for our cipher"""
    shuffled = sorted(chars, key=lambda k: random.random())
    return dict(zip(chars, shuffled))

def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    return ''.join(key[l] for l in plaintext)

def show_result(plaintext):
    """Generate a resulting cipher with elements shown"""
    key = generate_key()
    encrypted = encrypt(key, plaintext)
    print 'Key: %s' % key
    print 'Encrytped: %s' % encrypted
s = socket()
s.connect(("localhost",15000))
show_result('test')
