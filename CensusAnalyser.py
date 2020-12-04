import pandas as pd

from CensusAnalyserError import CensusAnalyserError
from IndianCensusCSV import IndiaCensusCSV

class CSVLoader:

    def __init__(self, path):
        self.path = path

    def record_counter(self):
        """
        Count record in file
        :return: number of records in file
        """
        try:
            state_col_list = repr(IndiaCensusCSV()).split(",")
            state_list = pd.read_csv(self.path, usecols=state_col_list)
            return len(state_list)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")