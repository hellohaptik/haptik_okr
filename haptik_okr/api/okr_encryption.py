import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

ENCRYPTION_KEY = 'HAPTIKOKR1411'


class AESCipher:
    def __init__(self, key):
        self.bs = 16
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        message = self._pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message)).decode('utf-8').replace('+', '_').replace('/', '-')

    def decrypt(self, enc):
        enc = enc.replace('_', '+').replace('-', '/')
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


def encrypt_user_id(decrypted_id):
    encrypted_id = AESCipher(ENCRYPTION_KEY).encrypt(decrypted_id)
    return encrypted_id


def decrypt_user_id(encrypted_id):
    encrypted_id = encrypted_id.replace('/', '-')
    if len(encrypted_id) == 43:
        encrypted_id = "-" + encrypted_id
    decrypted_id = AESCipher(ENCRYPTION_KEY).decrypt(encrypted_id)
    return decrypted_id