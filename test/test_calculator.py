from calculator import add, subtract

def test_add():
    assert add(2,3) == 5
    assert add(3,5) == 8
    assert add (0,0) == 0;
def test_subtract():
    assert subtract(2,1) == 1
    assert subtract(3,1) == 2
    assert subtract(8,7) == 1;
