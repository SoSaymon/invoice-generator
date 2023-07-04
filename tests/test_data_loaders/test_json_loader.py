import sys
import pytest

sys.path.append(".")

from src.invoice_generator.data_loaders.json_loader import load_json


@pytest.mark.parametrize(
    "file_path, expected",
    [
        ("tests/test_data_loaders/test_data/test_json_loader.json", [
            {'name': 'John', 'surname': 'Doe', 'age': 25},
            {'name': 'Jane', 'surname': 'Doe', 'age': 24},
            {'name': 'John', 'surname': 'Smith', 'age': 30},
        ]),
    ]
)
def test_load_json(file_path: str, expected: list[dict]) -> None:
    """
    Test load_json function
    :param file_path: str - path to json file
    :param expected: list[dict] - expected data
    :return: None
    """

    assert load_json(file_path) == expected


def test_load_json_non_existing_file() -> None:
    """
    Test load_json function with non-existing file
    :return: None
    """

    with pytest.raises(FileNotFoundError):
        load_json('tests/test_data_loaders/test_data/test_json_loader_non_existing_file.json')


def test_load_json_empty_file() -> None:
    """
    Test load_json function with empty file
    :return: None
    """

    assert load_json('tests/test_data_loaders/test_data/test_json_loader_empty_file.json') == []

