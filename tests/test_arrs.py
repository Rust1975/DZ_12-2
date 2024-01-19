import pytest
from utils import arrs
@pytest.fixture()
def my_first_fixture():
    return [1, 2, 3]

@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, 3, [2, 3]),
    ([1, 2, 3], -2, -1, [2]),
    ([1, 2, 3], None, -4, []),
    ([], 0, -2, [])
])
def test_slice(array, start, end, expected, my_first_fixture):
    assert arrs.my_slice(array, start, end) == expected


def test_get():
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([], 0, "test") == "test"