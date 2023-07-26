import sys
import pytest

sys.path.append('.')

from src.invoice_generator.data_loaders.csv_loader import load_csv


@pytest.mark.data_loader
@pytest.mark.parametrize(
    'file_path, separator, expected',
    [
        ('tests/test_data_loaders/test_data/test_csv_loader_sep_coma.csv', ',', [
            {'name': 'John', 'surname': 'Doe', 'age': '25'},
            {'name': 'Jane', 'surname': 'Doe', 'age': '24'},
            {'name': 'John', 'surname': 'Smith', 'age': '30'},
        ]),
        ('tests/test_data_loaders/test_data/test_csv_loader_sep_semicolon.csv', ';', [
            {'name': 'John', 'surname': 'Doe', 'age': '25'},
            {'name': 'Jane', 'surname': 'Doe', 'age': '24'},
            {'name': 'John', 'surname': 'Smith', 'age': '30'},
        ]),
    ]
)
def test_load_csv(file_path: str, separator: str, expected: list[dict]) -> None:
    """
    Test load_csv function
    :param file_path: str - path to csv file
    :param separator: str - csv separator
    :param expected: list[dict] - expected data
    :return: None
    """

    assert load_csv(file_path, separator) == expected


@pytest.mark.data_loader
def test_load_csv_non_existing_file() -> None:
    """
    Test load_csv function with non-existing file
    :return: None
    """

    with pytest.raises(FileNotFoundError):
        load_csv('tests/test_data_loaders/test_data/test_csv_loader_non_existing_file.csv')


@pytest.mark.data_loader
def test_load_csv_empty_file() -> None:
    """
    Test load_csv function with empty file
    :return: None
    """

    assert load_csv('tests/test_data_loaders/test_data/test_csv_loader_empty_file.csv') == []
