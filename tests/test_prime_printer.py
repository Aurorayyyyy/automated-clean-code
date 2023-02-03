from prime_printer import calclulate_prime


def test_prime_printer():
    page = int(len(calclulate_prime(769)) / (5 * 8)) + 1
    assert page == 4
    assert len(calclulate_prime(769)) == 136
    assert calclulate_prime(1) == list()
    assert calclulate_prime(2) == [2]
