import pandas as pd

from CensusAnalyserError import CensusAnalyserError
from IndianCensusCSV import IndiaCensusCSV, StateCensusCSV


class CSVLoader:

    def __init__(self, path):
        self.path = path

    def load_census_data(self):
        """
        Load census data and return number of 
        :return: number of records in file
        """
        try:
            census_col_list = repr(IndiaCensusCSV()).split(",")
            census_data = pd.read_csv(self.path, usecols=census_col_list)
            return len(census_data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")

    def load_state_census_data(self):
        """
        Load state census data and return number of
        :return: number of records in file
        """
        try:
            state_col_list = repr(StateCensusCSV()).split(",")
            state_data = pd.read_csv(self.path, usecols=state_col_list)
            return len(state_data)
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")