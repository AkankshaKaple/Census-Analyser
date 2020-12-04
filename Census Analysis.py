import pandas as pd


class CSVLoader:

    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        data = pd.read_csv(self.path)
        return len(data)
