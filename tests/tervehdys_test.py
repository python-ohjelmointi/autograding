"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_funktio_on_olemassa():
    from tervehdys import tervehdys

    # tämä testi menee läpi, kunhan kutsu ei heitä poikkeusta:
    tervehdys('Matti')

def test_nimi_loytyy_tulosteesta(capsys):
    from tervehdys import tervehdys

    tervehdys('Anna Maria')
    captured = capsys.readouterr()
    assert 'Anna Maria' in captured.out

def test_tervehdys_oikein_muotoiltu(capsys):
    from tervehdys import tervehdys

    tervehdys('Maija')
    captured = capsys.readouterr()
    assert 'Hei Maija!' in captured.out

def test_tyhja_merkkijono_on_tuntematon(capsys):
    from tervehdys import tervehdys

    tervehdys('')
    captured = capsys.readouterr()
    assert 'Hei tuntematon!' in captured.out

def test_none_on_tuntematon(capsys):
    from tervehdys import tervehdys

    tervehdys(None)
    captured = capsys.readouterr()
    assert 'Hei tuntematon!' in captured.out

