from mypackage.main import add, double, sub, times

def test_add():
    a = 3
    b = 4
    assert add(a, b) == 7

def test_sub():
    a = 3
    b = 4
    assert sub(a, b) == -1

def test_times():
    a = 3
    b = 4
    assert times(a, b) == 12

def test_double():
    a = 3
    assert double(a) == 6