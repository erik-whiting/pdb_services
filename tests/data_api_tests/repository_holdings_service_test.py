from pdb_services.data_api import repository_holdings_service


class TestRepositoryHoldingsService:
    def test_current_entries(self):
        service = repository_holdings_service.CurrentEntriesService()
        data = service.search()
        # This endpoint returns a huge array so we're just
        # going to test that there's more than 1,000 results
        assert len(data) > 1000

    def test_removed_entries(self):
        service = repository_holdings_service.RemovedEntriesService()
        data = service.search()
        # This endpoint returns a huge array so we're just
        # going to test that there's more than 1,000 results
        assert len(data) > 1000

    def test_unreleased_entries(self):
        service = repository_holdings_service.UnreleasedEntriesService()
        data = service.search()
        # This endpoint returns a huge array so we're just
        # going to test that there's more than 1,000 results
        assert len(data) > 1000

    def test_entry_status_service(self):
        entry_id = "4HHB"
        service = repository_holdings_service.EntryStatusService()
        data = service.search(entry_id)
        assert data["rcsb_id"] == entry_id

    def test_removed_entry_status_service(self):
        entry_id = "14PS"
        service = repository_holdings_service.RemovedEntryService()
        data = service.search(entry_id)
        assert data["rcsb_id"] == entry_id

    def test_unreleased_status_service(self):
        entry_id = "3A5H"
        service = repository_holdings_service.UnreleasedEntryService()
        data = service.search(entry_id)
        assert data["rcsb_id"] == entry_id

    def test_status_of_multiple_entries(self):
        entry_ids = ["2IM9", "6OIL"]
        service = repository_holdings_service.EntryStatusService()
        data = service.search(entry_ids)
        assert data["rcsb_id"] == ",".join(entry_ids)

    def test_status_of_multiple_unreleased_entries(self):
        # Can't find a combination of IDs that works for this endpoint
        entry_ids = ["3A5H"]
        service = repository_holdings_service.UnreleasedEntryService()
        data = service.search(entry_ids)
        assert data["rcsb_id"] == entry_ids[0]
