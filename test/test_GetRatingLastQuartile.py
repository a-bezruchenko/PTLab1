from typing import Dict, Tuple, List
from Types import DataType
from GetRatingLastQuartile import GetRatingLastQuartile
import pytest

from io import StringIO
import sys


RatingsType = Dict[str, float]
TestCases = List[Tuple[RatingsType, float]]


class TestCalcRating():
    @pytest.fixture()
    def test_cases(self) -> List[Tuple[RatingsType, float]]:
        test_cases: List[Tuple[RatingsType, float]] = [
            ({"a": 1, "b": 2, "c": 3, "d": 4}, 3),
            ({"a": 1, "b": 2}, 1.75)
            ]
        return test_cases

    def test_calc_last_quartile(self, test_cases: TestCases) -> None:
        for test_case in test_cases:
            rating: RatingsType
            expected_quartile: float
            rating, expected_quartile = test_case
            quartil: float = GetRatingLastQuartile().calc_last_quartile(rating)
            assert pytest.approx(quartil, abs=0.001) == expected_quartile

    def test_print_last_quartile_students(self, test_cases: TestCases) -> None:
        for test_case in test_cases:
            rating: RatingsType
            expected_quartile: float
            rating, expected_quartile = test_case
            old_stdout = sys.stdout
            mystdout = StringIO()
            sys.stdout = mystdout
            GetRatingLastQuartile().print_last_quartile_students(rating)
            sys.stdout = old_stdout
            output = mystdout.getvalue()
            assert output == "d"
