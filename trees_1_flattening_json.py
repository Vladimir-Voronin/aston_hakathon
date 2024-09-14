"""Link to problem description:
https://docs.google.com/document/d/1dTcUMWCBmHV9dfWBsZrPyzRZTZJEEls7PlatPT7H9jo/edit?usp=sharing"""

import pytest
from utils.hints import show_file_hints


def flattening_json(json_obj: dict) -> dict:
    """Сглаживаю json ༼ °͜° ༽"""
    # Пиши код сюда


if __name__ == '__main__':
    example_input = {
        "id": 1,
        "name": "Vova",
        "department": {
            "address": "Konyev Street, 47",
            "projects": [
                {
                    "project_name": "Alpha",
                    "tech_stack": [
                        "Python",
                        "Postgres",
                        "Hadoop"
                    ]
                },
                {
                    "project_name": "Sigma",
                    "tech_stack": [
                        "C#",
                        "Oracle",
                        "WPF"
                    ]
                }
            ]
        }
    }

    # Check how your function work
    print(flattening_json(example_input))

    # Take some hints
    # show_file_hints(hint_level=1, show_all=False)

    # Test your example_input
    # pytest.main(["--color=yes", "-v", "test/test_trees.py::test_trees_1_flattening_json_example"])

    # Full test
    # pytest.main(["--color=yes", "-v", "test/test_trees.py::test_1_flattening_json_full"])
