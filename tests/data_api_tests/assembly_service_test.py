from pdb_services.data_api import assembly_service


class TestAssemblyService:
    assembly_service = assembly_service.AssemblyService()

    def test_initialization(self):
        entry_id = "1EHZ"
        assembly_id = 1
        data = self.assembly_service.search(entry_id, assembly_id)
        assert data["rcsb_id"] == "1EHZ-1"
