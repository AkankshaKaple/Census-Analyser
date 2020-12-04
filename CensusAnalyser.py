from CsvLoader import CSVLoader

class CensusAnalyser:

    def __init__(self, path):
        self.path = path

    def census_record_counter(self):
        indian_census_records = CSVLoader.load_indian_census_data(self.path)
        return len(indian_census_records)

    def state_code_record_counter(self):
        state_census_records = CSVLoader.load_state_code_data(self.path)
        return len(state_census_records)


