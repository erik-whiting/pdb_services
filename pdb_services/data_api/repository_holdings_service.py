import requests


# These endpoints are slightly different than
# the others, so we aren't importing `ServiceModel`
class HoldingsServices:
    pdb_base_url = "https://data.rcsb.org/rest/v1/holdings"
    url_request_string = ""

    def __init__(self, holding_type: str):
        self.holding_type = holding_type
        self.base_url = f"{self.pdb_base_url}/{holding_type}"

    def search(self):
        raise NotImplementedError

    def _make_api_request(self):
        r = requests.get(self.url_request_string)
        if r.status_code == 200:
            return r.json()
        else:
            return {"status_code": r.status_code, "content": str(r.content)}


class MultipleIDsServices(HoldingsServices):
    def __init__(self, holding_type):
        super().__init__(holding_type)

    def search(self):
        self.url_request_string = f"{self.base_url}/entry_ids"
        return self._make_api_request()


class CurrentEntriesService(MultipleIDsServices):
    def __init__(self):
        super().__init__("current")


class RemovedEntriesService(MultipleIDsServices):
    def __init__(self):
        super().__init__("removed")


class UnreleasedEntriesService(MultipleIDsServices):
    def __init__(self):
        super().__init__("unreleased")


class StatusService(HoldingsServices):
    def __init__(self, holding_type):
        super().__init__(holding_type)

    def search(self, params):
        search_string = params
        if type(params) == list:
            search_string = ",".join(params)
        self.url_request_string = f"{self.base_url}/{search_string}"
        return self._make_api_request()


class EntryStatusService(StatusService):
    def __init__(self):
        super().__init__("status")


class RemovedEntryService(StatusService):
    def __init__(self):
        super().__init__("removed")

    def search(self, params):
        if type(params) == list:
            # RCSB doesn't provide a service for this
            raise NotImplementedError
        return super().search(params)


class UnreleasedEntryService(StatusService):
    def __init__(self):
        super().__init__("unreleased")
