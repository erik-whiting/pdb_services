from .base import ServiceModel


class AssemblyService(ServiceModel):
    def __init__(self):
        super().__init__("assembly")

    def search(self, entry_id: str, assembly_id: int):
        self.url_request_string = f"{self.base_url}/{entry_id}/{assembly_id}"
        return self._make_api_request()
