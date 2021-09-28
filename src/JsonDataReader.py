from Types import DataType
from DataReader import DataReader
import json

class JsonDataReader(DataReader):
    def read(self, path: str) -> DataType:
        file_text : str
        parsed_file : DataType
        with open(path, "r", encoding="utf-8") as file:
            file_text = file.read()    
        parsed_file = json.loads(file_text)
        return parsed_file
