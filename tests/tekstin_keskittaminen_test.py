"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_keskita_yksi_merkki():
    from tekstin_keskittaminen import keskita_teksti

    keskitetty = keskita_teksti("a", 5)
    assert typista(keskitetty) == "  a  "

def test_keskita_yksi_rivi():
    from tekstin_keskittaminen import keskita_teksti

    keskitetty = keskita_teksti("keskitetty", 12)
    assert typista(keskitetty) == " keskitetty "

def test_keskita_monta_rivia():
    from tekstin_keskittaminen import keskita_teksti

    keskitetty = keskita_teksti("keskitetty\nteksti\nkeskitetty\nteksti", 12)
    assert typista(keskitetty) == " keskitetty \n   teksti   \n keskitetty \n   teksti   "

def test_keskita_liian_pitka_rivi():
    from tekstin_keskittaminen import keskita_teksti

    keskitetty = keskita_teksti("Hello!\nTerve maailma!", 10)
    assert typista(keskitetty) == "  Hello!  \nTerve maailma!"

def test_keskita_pariton_keskitys():
    from tekstin_keskittaminen import keskita_teksti

    keskitetty = keskita_teksti("Hello\nworld", 8)
    assert typista(keskitetty) in [" Hello  \n world  ", "  Hello \n  world "]


def typista(teksti: str):
    """
    Poistaa annetusta merkkijonosta mahdollisen lopussa olevan rivinvaihdon
    ja palauttaa uuden merkkijonon.
    """
    if teksti.endswith("\n"):
        return teksti[:-1]
    return teksti
