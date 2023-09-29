from fuel import convert, gauge
from pytest import raises

def main():
    test_convert()
    test_gauge()
    test_zero_divisor()
    test_value_error()

def test_convert():
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"

def test_zero_divisor():
    with raises(ZeroDivisionError):
        assert convert("1/0")

def test_value_error():
    with raises(ValueError):
        assert convert(10)

if __name__ == "__main__":
    main()