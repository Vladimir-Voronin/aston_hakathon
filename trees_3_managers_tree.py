"""link to problem description:
https://docs.google.com/document/d/16z_JU1bmNfSwkMC4tldC1_fVPj543__nAHyIOnNbMa0/edit?usp=sharing
"""
from __future__ import annotations
from dataclasses import dataclass, field
import pytest
from utils.hints import show_file_hints


@dataclass(frozen=True)
class Employee:
    """Dataclass работника. Значения по умолчанию можно изменить, хотя для решения задачи
    это необязательно"""
    id: int
    manager_id: int
    name: str = "Unknown"
    salary: int = 0


@dataclass
class TreeNode:
    """Узел дерева. Так количество детей неизвестно заранее, children имеет тип list."""
    employee_obj: Employee
    children: list[TreeNode] = field(default_factory=list)


def create_manager_tree(json_list: list[dict]) -> TreeNode:
    """Строю дерево и возвращаю его корень на основе списка json объектов"""
    # Пиши код сюда


if __name__ == '__main__':
    example_input = [
        {
            "id": 6,
            "name": "Paskuda)",
            "manager_id": 4
        },
        {
            "id": 8,
            "name": "Chudovishe",
            "manager_id": 5
        },
        {
            "id": 7,
            "name": "Krisa",
            "salary": 90000,
            "manager_id": 4
        },
        {
            "id": 1,
            "name": "Gnida",
            "salary": 50000,
            "manager_id": 2
        },
        {
            "id": 2,
            "name": "Tvar`",
            "salary": 100000,
            "manager_id": None
        },
        {
            "id": 3,
            "name": "Yrod",
            "salary": 40000,
            "manager_id": 1
        },
        {
            "id": 4,
            "name": "Mraz'",
            "salary": 60000,
            "manager_id": 1
        },
        {
            "id": 5,
            "name": "Chert",
            "salary": 50000,
            "manager_id": 4
        },
    ]

    # Check how your function work
    print(create_manager_tree(example_input))

    # Take some hints
    # show_file_hints(hint_level=1, show_all=False)

    # Test your example_input (возможно этот тест не очень)
    # pytest.main(["--color=yes", "-v", "test/test_trees.py::test_trees_3_managers_tree_example"])
