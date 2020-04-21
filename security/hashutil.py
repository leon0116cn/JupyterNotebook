import hashlib
from base64 import b64encode, b64decode


class HashHelper:

    @classmethod
    def hash_with_sha256(cls, message, encoded=True):
        message_bytes = message.encode('utf-8')
        sha256 = hashlib.sha256(message_bytes)
        
        if encoded:
            return b64encode(sha256.digest())

        return sha256.hexdigest()

    @classmethod
    def hash_with_md5(cls, message, encoded=True):
        message_bytes = message.encode('utf-8')
        md5 = hashlib.md5(message_bytes)
        
        if encoded:
            return b64encode(md5.digest())

        return md5.hexdigest()

    @classmethod
    def verify_with_sha256(cls, message, tag, encoded=True):
        message_bytes = message.encode('utf-8')
        sha256 = hashlib.sha256(message_bytes)

        if encoded:
            sha256_msg = b64encode(sha256.digest())
        else:
            sha256_msg = sha256.hexdigest()

        if tag != sha256_msg:
            raise ValueError('verify sha256 hash error.')

        return True
        
    @classmethod
    def verify_with_md5(cls, message, tag, encoded):
        message_bytes = message.encode('utf-8')
        md5 = hashlib.md5(message_bytes)

        if encoded:
            md5_msg = b64encode(md5.digest())
        else:
            md5_msg = md5.hexdigest()

        if tag != md5_msg:
            raise ValueError('verify md5 hash error.')

        return True
        

if __name__ == "__main__":
    message = 'hello world.'
    # print(HashHelper.hash_with_sha256(message))
    # print(HashHelper.hash_with_sha256(message, b64_encoded=False))

    # print(HashHelper.hash_with_md5(message))
    # print(HashHelper.hash_with_md5(message, encoded=False))