import requests


# These endpoints are slightly different than
# the others, so we aren't importing `ServiceModel`


class SchemaServices:
    pdb_base_url = "https://data.rcsb.org/rest/v1/schema"

    def __init__(self, model_name):
        self.base_url = f"{self.pdb_base_url}/{model_name}"

    def search(self):
        return self._make_api_request()

    def _make_api_request(self):
        r = requests.get(self.base_url)
        if r.status_code == 200:
            return r.json()
        else:
            return {"status_code": r.status_code, "content": str(r.content)}


class AssemblySchemaService(SchemaServices):
    def __init__(self):
        super().__init__("assembly")


class BranchedEntityInstance(SchemaServices):
    def __init__(self):
        super().__init__("branched_entity_instance")


class BranchedEntityService(SchemaServices):
    def __init__(self):
        super().__init__("branched_entity")


class ChemicalComponentService(SchemaServices):
    def __init__(self):
        super().__init__("chem_comp")


class DrugBankSchemaService(SchemaServices):
    def __init__(self):
        super().__init__("drugbank")


class EntrySchemaService(SchemaServices):
    def __init__(self):
        super().__init__("entry")


class NonPolymerEntityInstanceSchemaService(SchemaServices):
    def __init__(self):
        super().__init__("nonpolymer_entity_instance")


class NonPolymerEntitySchemaService(SchemaServices):
    def __init__(self):
        super().__init__("nonpolymer_entity")


class PolymerEntityInstanceSchemaService(SchemaServices):
    def __init__(self):
        super().__init__("polymer_entity")


class PolymerEntitySchemaService(SchemaServices):
    def __init__(self):
        super().__init__("polymer_entity")


class PubMedSchemaService(SchemaServices):
    def __init__(self):
        super().__init__("pubmed")


class UniProt(SchemaServices):
    def __init__(self):
        super().__init__("uniprot")
