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
    'Para um valor de "key" incorreto, retorna um erro'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "2")

    'Para um valor de "message" incorreto, retorna um erro'
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123123, 2)

    'Para um valor de "key" negativo, retorna a string invertina'
    assert encrypt_message("message", -1) == "egassem"

    'Para um valor impar de "key", retorna a string dividida'
    assert encrypt_message("message", 3) == "sem_egas"

    'Para um valor par de "key", retorna a string dividida'
    assert encrypt_message("message", 2) == "egass_em"
