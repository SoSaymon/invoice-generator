from csv import DictReader


def load_csv(file_path: str, separator: str = ',') -> list[dict]:
    """
    Load data from csv file
    :param file_path: str - path to csv file
    :param separator: str - csv separator
    :return: list[dict] - list of dictionaries with data
    """

    with open(file_path, 'r') as csv_file:
        csv_reader: DictReader = DictReader(csv_file, delimiter=separator)
        data: list[dict] = [row for row in csv_reader]
    return data
