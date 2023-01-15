from .base import ServiceModel


class InterfaceService(ServiceModel):
    def __init__(self):
        super().__init__("interface")

    def search(self, entry_id: str, assembly_id: str, interface_id: str):
        self.url_request_string = f"{self.base_url}/{entry_id}/{assembly_id}/{interface_id}"
        return self._make_api_request()
