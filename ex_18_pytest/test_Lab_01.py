import pytest

@pytest.mark.smoke
def test_method1():
    print("Hello Word")
    assert 5 == 6


@pytest.mark.smoke
def test_method2():
    print("hello world")
    assert 5 == 5



