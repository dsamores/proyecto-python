from primos import generar_primos


def test_primos_vacio():
    assert generar_primos(0) == []


def test_primos_uno():
    assert generar_primos(1) == [2]


def test_primos_dos():
    assert generar_primos(2) == [2, 3]


def test_primos_diez():
    assert generar_primos(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
