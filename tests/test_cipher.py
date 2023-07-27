import cipher.assignment_cipher


def test_encryption():
    assert cipher.assignment_cipher.encryption("abc", 3) == "def"


def test_decryption():
    assert cipher.assignment_cipher.decryption("def", 3) == "abc"

