import pytest

from . import bignumber


def test_add():
    digits = bignumber.BigNumber([1, 8, 3, 1])
    result = digits + [4, 9, 8, 2]
    assert result == [6, 8, 1, 3]
    digits = bignumber.BigNumber([3, 1])
    result = digits + [4, 9, 8, 2]
    assert result == [5, 0, 1, 3]


def test_sub():
    digits = bignumber.BigNumber([8, 0, 0, 3])
    result = digits - [8, 0, 0, 3]
    assert result == [0]
    result = digits - [2, 2, 6, 7, 9]
    assert result == ["-", 1, 4, 6, 7, 6]


def test_mul():
    digits = bignumber.BigNumber([3, 2, 5])
    result = digits * [2, 5]
    assert result == [8, 1, 2, 5]
    result = digits * [6, 9, 4, 5]
    assert result == [3, 8, 1, 9, 7, 5]


def test_validation():
    with pytest.raises(bignumber.FirstNumberError) as e:
        bignumber.BigNumber([0, 2, 5])
    assert str(e.value) == "First digit cannot be 0"

    with pytest.raises(TypeError) as e:
        bignumber.BigNumber("string")
    assert str(e.value) == "The value must be passed in a list"

    with pytest.raises(bignumber.NumbersInListError) as e:
        bignumber.BigNumber([3, 5, "string"])
    assert str(e.value) == "The value in the list must be numbers"

    with pytest.raises(bignumber.OutOfRangeError) as e:
        bignumber.BigNumber([3, 5, 15])
    assert str(e.value) == "The value in the list must be in range 0 to 9"

