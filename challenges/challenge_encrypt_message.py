import pytest


def encrypt_message(message: str, key: int):
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "2")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123123, 2)

    assert encrypt_message("encrypt", -1) == "tpyrcne"
    assert encrypt_message("message", 3) == "sem_egas"
    assert encrypt_message("trybe", 2) == "eby_rt"
