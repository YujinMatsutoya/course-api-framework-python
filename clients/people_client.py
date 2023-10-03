from clients.base_client import BaseClient
from utils.requests import APIRequest
import config
import json
from utils.print_helpers import pretty_print
from uuid import uuid4

class PeopleClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_uri = config.BASE_URI
        self.request = APIRequest()

    def get_all_people(self):
        response = self.request.get(self.base_uri)
        return response

    def get_person_by_id(self, person_id):
        response = self.request.get(f"{self.base_uri}/{person_id}")
        return response
        
    def get_person_by_lname(self, lname):
        # people = requests.get(BASE_URI).json()
        response = self.get_all_people().as_json

        match_person = [person for person in response if person['lname'] == lname]
        return match_person[0]
    
    def get_pid_by_lname(self, lname):
         person = self.get_person_by_lname(lname)
         pid = person['person_id']
         return pid

    def create_person(self, body = None):
            if body == None:
                lname = f"lname {str(uuid4())}"
                payload = json.dumps({
                    'fname': 'default',
                    'lname': lname
                })
                pretty_print(payload)
                pretty_print(self.headers)
                pretty_print(self.base_uri)
            else:
                lname = body['lname']
                payload = json.dumps(body)
            
            response = self.request.post(self.base_uri, self.headers, payload)
            return response
    
    def delete_person(self, person_id):
         response = self.request.delete(f"{self.base_uri}/{person_id}")
         return response
    
    def update_person(self, person_id, body):
        response = self.request.put(f"{self.base_uri}/{person_id}", self.headers, body)
        return response