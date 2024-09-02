"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_palauttaa_arvon_eika_tulosta(capsys):
    from alkukirjaimet import rivien_alkukirjaimet_isoksi

    result = rivien_alkukirjaimet_isoksi('testi')

    # funktion pitää palauttaa, se ei saa tulostaa
    assert type(result) == str
    assert '?' not in result
    assert '' == capsys.readouterr().out


def test_vain_yksi_merkki():
    from alkukirjaimet import rivien_alkukirjaimet_isoksi

    tulos = rivien_alkukirjaimet_isoksi("a")
    assert typista(tulos) == "A"

    tulos = rivien_alkukirjaimet_isoksi("b")
    assert typista(tulos) == "B"

    # valmiiksi iso kirjain
    tulos = rivien_alkukirjaimet_isoksi("X")
    assert typista(tulos) == "X"


def test_kaksi_rivia():
    from alkukirjaimet import rivien_alkukirjaimet_isoksi

    tulos = rivien_alkukirjaimet_isoksi(
        "ohjelmointi on matka\njokainen rivi vie lähemmäs")
    assert typista(
        tulos) == 'Ohjelmointi on matka\nJokainen rivi vie lähemmäs'


def test_monta_rivia():
    from alkukirjaimet import rivien_alkukirjaimet_isoksi

    tulos = rivien_alkukirjaimet_isoksi("Eat\nSleep\ncode")
    assert typista(tulos) == 'Eat\nSleep\nCode'


def test_tyhjat_rivit_valissa():
    from alkukirjaimet import rivien_alkukirjaimet_isoksi

    tulos = rivien_alkukirjaimet_isoksi(
        "plan thoroughly\n\ncode carefully\n\ntest")
    assert typista(
        tulos) == 'Plan thoroughly\n\nCode carefully\n\nTest'


def typista(teksti: str):
    """
    Poistaa annetusta merkkijonosta mahdollisen lopussa olevan rivinvaihdon
    ja palauttaa uuden merkkijonon.
    """
    return teksti.rstrip()
