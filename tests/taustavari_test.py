"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_funktio_kunnossa():
    from taustavari import taustavari
    assert type(taustavari(0)) == str

def test_otsikkorivin_tausta():
    from taustavari import taustavari

    assert taustavari(0) == '#227447'

    from taustavari import TAUSTA_OTSIKKO
    assert taustavari(0) == TAUSTA_OTSIKKO

def test_ekan_rivin_tausta():
    from taustavari import taustavari, TAUSTA_PARITON

    assert taustavari(1) == '#d9d9d9'

    assert taustavari(3) == TAUSTA_PARITON

def test_toka_rivi():
    from taustavari import taustavari, TAUSTA_PARILLINEN

    assert taustavari(2) == '#ffffff'
    assert taustavari(4) == TAUSTA_PARILLINEN

def test_isot_rivimumerot():
    from taustavari import taustavari

    assert taustavari(10_000_000_002) == '#ffffff'
    assert taustavari(10_000_000_003) == '#d9d9d9'
