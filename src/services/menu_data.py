import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Dish = set()
        with open(source_path) as file:
            reader = list(csv.reader(file))
            for row in reader[1:]:
                dish = Dish(row[0], float(row[1]))
                ingredient = row[2]
                amount = int(row[3])
                self.dishes.add(dish)
                for d in self.dishes:
                    if dish == d:
                        d.add_ingredient_dependency(
                            Ingredient(ingredient), amount
                        )
