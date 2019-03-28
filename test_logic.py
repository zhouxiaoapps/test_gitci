from logic import pick_bucket
import pytest

def test_bucket1():
    assert pick_bucket(4, 2) == 0
    assert pick_bucket(5, 2) == 1
    assert pick_bucket(4, 2) == pick_bucket(4)


def test_bucket2():
    with pytest.raises(AssertionError):
        pick_bucket(5, 0)

    with pytest.raises(AssertionError):
        pick_bucket(5, -1)
