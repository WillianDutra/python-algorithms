from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "2")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(999, 4)

    assert encrypt_message("encrypt", 10) == "tpyrcne"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("trybe", 2) == "eby_rt"
