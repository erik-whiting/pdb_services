from pdb_services.data_api import interface_service


class TestInterfaceService:
    def test_interface_service(self):
        entry_id = "1RH7"
        assembly_id = "1"
        interface_id = "1"
        service = interface_service.InterfaceService()
        data = service.search(entry_id, assembly_id, interface_id)
        assert data["rcsb_id"] == "1RH7-1.1"
