"""Testing functions related to tree problems"""

from trees_1_flattening_json import flattening_json
from answers.answer_trees_3 import create_manager_tree as create_manager_tree_solution
from trees_3_managers_tree import create_manager_tree


def test_trees_1_flattening_json_example():
    """Small test based on one input."""
    data_input = {
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
    output = {
        "id": 1,
        "name": "Vova",
        "department_address": "Konyev Street, 47",
        "department_projects_1_project_name": "Alpha",
        "department_projects_1_tech_stack_1": "Python",
        "department_projects_1_tech_stack_2": "Postgres",
        "department_projects_1_tech_stack_3": "Hadoop",
        "department_projects_2_project_name": "Sigma",
        "department_projects_2_tech_stack_1": "C#",
        "department_projects_2_tech_stack_2": "Oracle",
        "department_projects_2_tech_stack_3": "WPF"
    }
    result = flattening_json(data_input)
    assert isinstance(result,
                      dict), (f'Возвращаемое значение должно быть типа dict. '
                              f'В вашем случае return_val == {type(result)}')
    assert result == output


def test_1_flattening_json_full():
    """Full test based on several inputs."""
    input_1 = {}
    output_1 = {}
    input_2 = {
        "photos": {
            "page": 1,
            "pages": "11824",
            "perpage": 2,
            "total": "23648",
            "photo": [
                {
                    "id": "50972466107",
                    "owner": "191126281@N@7",
                    "secret": "Q6f861f8b0",
                    "server": "65535",
                    "farm": 66,
                    "title": "Prompt & Reliable Electrolux Oven Repairs in Gold Coast",
                    "ispublic": 1,
                    "isfriend": 0,
                    "isfamily": 0
                },
                {
                    "id": "50970556873",
                    "owner": "49965961@NG0",
                    "secret": "21f7a6424b",
                    "server": "65535",
                    "farm": 66,
                    "title": "IMG_20210222_145514",
                    "ispublic": 1,
                    "isfriend": 0,
                    "isfamily": 0
                }
            ]
        },
        "stat": "ok"
    }
    output_2 = {
        "photos_page": 1,
        "photos_pages": "11824",
        "photos_perpage": 2,
        "photos_total": "23648",
        "photos_photo_1_id": "50972466107",
        "photos_photo_1_owner": "191126281@N@7",
        "photos_photo_1_secret": "Q6f861f8b0",
        "photos_photo_1_server": "65535",
        "photos_photo_1_farm": 66,
        "photos_photo_1_title": "Prompt & Reliable Electrolux Oven Repairs in Gold Coast",
        "photos_photo_1_ispublic": 1,
        "photos_photo_1_isfriend": 0,
        "photos_photo_1_isfamily": 0,
        "photos_photo_2_id": "50970556873",
        "photos_photo_2_owner": "49965961@NG0",
        "photos_photo_2_secret": "21f7a6424b",
        "photos_photo_2_server": "65535",
        "photos_photo_2_farm": 66,
        "photos_photo_2_title": "IMG_20210222_145514",
        "photos_photo_2_ispublic": 1,
        "photos_photo_2_isfriend": 0,
        "photos_photo_2_isfamily": 0,
        "stat": "ok"
    }

    test_trees_1_flattening_json_example()
    assert flattening_json(input_1) == output_1
    assert flattening_json(input_2) == output_2


def test_trees_3_managers_tree_example():
    """Recursive test, comparing trainee func implementation with my implementation."""

    def check_eq(node_check, node_standard):
        assert len(node_check.children) == len(
            node_standard.children), (
            f"In node with id {node_check.employee_obj.id} the length of children list is "
            f"not right.")
        if not node_check.children:
            return
        children_1 = sorted(node_check.children, key=lambda x: x.employee_obj.id)
        children_2 = sorted(node_standard.children, key=lambda x: x.employee_obj.id)
        for child_1, child_2 in zip(children_1, children_2):
            assert child_1.employee_obj == child_2.employee_obj, (
                f"Some of children in node with id"
                f" {node_check.employee_obj.id} are "
                f"not right")
            check_eq(child_1, child_2)

    example_input = [
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
    ]
    root_check = create_manager_tree(example_input)
    root_standard = create_manager_tree_solution(example_input)
    check_eq(root_check, root_standard)
