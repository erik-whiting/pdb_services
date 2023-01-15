from .base import ServiceModel


class EntityInstanceService(ServiceModel):
    def __init__(self, entity_type):
        super().__init__(entity_type)

    def search(self, entry_id: str, asym_id: str):
        self.url_request_string = f"{self.base_url}/{entry_id}/{asym_id}"
        return self._make_api_request()


class BranchedEntityInstanceService(EntityInstanceService):
    def __init__(self):
        super().__init__("branched_entity_instance")


class NonPolymerEntityInstanceService(EntityInstanceService):
    def __init__(self):
        super().__init__("nonpolymer_entity_instance")


class PolymerEntityInstanceService(EntityInstanceService):
    def __init__(self):
        super().__init__("polymer_entity_instance")
