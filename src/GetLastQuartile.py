from typing import Dict, List

RatingType = Dict[str, float]


class GetLastRatingQuartile():
    def calc(self, students_rating: RatingType) -> float:
        ratings: List[float] = [students_rating[x]
                                    for x in students_rating]
        length: int = len(ratings)
        if length % 4 == 0:
            ratings.sort(reverse=True)  # descending
            return ratings[length//4]
        else:
            ratings.sort()  # ascending
            length: int = len(ratings)
            f_values: List[float] = [i/(length-1) for i in range(length)]
            lower: float = f_values[0]
            upper: float = f_values[0]
            for i in range(length):
                if f_value_list[i] > 0.75:
                    upper = i
                    break
                else:
                    lower = i
            diff_f_values: float = f_values[upper] - f_values[lower]
            diff_75: float = 0.75 - f_values[lower]
            ratio: float = diff_75 / diff_f_values
            diff_values: float = ratings[upper] - ratings[lower]
            quartile: float = ratings[upper] + diff_values * ratio
            return quartile
