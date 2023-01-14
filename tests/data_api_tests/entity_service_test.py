from pdb_services.data_api import entity_service


class TestEntityService:
    def test_branched_entity(self):
        entry_id = "4CYG"
        entity_id = "2"
        service = entity_service.BranchedEntityService()
        data = service.search(entry_id, entity_id)
        assert data["rcsb_id"] == "4CYG_2"

    def test_non_polymer_entity(self):
        entry_id = "4G22"
        entity_id = "2"
        service = entity_service.NonPolymerEntityService()
        data = service.search(entry_id, entity_id)
        assert data["rcsb_id"] == "4G22_2"

    def test_polymer_entity(self):
        entry_id = "4G22"
        entity_id = "1"
        service = entity_service.PolymerEntityService()
        data = service.search(entry_id, entity_id)
        assert data["rcsb_id"] == "4G22_1"

    def test_uniprot_entity(self):
        entry_id = "4G22"
        entity_id = "1"
        service = entity_service.UniProtEntityService()
        data = service.search(entry_id, entity_id)
        assert data[0]["rcsb_id"] == "A4ZKE4"
