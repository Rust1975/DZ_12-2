import pytest
from utils import arrs


@pytest.mark.parametrize('array, start, end, expected' [
    ([1, 2, 3, 4], int(1), int(3), [2, 3]),
    ([1, 2, 3], int(1), [2, 3]),
    ([1, 2, 3], int(-2), int(-1), [2]),
    ([1, 2, 3], None, int(-4), []),
    ([], int(0), int(-2), [])
])

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array, start, end, expected):
    assert arrs.my_slice(array, int(start), int(end)) == expected
#    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
#    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
#    assert arrs.my_slice([1, 2, 3], -2, -1) == [2]
#    assert arrs.my_slice([1, 2, 3], None, -4) == []
#    assert arrs.my_slice([], 0, -2) == []