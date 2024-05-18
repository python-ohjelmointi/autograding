"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_voittava_rivi():
    from ristinolla import tarkista_voittaja

    assert tarkista_voittaja(".o.", "xxx", ".o.") == 'x'
    assert tarkista_voittaja(".x.", ".x.", "ooo") == 'o'

def test_voittava_sarake():
    from ristinolla import tarkista_voittaja

    assert tarkista_voittaja("xox", ".o.", ".o.") == 'o'
    assert tarkista_voittaja("xoo", "xo.", "x..") == 'x'
    assert tarkista_voittaja("..x", "..x", "..x") == 'x'
    assert tarkista_voittaja("o..", "o..", "o..") == 'o'

def test_voitto_vinosti():
    from ristinolla import tarkista_voittaja

    assert tarkista_voittaja("oox", ".x.", "x.o") == 'x'
    assert tarkista_voittaja("oox", ".o.", "x.o") == 'o'

def test_tasapeli():
    from ristinolla import tarkista_voittaja

    assert tarkista_voittaja("o..", "x..", "...") is None
    assert tarkista_voittaja("oox", "xxo", "oxo") is None

def test_tyhja_peli():
    from ristinolla import tarkista_voittaja

    assert tarkista_voittaja("...", "...", "...") is None

