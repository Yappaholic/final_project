import pytest
from project import calculate, enter, result 

def test_calculate():
    assert calculate([4, 2, 1, 3]) == -11

def test_enter():
    with pytest.raises(SystemExit):
        enter("dog")
    with pytest.raises(SystemExit):
        enter("2")

def test_result():
    assert result(10) == "Your ups and downs are considered normal"
    assert result(34) == "You might have severe depression"
