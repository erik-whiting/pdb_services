from pdb_services.data_api import entry_service


class TestEntryService:
    def test_entry(self):
        entry_id = "1EHZ"
        service = entry_service.EntryService()
        data = service.search(entry_id)
        cell_data = {
            "angle_alpha": 90.0,
            "angle_beta": 90.2,
            "angle_gamma": 90.0,
            "length_a": 54.981,
            "length_b": 33.389,
            "length_c": 61.921,
            "zpdb": 2
        }
        assert data["cell"] == cell_data

    def test_pubmed(self):
        entry_id = "1US2"
        service = entry_service.PubMedService()
        data = service.search(entry_id)
        assert data["rcsb_id"] == "14670951"
