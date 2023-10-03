# import pytest
# import requests
import json
from uuid import uuid4

from clients.people_client import PeopleClient
from utils.print_helpers import pretty_print

client = PeopleClient()   


def test_get_read_all_containing_kent():
    response = client.get_all_people()
    people = response.as_json

    assert response.status_code ==200
    first_names = [person['fname'] for person in people]
    assert 'Kent' in first_names


def test_get_person_kent():
    response = client.get_person_by_id(2)

    assert response.status_code == 200
    assert response.as_json['lname'] == 'Brockman'


def test_delete_person(create_data):

    client.create_person(create_data)

    pid = client.get_pid_by_lname(create_data['lname'])
    response = client.delete_person(pid)
    assert response.status_code == 200
    
    response_get = client.get_person_by_id(pid)
    assert response_get.status_code ==404         
       

def test_create_person(create_data):
    person_count = len(client.get_all_people().as_json)
    response = client.create_person(create_data)
    person_count_after = len(client.get_all_people().as_json)

    assert person_count_after == person_count + 1   
    assert response.status_code == 204

    pid = client.get_pid_by_lname(create_data['lname'])
    response = client.delete_person(pid)
    assert response.status_code == 200


def test_update_person(create_data):
    client.create_person(create_data)
    pid = client.get_pid_by_lname(create_data['lname'])

    payload = json.dumps({
        "fname": "Moses",
        "lname": "Sumney"
    })

    response = client.update_person(pid, payload)
    assert response.status_code == 200
    new_pid = client.get_pid_by_lname('Sumney')
    client.delete_person(new_pid)


# def test_update_with_existing_person():
    