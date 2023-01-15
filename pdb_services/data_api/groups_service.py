from .base import ServiceModel


class EntryGroupService(ServiceModel):
    def __init__(self):
        super().__init__("entry_groups")

    def search(self, group_id: str):
        self.url_request_string = f"{self.base_url}/{group_id}"
        return self._make_api_request()

class GroupProvenanceService(ServiceModel):
    def __init__(self):
        super().__init__("group_provenance")

    def search(self, group_provenance_id: str):
        self.url_request_string = f"{self.base_url}/{group_provenance_id}"
        return self._make_api_request()

class PolymerEntityGroupsService(ServiceModel):
    def __init__(self):
        super().__init__("polymer_entity_groups")

    def search(self, group_id: str):
        self.url_request_string = f"{self.base_url}/{group_id}"
        return self._make_api_request()
