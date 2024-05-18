"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""

def test_luvut_jarjestyksessa_ykkosesta_alkaen():
    from puuttuva_luku import etsi_puuttuva_luku

    assert etsi_puuttuva_luku([1, 2, 3, 4, 6, 7]) == 5

def test_luvut_jarjestyksessa_kympista_alkaen():
    from puuttuva_luku import etsi_puuttuva_luku

    assert etsi_puuttuva_luku([10, 11, 12, 14, 15]) == 13

def test_luvut_epajarjestyksessa():
    from puuttuva_luku import etsi_puuttuva_luku

    assert etsi_puuttuva_luku([2, 6, 4, 3]) == 5

def test_negatiiviset_luvut():
    from puuttuva_luku import etsi_puuttuva_luku

    assert etsi_puuttuva_luku([-1, -2, -3, -4, -6, -7]) == -5

def test_positiiviset_ja_negatiiviset_luvut():
    from puuttuva_luku import etsi_puuttuva_luku

    assert etsi_puuttuva_luku([-1, -3, 0, 1, 2, 3]) == -2
