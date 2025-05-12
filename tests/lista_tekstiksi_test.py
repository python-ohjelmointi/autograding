"""
Import-komennot on tässä moduulissa toteutettu kunkin testin alussa, jotta
testattavan moduulin puuttuminen tai virheellisyys ei estäisi testien latautumista.
"""


def test_yksi_sana():
    from lista_tekstiksi import lista_tekstiksi

    teksti = lista_tekstiksi(['Python'])

    # saliitaan tyhjät merkit alusta ja lopusta
    assert teksti.strip() == 'Python'


def test_kaksi_sanaa():
    from lista_tekstiksi import lista_tekstiksi

    teksti = lista_tekstiksi(['Python', 'TypeScript'])

    # saliitaan tyhjät merkit alusta ja lopusta
    assert teksti.strip() == 'Python ja TypeScript'

def test_kolme_sanaa():
    from lista_tekstiksi import lista_tekstiksi

    teksti = lista_tekstiksi(['Python', 'Java', 'TypeScript'])
    assert teksti == 'Python, Java ja TypeScript'

def test_tyhja_lista():
    from lista_tekstiksi import lista_tekstiksi

    assert lista_tekstiksi([]) == ''


def test_suuri_maara_sanoja():
    from lista_tekstiksi import lista_tekstiksi

    teksti = lista_tekstiksi(['Python'] * 1_000)  # ei heitä poikkeusta
    assert teksti.count('Python') == 1_000
    assert teksti.count('Python,') == 998
    assert teksti.endswith('ja Python') == 1

