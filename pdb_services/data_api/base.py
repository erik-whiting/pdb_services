import requests


class ServiceModel:
    pdb_base_url = "https://data.rcsb.org/rest/v1/core"
    url_request_string = ""

    def __init__(self, service_name: str):
        self.service_name = service_name
        self.base_url = self.pdb_base_url + "/" + service_name

    def search(self):
        raise NotImplementedError

    def _make_api_request(self):
        r = requests.get(self.url_request_string)
        if r.status_code == 200:
            return r.json()
        else:
            return {"status_code": r.status_code, "content": str(r.content)}
