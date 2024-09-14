"""Link to problem description:
https://docs.google.com/document/d/1jkpSkZWnAZO9qr5i7UOuS6_YZPg9ZlP3bhE7asfqB1I/edit?usp=sharing"""
import csv
from pathlib import Path
import pytest
from utils.hints import show_file_hints


def find_real_and_fake_csv() -> tuple[list[Path], list[Path]]:
    """real csv format is: 'id\tname\tage\tweight' and has at least one row of data"""
    source_dir = Path(r'data/analytical_chaos')
    real_csv_paths = []
    fake_csv_paths = []

    # Пиши код сюда

    return real_csv_paths, fake_csv_paths


if __name__ == '__main__':
    # Check what your function returns
    print(find_real_and_fake_csv())

    # Take some hints
    # show_file_hints(hint_level=1, show_all=False)

    # Для этой задачи нет тестов
