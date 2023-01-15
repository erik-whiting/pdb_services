from pdb_services.data_api import chemical_component_service


class TestChemicalComponentService:
    def test_chemical_component_service(self):
        comp_id = "CFF"
        service = chemical_component_service.ChemicalComponentService()
        data = service.search(comp_id)
        assert data["chem_comp"]["name"] == "CAFFEINE"

    def test_drugbank_annotation_service(self):
        comp_id = "CFF"
        service = chemical_component_service.DrugBankAnnotationService()
        data = service.search(comp_id)
        assert data["drugbank_info"]["cas_number"] == "58-08-2"
