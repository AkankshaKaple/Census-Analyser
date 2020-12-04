from CsvLoader import CSVLoader
import pandas as pd
from IndianCensusCSV import IndiaCensusCSV, StateCensusCSV


class CensusAnalyser:
    __data_list = pd.DataFrame()

    def __init__(self, path):
        self.path = path

    def census_record_counter(self):
        CensusAnalyser.__data_list = CSVLoader.load_indian_census_data(self.path)
        return len(CensusAnalyser.__data_list)

    def state_code_record_counter(self):
        CensusAnalyser.__data_list = CSVLoader.load_state_code_data(self.path)
        return len(CensusAnalyser.__data_list)

    def sort_by_state(self):
        CensusAnalyser.__data_list.sort_values(by=IndiaCensusCSV().state, inplace=True)
        return CensusAnalyser.__data_list.to_json(orient='records')

    def sort_by_stateCode(self):
        CensusAnalyser.__data_list.sort_values(by=StateCensusCSV().state_code, inplace=True)
        return CensusAnalyser.__data_list.to_json(orient='records')


