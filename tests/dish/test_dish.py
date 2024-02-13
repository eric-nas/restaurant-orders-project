from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    prato1 = Dish('Hambúrguer', 4)
    prato2 = Dish('Hambúrguer', 4)
    prato3 = Dish('Pizza', 2)
    prato1.add_ingredient_dependency(Ingredient('farinha'), 2)
    assert prato1.recipe == {Ingredient('farinha'): 2}
    assert prato1.get_ingredients() == {Ingredient('farinha')}
    assert prato1.get_restrictions() == {Restriction.GLUTEN}
    assert prato1.name == 'Hambúrguer'
    assert prato1.__eq__(prato2)
    assert prato1.__hash__() == prato2.__hash__()
    assert prato1.__hash__() != prato3.__hash__()
    assert prato1.__repr__() == "Dish('Hambúrguer', R$4.00)"
    with pytest.raises(TypeError):
        Dish('Pizza', '2')
    with pytest.raises(ValueError):
        Dish('Pizza', -2)
