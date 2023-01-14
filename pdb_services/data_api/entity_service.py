from .base import ServiceModel


class EntityService(ServiceModel):
    def __init__(self, entity_type):
        super().__init__(entity_type)

    def search(self, entry_id: str, entity_id: int):
        self.url_request_string = f"{self.base_url}/{entry_id}/{entity_id}"
        return self._make_api_request()


class BranchedEntityService(EntityService):
    def __init__(self):
        super().__init__("branched_entity")


class NonPolymerEntityService(EntityService):
    def __init__(self):
        super().__init__("nonpolymer_entity")


class PolymerEntityService(EntityService):
    def __init__(self):
        super().__init__("polymer_entity")


class UniProtEntityService(EntityService):
    def __init__(self):
        super().__init__("uniprot")
