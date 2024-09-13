from answers.trees_1_flattening_json import flattening_json


def test_trees_1_flattening_json_example():
    input = {
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
    assert flattening_json(input) == flattening_json(output)


def test_1_flattening_json_full():
    test_trees_1_flattening_json_example()
