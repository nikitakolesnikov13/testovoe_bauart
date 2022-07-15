import clickhouse_driver
from clickhouse_driver import Client
from csv import DictReader
from datetime import datetime
import pandas as pd


class Repository:
    def __init__(self):
        self.client = Client("localhost")

    @classmethod
    def reader(cls):
        filename = "PurchasingExample correct.csv"

        with open(filename, 'r') as f:
            reader = DictReader(f)
            for line in reader:
                yield line.items()

    def create_table(self):
        self.client.execute(
            'CREATE TABLE IF NOT EXISTS csv '
            '('
            'Case_ID Int32,'
            'Start_Timestamp DateTime, '
            'Complete_Timestamp DateTime, '
            'Activity String, '
            'Resource String, '
            'Role String'
            ') Engine = engine'
        )
        self.client.execute('INSERT INTO data_csv VALUES', self.reader("PurchasingExample correct.csv"))

    def check(self):
        return self.client.execute("SHOW TABLES")

    def group_by(self):
        pass

    def drop_file(self):
        pass


client = Client("localhost")


def reader_CSV():
    filename = "PurchasingExample correct.csv"

    with open(filename, 'r') as f:
        reader = DictReader(f)
        dict_from_csv = dict(list(reader)[0])
        list_of_column_names = list(dict_from_csv.items())
pd.read_csv("PurchasingExample correct.csv")