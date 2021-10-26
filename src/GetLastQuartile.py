from typing import Dict, List

RatingType = Dict[str, float]


class GetLastRatingQuartile():
    def calc(self, students_rating: RatingType) -> float:
        rating_list : List[float] = [students_rating[x] for x in students_rating]
        length : int = len(rating_list)
        if length % 4 == 0:
            rating_list.sort(reverse=True) # descending
            return rating_list[length//4]
        else:
            rating_list.sort() # ascending
            length : int = len(rating_list)
            f_value_list : List[float] = [i/(length-1) for i in range(length)]
            last_lower : float = f_value_list[0]
            first_upper : float = f_value_list[0] 
            for i in range(length):
                if f_value_list[i] > 0.75:
                    first_upper = i
                    break
                else:
                    last_lower = i
            diff_pre_after : float = f_value_list[first_upper] - f_value_list[last_lower]
            diff_75 : float = 0.75 - f_value_list[last_lower]
            ratio : float = diff_75 / diff_pre_after
            diff_pre_after_values : float = rating_list[first_upper] - rating_list[last_lower]
            quartile : float = rating_list[first_upper] + diff_pre_after_values * ratio
            return quartile
        
