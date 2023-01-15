from pdb_services.data_api import groups_service


class TestGroupsService:
    def test_entry_group(self):
        group_id = "Q3Y9I6"
        service = groups_service.EntryGroupService()
        data = service.search(group_id)
        # There seems to be a bug in this endpoint on the
        # PDB side because this is returning a 500 error
        assert data["status_code"] == 500

    def test_group_provenance(self):
        group_provenance_id = "provenance_sequence_identity"
        service = groups_service.GroupProvenanceService()
        data = service.search(group_provenance_id)
        assert data["rcsb_id"] == "provenance_sequence_identity"

    def test_polymer_entity_group(self):
        group_id = "Q3Y9I6"
        service = groups_service.PolymerEntityGroupsService()
        data = service.search(group_id)
        assert data["rcsb_id"] == group_id
