from app import total_ht


def test_total():
    assert total_ht(3, 20) == 60


def test_zero():
    assert total_ht(0, 20) == 0


def test_quantite_negative():
    try:
        total_ht(-1, 20)
    except ValueError:
        return
    assert False, "Une quantite negative doit etre refusee"


def test_prix_negatif():
    try:
        total_ht(1, -20)
    except ValueError:
        return
    assert False, "Un prix negatif doit etre refuse"
