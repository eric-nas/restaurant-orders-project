from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente = Ingredient('ovo')
    ingrediente2 = Ingredient('ovo')
    ingrediente3 = Ingredient('salmão"')
    assert ingrediente.name == 'ovo'
    assert ingrediente.__eq__(ingrediente2)
    assert ingrediente.__hash__() == ingrediente2.__hash__()
    assert ingrediente.__hash__() != ingrediente3.__hash__()
    assert ingrediente.__repr__() == "Ingredient('ovo')"
    assert ingrediente.restrictions == {Restriction.ANIMAL_DERIVED}
