import requests
import json
from uuid import uuid4

from config import BASE_URI
from utils.print_helpers import pretty_print

def test_get_read_all_contains_kent():
    response = requests.get(BASE_URI)
    people = response.json()
    pretty_print(people)

    assert response.status_code == 200
    first_names = [person['fname'] for person in people]
    assert 'Kent' in first_names


def test_get_person_kent():
    person = get_person_by_id(2)
    assert person['lname'] == "Brockman"


def test_delete_person():
    person = create_unique_person()
    pid_unique = person['person_id']

    response = requests.delete(f"{BASE_URI}/{pid_unique}")
    assert response.status_code == 200


def test_create_person():
    count_before = len(get_all_people())

    person = create_unique_person()
    pid = person['person_id']
    count_after = len(get_all_people())
    pretty_print(f"this is the new unique person - {person}")

    assert count_after == count_before + 1   

    requests.delete(f"{BASE_URI}/{pid}")


def tests_update_person():
    person = create_unique_person()
    pid = person['person_id']

    payload = json.dumps({
        "fname": "Moses",
        "lname": "Sumney"
    })

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.put(f"{BASE_URI}/{pid}", headers=headers, data=payload) 
    pretty_print(get_person_by_lname("Sumney"))
    response.status_code == 200
    requests.delete(f"{BASE_URI}/{pid}")

    




def create_unique_person(fname = 'Firsty', lname = 'User'):
    unique_fname, unique_lname = f"{fname} {str(uuid4())}", f"{lname} {str(uuid4())}"

    payload = json.dumps({
        'fname': unique_fname,
        'lname': unique_lname
    })
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(BASE_URI, headers=headers, data=payload)
    assert response.status_code == 204
    unique_person = get_person_by_lname(unique_lname)
    return unique_person

def get_all_people():
    response = requests.get(BASE_URI)
    people = response.json()
    return people

def get_person_by_lname(lname):
    people = requests.get(BASE_URI).json()
    match_person = [person for person in people if person['lname'] == lname]
    return match_person[0]
    
def get_person_by_id(person_id):
    response = requests.get(f"{BASE_URI}/{person_id}")
    assert response.status_code == 200
    return response.json()