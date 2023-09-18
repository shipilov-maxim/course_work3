import json

from src.utils import load_json

@pytest.fixture
def json_data(tmp_path):
    data = [
        {},
        {
            "id": 1,
            "inner": {
                "inner_1": {
                    "inner_2": {
                        "inner_3": {
                            "data": "some_data"
                        }
                    }
                }
            }
        }
    ]

    path = tmp_path / "test_data.json"

    with open(path, "w") as test_data:
        test_data.write(json.dumps(data))

    return path


def test_load_json(json_data):
    handler = load_json()
    data = handler.get_data()

    assert list(data) == [
        {"id": 1, "data": "some_data"}
    ]
