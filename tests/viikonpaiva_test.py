"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_funktio_on_olemassa():
    from viikonpaiva import viikonpaiva

    assert callable(viikonpaiva)


def test_funktion_parametri_oikein():
    from viikonpaiva import viikonpaiva

    # tämä testi menee läpi, kunhan import ei heitä poikkeusta:
    viikonpaiva(1)


def test_funktio_palauttaa_arvon_eika_tulosta(capsys):
    from viikonpaiva import viikonpaiva

    result = viikonpaiva(1)

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str
    assert '' == capsys.readouterr().out


def test_oikeat_viikonpaivat():
    from viikonpaiva import viikonpaiva

    assert viikonpaiva(1) == 'Maanantai'
    assert viikonpaiva(2) == 'Tiistai'
    assert viikonpaiva(3) == 'Keskiviikko'
    assert viikonpaiva(4) == 'Torstai'
    assert viikonpaiva(5) == 'Perjantai'
    assert viikonpaiva(6) == 'Lauantai'
    assert viikonpaiva(7) == 'Sunnuntai'


def test_tuntematon_numero():
    from viikonpaiva import viikonpaiva

    assert viikonpaiva(-1) == ''
    assert viikonpaiva(-2) == ''
    assert viikonpaiva(-3) == ''
    assert viikonpaiva(-4) == ''
    assert viikonpaiva(-5) == ''
    assert viikonpaiva(-6) == ''
    assert viikonpaiva(-7) == ''
