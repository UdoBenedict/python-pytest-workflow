from src.calculator import add, multiply

def test_add():
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(-2, -2) == -4

def test_multiply():
    assert multiply(1, 3) == 3
    assert multiply(1, -2) == -2
    assert multiply(0, 3) == 0