from TextDataReader import TextDataReader
from CalcRating import CalcRating
from GetRatingLastQuartile import GetRatingLastQuartile
from JsonDataReader import JsonDataReader
import argparse
import sys
from pprint import pprint

def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path

def main():
    text_path = get_path_from_arguments(sys.argv[1:3])
    reader = TextDataReader()
    students = reader.read(text_path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    json_path = get_path_from_arguments(sys.argv[3:5])
    json_reader = JsonDataReader()
    students = json_reader.read(json_path)
    print("Students:")
    pprint(students)
    qg = GetRatingLastQuartile()
    rating = CalcRating(students).calc()
    print("Last quartile: ", qg.calc_last_quartile(rating))
    print("Last quartile students: ")
    qg.print_last_quartile_students(rating)


if __name__ == "__main__":
    main()
