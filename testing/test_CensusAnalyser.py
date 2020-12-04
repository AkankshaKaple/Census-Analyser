from CensusAnalyserError import CensusAnalyserError
from CsvLoader import CSVLoader
import pytest

CENSUS_CSV_FILE_PATH = "/home/akanksha/PycharmProjects/CensusAnalyzer/Data/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "/home/akanksha/PycharmProjects/CensusAnalyzer/Data/USCensusData.xls"

# NOTE - Change delimiter of the file and save it
CENSUS_CSV_FILE_WRONG_DELIMITER = "/home/akanksha/PycharmProjects/CensusAnalyzer/Data/USCensusDataDelimiter.csv"


# check if length of records is same or not
def test_record_counter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_PATH)
    assert csv_loader.load_census_data() == 29


# Check if exception gets raised or not
def test_record_counter_for_wrong_file_path():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_census_data()


# Check if exception gets raised or not
def test_record_counter_for_wrong_file_type():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_census_data()


# Check if exception gets raised or not
# NOTE - Change delimiter of the file and save it
def test_record_counter_for_wrong_delimiter():
    csv_loader = CSVLoader(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        csv_loader.load_census_data()



