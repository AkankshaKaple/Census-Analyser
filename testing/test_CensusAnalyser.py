from CensusAnalyser import CensusAnalyser
from CensusAnalyserError import CensusAnalyserError
import pytest


CENSUS_CSV_FILE_PATH = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_PATH = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/WRONG-Resources/IndiaStateCensusData.csv"
CENSUS_CSV_FILE_WRONG_TYPE = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCensusData.txt"
CENSUS_CSV_FILE_WRONG_DELIMITER = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCensusData_WrongDelimiter.csv"
STATE_CODE_CSV_FILE_PATH = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_PATH = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/WRONG-Resources/IndiaStateCode.csv"
STATE_CODE_CSV_FILE_WRONG_TYPE = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCode.txt"
STATE_CODE_CSV_FILE_WRONG_DELIMITER = "/home/akanksha/Akanksha/Python FullStack/Census-Analyser/Resources/IndiaStateCodeWrongDelimiter.csv"


def test_givenIndiaCensusCSVFile_WhenCounted_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    assert census_analyser.census_record_counter() == 29


def test_givenIndiaCensusCSVFile_WhenWrongPath_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenWrongFileType_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenIndiaCensusCSVFile_WhenHeadersWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.census_record_counter()


def test_givenStateCodeCSVFile_WhenLoaded_ShouldReturnRecordsCount():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_PATH)
    assert census_analyser.state_code_record_counter() == 37


def test_givenStateCodeCSVFile_WhenPathWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenFileTypeWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_TYPE)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenDelimiterWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(STATE_CODE_CSV_FILE_WRONG_DELIMITER)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()


def test_givenStateCodeCSVFile_WhenHeadersWrong_ShouldRaiseException():
    census_analyser = CensusAnalyser(CENSUS_CSV_FILE_PATH)
    with pytest.raises(CensusAnalyserError):
        assert census_analyser.state_code_record_counter()

