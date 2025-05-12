"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_lukusarja_kakkosesta():
    from lukusarja import lukusarja

    assert lukusarja(2) == [2, 1]


def test_lukusarja_kasista():
    from lukusarja import lukusarja

    assert lukusarja(8) == [8, 4, 2, 1]


def test_lukusarja_seiskasta():
    from lukusarja import lukusarja

    assert lukusarja(7) == [7, 22, 11, 34, 17, 52, 26,
                            13, 40, 20, 10, 5, 16, 8, 4, 2, 1]


def test_lukusarja_kympista():
    from lukusarja import lukusarja

    assert lukusarja(10) == [10, 5, 16, 8, 4, 2, 1]


def test_lukusarja_sadasta():
    from lukusarja import lukusarja

    assert lukusarja(100) == [100, 50, 25, 76, 38, 19, 58, 29, 88,
                              44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
