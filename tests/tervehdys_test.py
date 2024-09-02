"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_funktio_on_olemassa():
    from tervehdys import tervehdi

    # tämä testi menee läpi, kunhan kutsu ei heitä poikkeusta:
    tervehdi('Matti', 'en')


def test_nimi_loytyy_tulosteesta(capsys):
    from tervehdys import tervehdi

    tervehdi('Mira', 'fi')
    tervehdi('Heikki', 'en')
    tervehdi('Aino', 'sv')

    captured = capsys.readouterr()
    assert 'Mira' in captured.out
    assert 'Heikki' in captured.out
    assert 'Aino' in captured.out


def test_tervehdys_oikein_eri_kielilla(capsys):
    from tervehdys import tervehdi

    tervehdi('Mira', 'fi')
    assert 'Hei Mira!' in capsys.readouterr().out

    tervehdi('Heikki', 'en')
    assert 'Hello Heikki!' in capsys.readouterr().out

    tervehdi('Aino', 'sv')
    assert 'Hej Aino!' in capsys.readouterr().out


def test_tuntematon_kieli(capsys):
    from tervehdys import tervehdi

    tervehdi('Jaakko', '')       # tyhjä kieli
    assert 'Hello Jaakko!' in capsys.readouterr().out

    tervehdi('Jaakko', 'de')     # tuntematon kieli
    assert 'Hello Jaakko!' in capsys.readouterr().out


def test_puuttuva_nimi(capsys):
    from tervehdys import tervehdi

    tervehdi('', 'fi')          # tyhjä nimi
    assert 'Hello stranger!' in capsys.readouterr().out

    tervehdi(None, 'fi')        # puuttuva nimi
    assert 'Hello stranger!' in capsys.readouterr().out
