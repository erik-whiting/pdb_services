from pdb_services.data_api import entity_instance_service


class TestEntityInstanceService:
    def test_branched_entity(self):
        entry_id = "1US2"
        asym_id = "C"
        service = entity_instance_service.BranchedEntityInstanceService()
        data = service.search(entry_id, asym_id)
        assert data["rcsb_id"] == "1US2.C"

    def test_non_polymer_entity(self):
        entry_id = "2FBW"
        asym_id = "J"
        service = entity_instance_service.NonPolymerEntityInstanceService()
        data = service.search(entry_id, asym_id)
        assert data["rcsb_id"] == "2FBW.J"

    def test_polymer_entity(self):
        entry_id = "2FBW"
        asym_id = "E"
        service = entity_instance_service.PolymerEntityInstanceService()
        data = service.search(entry_id, asym_id)
        assert data["rcsb_id"] == "2FBW.E"
