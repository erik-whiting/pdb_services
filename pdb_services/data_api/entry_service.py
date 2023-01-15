from .base import ServiceModel


class EntryService(ServiceModel):
    def __init__(self):
        super().__init__("entry")

    def search(self, entry_id: str):
        self.url_request_string = f"{self.base_url}/{entry_id}"
        return self._make_api_request()

class PubMedService(ServiceModel):
    def __init__(self):
        super().__init__("pubmed")

    def search(self, entry_id: str):
        self.url_request_string = f"{self.base_url}/{entry_id}"
        return self._make_api_request()
