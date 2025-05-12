"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

ruudukko = """
abc
def
ghi
""".strip()


def test_vaakarivi_eteenpain():
    from sanahaku import sanahaku

    assert not sanahaku("dhi", ruudukko)

    assert sanahaku("abc", ruudukko)
    assert sanahaku("def", ruudukko)
    assert sanahaku("ghi", ruudukko)


def test_vaakarivi_taaksepain():
    from sanahaku import sanahaku

    assert not sanahaku("dhi", ruudukko)

    assert sanahaku("cba", ruudukko)
    assert sanahaku("fed", ruudukko)
    assert sanahaku("ihg", ruudukko)


def test_pystyrivi_alaspain():
    from sanahaku import sanahaku

    assert not sanahaku("dhi", ruudukko)

    assert sanahaku("adg", ruudukko)
    assert sanahaku("beh", ruudukko)
    assert sanahaku("cfi", ruudukko)


def test_pystyrivi_ylospain():
    from sanahaku import sanahaku

    assert not sanahaku("dhi", ruudukko)

    assert sanahaku("gda", ruudukko)
    assert sanahaku("heb", ruudukko)
    assert sanahaku("ifc", ruudukko)


def test_osittaiset_rivit():
    from sanahaku import sanahaku

    assert not sanahaku("dhi", ruudukko)

    assert sanahaku("ab", ruudukko)
    assert sanahaku("fe", ruudukko)
    assert sanahaku("eh", ruudukko)
    assert sanahaku("eb", ruudukko)
