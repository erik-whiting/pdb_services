import pytest


from pdb_services.data_api import base


class TestServiceModel:
    service_model = base.ServiceModel("test_service")

    def test_initialization(self):
        assert self.service_model.service_name == "test_service"
        assert (
            self.service_model.base_url
            == "https://data.rcsb.org/rest/v1/core/test_service"
        )

    def test_search(self):
        with pytest.raises(NotImplementedError):
            self.service_model.search()
