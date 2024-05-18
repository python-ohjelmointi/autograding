"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_yksi_rivi():
    from rivinumerot import lisaa_rivinumerointi

    numeroitu = lisaa_rivinumerointi("hello")
    assert typista(numeroitu) == "1. hello"

def test_kaksi_rivia():
    from rivinumerot import lisaa_rivinumerointi

    numeroitu = lisaa_rivinumerointi("Hello\nWorld")
    assert typista(numeroitu) == "1. Hello\n2. World"


def test_kolme_rivia():
    from rivinumerot import lisaa_rivinumerointi

    numeroitu = lisaa_rivinumerointi("Hello\nWorld\nTest")
    assert typista(numeroitu) == "1. Hello\n2. World\n3. Test"

def test_monta_rivia():
    from rivinumerot import lisaa_rivinumerointi

    numeroitu = lisaa_rivinumerointi("Eat\nSleep\nCode\nRepeat")
    assert typista(numeroitu) == "1. Eat\n2. Sleep\n3. Code\n4. Repeat"

def test_tyhja_rivi_valissa():
    from rivinumerot import lisaa_rivinumerointi

    numeroitu = lisaa_rivinumerointi("Hello\n\nWorld")
    assert typista(numeroitu) == "1. Hello\n2. \n3. World"

def typista(teksti: str):
    """
    Poistaa annetusta merkkijonosta mahdollisen lopussa olevan rivinvaihdon
    ja palauttaa uuden merkkijonon.
    """
    if teksti.endswith("\n"):
        return teksti[:-1]
    return teksti
