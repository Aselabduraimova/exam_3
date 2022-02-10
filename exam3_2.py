class Lemonade:

    def init(self, ingredient='Обычная'):
        if isinstance(ingredient, str):
            self.ingredient = ingredient

    @property
    def drink_info(self):
        return f'{self.ingredient} газировка'

l1 = Lemonade("Лимонная")
print(l1.drink_info)
l2 = Lemonade()
print(l2.drink_info)