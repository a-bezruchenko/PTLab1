from typing import Dict, Tuple, List
from Types import DataType
from GetRatingLastQuartile import GetRatingLastQuartile
import pytest


RatingsType = Dict[str, float]


class TestCalcRating():
    @pytest.fixture()
    def test_cases(self) -> List[Tuple[RatingsType, float]]:
        test_cases: List[Tuple[RatingsType, float]] = [
            ({"a": 1, "b": 2, "c": 3, "d": 4}, 3),
            ({"a": 1, "b": 2}, 1.75)
            ]
        return test_cases

    def test_calc(self, test_cases:
                  List[Tuple[RatingsType, float]]) -> None:
        for test_case in test_cases:
            rating: RatingsType
            expected_quartile: float
            rating, expected_quartile = test_case
            quartile: float = GetRatingLastQuartile().calc(rating)
            assert pytest.approx(quartile, abs=0.001) == expected_quartile
