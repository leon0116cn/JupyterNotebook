import sys
import unittest
from security.hashutil import HashHelper


class HashTest(unittest.TestCase):
    def setUp(self):
        self.message = 'hello world.'
        self.message_md5_encoded = b'PEKSrpW+WODFjk5VEfCWRw=='
        self.message_md5 = '3c4292ae95be58e0c58e4e5511f09647'
        self.message_sha256_encoded = b'fdsicxX0IyUPxn875pxURijf/kF1KvkcUK4KnEn664c='
        self.message_sha256 = '7ddb227315f423250fc67f3be69c544628dffe41752af91c50ae0a9c49faeb87'

    def tearDown(self):
        pass
    
    def test_hash_with_sha256(self):
        encoded_tag = HashHelper.hash_with_sha256(self.message)
        self.assertEqual(encoded_tag, self.message_sha256_encoded)

        tag = HashHelper.hash_with_sha256(self.message, encoded=False)
        self.assertEqual(tag, self.message_sha256)

    def test_hash_with_md5(self):
        encoded_tag = HashHelper.hash_with_md5(self.message)
        self.assertEqual(encoded_tag, self.message_md5_encoded)

        tag = HashHelper.hash_with_md5(self.message, encoded=False)
        self.assertEqual(tag, self.message_md5)

    def test_verify_with_sha256(self):
        self.assertTrue(HashHelper.verify_with_sha256(self.message, self.message_sha256_encoded))
        with self.assertRaises(ValueError):
            HashHelper.verify_with_sha256(self.message, '123456')
        
        self.assertTrue(HashHelper.verify_with_sha256(self.message, self.message_sha256, encoded=False))
        with self.assertRaises(ValueError):
            HashHelper.verify_with_sha256(self.message, '123456', encoded=False)


if __name__ == "__main__":
    unittest.main()
