from Types import DataType
from DataReader import DataReader
import json


class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        file_text : str
        parsed : DataType
        result : DataType
        with open(path, "r", encoding="utf-8") as file:
            file_text = file.read()    
        parsed = json.loads(file_text)
        result = {x : list(parsed[x].items()) for x in parsed}
        return result
