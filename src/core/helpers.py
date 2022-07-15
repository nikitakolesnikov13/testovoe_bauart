from csv import DictReader
from datetime import datetime
from typing import Dict



heuristics = (lambda value: datetime.strptime(value, "%Y-%m-%d %H:%M:%S"),
              int, float)

def data_reader(file) -> Dict:
    with open(file, 'r') as f:
        reader = DictReader(f)
        columns = reader.fieldnames
        data = [x.strip('"') for x in f.readline().split(",")]
    return {"data": data, "columns": columns}


def convert(value):
    for type in heuristics:
        try:
            return type(value)
        except ValueError:
            continue
    return value


def prepare_data_to_query(file) -> tuple:
    pd = data_reader(file)
    for value in pd["data"]:
        converted_value = convert(value)
        return (converted_value, type(converted_value))



