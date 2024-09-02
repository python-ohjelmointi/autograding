"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def ruudukko():
    return [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55]
    ]


def test_tyhja_arvottujen_lista_ei_tuota_bingoa():
    from bingo import tarkista_bingo

    assert not tarkista_bingo(ruudukko(), [])


def test_kaikki_numerot_arvottu_tuottaa_varman_bingon():
    from bingo import tarkista_bingo

    assert tarkista_bingo(ruudukko(), list(range(1, 76)))


def test_bingo_yhdella_rivilla():
    from bingo import tarkista_bingo

    # tarkastetaan, ettei funktio palauta vääriä voittoja
    assert not tarkista_bingo(ruudukko(), [11, 12, 13, 14])
    assert not tarkista_bingo(ruudukko(), [21, 22, 24, 25])

    # tarkastetaan ylin rivi
    assert tarkista_bingo(ruudukko(), [11, 12, 13, 14, 15])

    # tarkastetaan alin rivi
    assert tarkista_bingo(ruudukko(), [1, 2, 55, 54, 53, 3, 4, 51, 52])


def test_bingo_yhdessa_sarakkeessa():
    from bingo import tarkista_bingo

    # tarkastetaan, ettei funktio palauta vääriä voittoja
    assert not tarkista_bingo(ruudukko(), [11, 21, 31, 51])
    assert not tarkista_bingo(ruudukko(), [14, 24, 44, 54])

    # toiseksi viimeinen pyrstyrivi
    assert tarkista_bingo(ruudukko(), [14, 24, 34, 44, 54])

    # ensimmäinen pyrstyrivi
    assert tarkista_bingo(ruudukko(), [1, 2, 3, 11, 21, 31, 41, 51, 7, 8, 9])


def test_bingo_vinosti():
    from bingo import tarkista_bingo

    # tarkastetaan, ettei funktio palauta vääriä voittoja
    assert not tarkista_bingo(ruudukko(), [11, 22, 33, 55])
    assert not tarkista_bingo(ruudukko(), [15, 24, 33, 51])

    # vinosti vasemmalta alhaalta oikealle ylös
    assert tarkista_bingo(ruudukko(), [51, 42, 33, 24, 15])

    # vinosti vasemmalta ylhäältä oikealle alas
    assert tarkista_bingo(ruudukko(), [1, 2, 3, 11, 22, 33, 44, 55, 7, 8, 9])
