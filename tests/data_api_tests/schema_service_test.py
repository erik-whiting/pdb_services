from pdb_services.data_api import schema_service


class TestSchemaServices:
    def test_assembly_schema_service(self):
        service = schema_service.AssemblySchemaService()
        data = service.search()
        assert data["title"] == "Core Assembly"

    def test_branched_entity_instance_schema_service(self):
        service = schema_service.BranchedEntityInstance()
        data = service.search()
        assert data["title"] == "Core Branched Entity Instance"

    def test_branched_entity_schema_service(self):
        service = schema_service.BranchedEntityService()
        data = service.search()
        assert data["title"] == "Core Branched Entity"

    def test_chemical_component_schema_service(self):
        service = schema_service.ChemicalComponentService()
        data = service.search()
        assert data["title"] == "schema: bird_chem_comp_core collection: bird_chem_comp_core version: 7.1.2"

    def test_drugbank_schema_service(self):
        service = schema_service.DrugBankSchemaService()
        data = service.search()
        assert data["title"] == "schema: drugbank_core collection: drugbank_core version: 1.3.1"

    def test_entry_schema_service(self):
        service = schema_service.EntrySchemaService()
        data = service.search()
        assert data["title"] == "Core Entry"

    def test_nonpolymer_entity_instance_schema_service(self):
        service = schema_service.NonPolymerEntityInstanceSchemaService()
        data = service.search()
        assert data["title"] == "Core Nonpolymer Entity Instance"

    def test_nonpolymer_entity_schema_service(self):
        service = schema_service.NonPolymerEntitySchemaService()
        data = service.search()
        assert data["title"] == "Core Nonpolymer Entity"

    def test_polymer_entity_instance_schema_service(self):
        service = schema_service.PolymerEntityInstanceSchemaService()
        data = service.search()
        assert data["title"] == "Core Polymer Entity"

    def test_polymer_entity_schema_service(self):
        service = schema_service.PolymerEntitySchemaService()
        data = service.search()
        assert data["title"] == "Core Polymer Entity"

    def test_pubmed_schema_service(self):
        service = schema_service.PubMedSchemaService()
        data = service.search()
        assert data["title"] == "Core PubMed"

    def test_uniprot_schema_service(self):
        service = schema_service.UniProt()
        data = service.search()
        assert data["title"] == "Core UniProt"
