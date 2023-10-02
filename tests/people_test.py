import requests
import json
from uuid import uuid4

from config import BASE_URI
from utils.print_helpers import pretty_print

def test_get_read_all_contains_kent():
    # call requests.get() to return a list of people
    people = get_all_people()
    # list comprehension to make a list of firstnames
    first_names = [person['fname'] for person in people]
    assert 'Kent' in first_names


def test_get_person_kent():
    person = get_person_by_id(2)
    assert person['lname'] == "Brockman"


def test_delete_person(create_data):
    person = create_unique_person(create_data)
    pid_unique = person['person_id']

    response = requests.delete(f"{BASE_URI}/{pid_unique}")
    assert response.status_code == 200


def test_create_person(create_data):
    count_before = len(get_all_people())
    person = create_unique_person(create_data)
    pid = person['person_id']
    count_after = len(get_all_people())

    assert count_after == count_before + 1   

    requests.delete(f"{BASE_URI}/{pid}")


def test_update_person(create_data):
    person = create_unique_person(create_data)
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
    response.status_code == 200
    requests.delete(f"{BASE_URI}/{pid}")

    


def create_unique_person(body = None):
    
    if body == None:
        lname = f"lname {str(uuid4())}"
        payload = json.dumps({
            'fname': 'default',
            'lname': lname
        })
    else:
        lname = body['lname']
        payload = json.dumps(body)
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(BASE_URI, headers=headers, data=payload)
    assert response.status_code == 204
    unique_person = get_person_by_lname(lname)
    return unique_person

# def create_unique_person(fname = 'Firsty', lname = 'User'):
#     unique_fname, unique_lname = f"{fname} {str(uuid4())}", f"{lname} {str(uuid4())}"

#     payload = json.dumps({
#         'fname': unique_fname,
#         'lname': unique_lname
#     })
    
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#     }

#     response = requests.post(BASE_URI, headers=headers, data=payload)
#     assert response.status_code == 204
#     unique_person = get_person_by_lname(unique_lname)
#     return unique_person

def get_all_people():
    response = requests.get(BASE_URI)
    people = response.json()
    assert response.status_code == 200
    return people

def get_person_by_lname(lname):
    people = requests.get(BASE_URI).json()
    match_person = [person for person in people if person['lname'] == lname]
    return match_person[0]
    
def get_person_by_id(person_id):
    response = requests.get(f"{BASE_URI}/{person_id}")
    assert response.status_code == 200
    return response.json()