import pytest

from src.math_utils import add, mean


def test_add_returns_sum():
    assert add(2, 3) == 5
    assert add(-1.5, 0.5) == -1.0


def test_mean_returns_average():
    assert mean([1.0, 2.0, 3.0]) == 2.0
    assert mean((0.0, 0.0)) == 0.0


def test_mean_raises_on_empty_iterable():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        mean(iter([]))
