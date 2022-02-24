import pytest
from classes.elements.operation import Operation

class TestOperation():
    """
        Cette classe est un test unitaire pour la classe Operation modele

        :author: Panda <panda@delmasweb.net>
        :date: 20 Fevrier 2022
        :version: 1.0
    """

    def setup_method(self) -> None:
        self.operation = Operation(
            id=1,
            libelle="Ma nouvelle operation",
            montant=10,
            date=50,
            est_valide=True,
            est_verrouille=True
        )

    def test_id(self) -> None:
        assert self.operation.id == 1
    
    def test_libelle(self) -> None:
        assert self.operation.libelle == "Ma nouvelle operation"

    def test_montant(self) -> None:
        assert self.operation.montant == 10

    def test_date(self) -> None:
        assert self.operation.date == 50

    def test_est_valide(self) -> None:
        assert self.operation.est_valide == True

    def test_est_verrouille(self) -> None:
        assert self.operation.est_verrouille == True
    
    @pytest.mark.parametrize("value", [10, 0, -5])
    def test_est_credit(self, value) -> None:
        self.operation.montant = value
        attendu = (value>=0)
        assert self.operation.est_credit() == attendu

    @pytest.mark.parametrize("date, recursivite", [(0, "w"), (0, "ow"), (0, "m"), (0, "om"), (0, "t"),(0, "s"),(0, "y")])
    def test_parse_nouvelle_date_recursivite(self, date, recursivite) -> None:

        result = Operation.parse_nouvelle_date_recursivite(date, recursivite)

        if(recursivite=="w"):
            assert result == 604800
        elif(recursivite=="ow"):
            assert result == 1209600
        elif(recursivite=="m"):
            assert result == 2678400
        elif(recursivite=="om"):
            assert result == 5097600
        elif(recursivite=="t"):
            assert result == 7776000
        elif(recursivite=="s"):
            assert result == 15638400
        elif(recursivite=="y"):
            assert result == 31536000