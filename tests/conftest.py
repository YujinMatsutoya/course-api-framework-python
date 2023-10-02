import pytest, json
from uuid import uuid4

from pathlib import Path

# import create_person


@pytest.fixture
def create_data():
    
    file_path = Path.cwd().joinpath('tests', 'data', 'create_person.json')
    
    with open(file_path) as f:
        payload = json.load(f)

    lname = f"Last {str(uuid4())}"
    payload['lname'] = lname

    yield payload
    