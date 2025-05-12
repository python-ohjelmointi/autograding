"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_on_olemassa():
    from tahtiarvostelu import tahtiarvostelu

    # tämä testi menee läpi, kunhan kutsu ei heitä poikkeusta:
    tahtiarvostelu(5)


def test_tahdet_palautetaan_tai_tulostetaan(capsys):
    from tahtiarvostelu import tahtiarvostelu

    tahdet = tahtiarvostelu(2)

    captured = capsys.readouterr()
    assert '⭐⭐' in [captured.out, tahdet]


def test_eri_pituiset_tahtijonot(capsys):
    from tahtiarvostelu import tahtiarvostelu

    assert '⭐' == tahtiarvostelu(1)
    assert '⭐⭐' == tahtiarvostelu(2)
    assert '⭐⭐⭐' == tahtiarvostelu(3)
    assert '⭐⭐⭐⭐' == tahtiarvostelu(4)
    assert '⭐⭐⭐⭐⭐' == tahtiarvostelu(5)


def test_nolla_tahtea():
    from tahtiarvostelu import tahtiarvostelu

    assert '' == tahtiarvostelu(0)


def test_suuri_maara_tahtia():
    from tahtiarvostelu import tahtiarvostelu

    tahdet = tahtiarvostelu(1_000)  # ei heitä poikkeusta
    assert tahdet.count('⭐') == 1_000


