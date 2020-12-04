import pandas as pd

from CensusAnalyserError import CensusAnalyserError
from IndianCensusCSV import IndiaCensusCSV, StateCensusCSV


class CSVLoader:

    def load_indian_census_data(path):
        """
        Load census data and return number of 
        :return: number of records in file
        """
        try:
            census_col_list = repr(IndiaCensusCSV()).split(",")
            census_data_list = pd.read_csv(path, usecols=census_col_list)
            return census_data_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")

    def load_state_code_data(path):
        """
        Load state census data and return number of
        :return: number of records in file
        """
        try:
            state_col_list = repr(StateCensusCSV()).split(",")
            state_data_list = pd.read_csv(path, usecols=state_col_list)
            return state_data_list
        except FileNotFoundError:
            raise CensusAnalyserError("Check file path")
        except ValueError:
            raise CensusAnalyserError("Wrong delimiter Or Headers do not match")