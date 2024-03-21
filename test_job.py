import pytest
from job import job

def test_mean():
    test_cases = [
        ([1, 2, 3, 4, 5], 3.0),
        ([5, 5, 5, 5, 5], 5.0),
        ([0, 0, 0, 0, 0], 0.0),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ]

    for nums, expected_mean in test_cases:
        assert mean(nums) == expected_mean
