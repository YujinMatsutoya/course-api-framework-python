from dataclasses import dataclass
import requests

@dataclass
class Response:
    status_code: int
    text: str
    as_json: object
    headers: dict

class APIRequest():
    
    def get(self, url):
        response = requests.get(url)
        return self.get_response(response)
    
    def post(self, url, headers, payload):
        response = requests.post(url, headers=headers, data=payload)
        return self.get_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.get_response(response)

    def put(self, url, headers, payload):
        response = requests.put(url, headers=headers, data=payload)
        return self.get_response(response)
    
    def get_response(self, response):
        status_code = response.status_code
        text = response.text
        try:
            as_json = response.json()
        except Exception:
            as_json = {}

        headers = response.headers

        return Response(status_code, text, as_json, headers)