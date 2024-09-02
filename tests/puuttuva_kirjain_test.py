"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_palauttaa_arvon_eika_tulosta(capsys):
    from puuttuva_kirjain import etsi_puuttuva_kirjain

    result = etsi_puuttuva_kirjain("ac")

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str and '?' not in result
    assert '' == capsys.readouterr().out


def test_kirjaimet_aakkosten_alusta():
    from puuttuva_kirjain import etsi_puuttuva_kirjain

    assert etsi_puuttuva_kirjain("acde") == 'b'


def test_kirjaimet_aakkosten_valista():
    from puuttuva_kirjain import etsi_puuttuva_kirjain

    assert etsi_puuttuva_kirjain("eghijklmn") == 'f'
    assert etsi_puuttuva_kirjain("efgijk") == 'h'


def test_kirjaimet_aakkosten_lopusta():
    from puuttuva_kirjain import etsi_puuttuva_kirjain

    assert etsi_puuttuva_kirjain("stuvwyz") == 'x'
    assert etsi_puuttuva_kirjain("stvw") == 'u'


def test_aakkoset_alusta_loppuun():
    from puuttuva_kirjain import etsi_puuttuva_kirjain

    assert etsi_puuttuva_kirjain("abcdefghijkmnopqrstuvwxyz") == 'l'
    assert etsi_puuttuva_kirjain("abcdefghijklmnpqrstuvwxyz") == 'o'
