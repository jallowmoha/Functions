
from func import first_smallest, second_smallest, n_smallest
import pytest

""" testdata, testdata2, testdata3 and 
testdat_exception are the test cases for 
the unit tests """

testdata = [
    ([2, -1, 5, 7, 10, 7], -1),
    ([2, 7, 4, 5, 10, 7], 2),
    ([], False),
    ([5, 5, 5, 5, 5, 5], 5)


]
testdata2 = [
    ([2, -1, 5, 7, 10, 7], 2),
    ([-1, 0, 5, 7, 10, 7], 0),
    ([], False),
]
testdata3 = [
    ([2, -1, 5, 7, 10, 7], 1, -1),
    ([2, -1, 5, 7, 10, 7], 3, 5),
    ([], 5, False),
    ([5, 5, 5, 5, 5, 5], 4, 5)


]
testdata_exception = [
    
    [2, -1, 5, 1.5, 10, 7],
    [2, -1, 5, "Hello", 10, 7],
  


]
#test for first_smallest function

@pytest.mark.parametrize ("firstSmallest, expected_result", testdata)
def test_first_smallest(firstSmallest, expected_result):
  assert first_smallest(firstSmallest) == expected_result
    
#unit test for second_smallest function
@pytest.mark.parametrize ("secondSmallest, expected_result", testdata2)
def test_second_smallest(secondSmallest, expected_result):
    assert second_smallest(secondSmallest) == expected_result

#unit test for n_smallest function
@pytest.mark.parametrize ("nSmallest, n, expected_result", testdata3)
def test_n_smallest(nSmallest, n, expected_result):
    assert n_smallest(nSmallest, n) == expected_result

#unit test for first_smallest function exception
@pytest.mark.parametrize ("firstSmallest", testdata_exception)
def test_execptions(firstSmallest):
    with pytest.raises(Exception) as exc:
        first_smallest(firstSmallest)
    assert "Only integers are allowed" in str(exc.value)
    assert exc.type == TypeError
