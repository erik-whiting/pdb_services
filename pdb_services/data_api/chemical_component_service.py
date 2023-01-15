from .base import ServiceModel


class ChemicalComponentService(ServiceModel):
    def __init__(self):
        super().__init__("chemcomp")

    def search(self, comp_id: str):
        self.url_request_string = f"{self.base_url}/{comp_id}"
        return self._make_api_request()


class DrugBankAnnotationService(ServiceModel):
    def __init__(self):
        super().__init__("drugbank")

    def search(self, comp_id: str):
        self.url_request_string = f"{self.base_url}/{comp_id}"
        return self._make_api_request()
