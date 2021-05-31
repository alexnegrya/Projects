# В данном случае кортеж дает преимущество защищенности от изменений
names = ("Espresso", "Cappuccino", "Robusta")

def _type_error(arg_name, arg):
    raise TypeError(f'Wrong type of argument \"{arg_name}\": {type(arg)}!')

class CoffeeMachine:
  def __init__(self, brand):
    if type(brand) == str:
        self.brand = brand
    else:
        _type_error('brand', brand)

  def makeCoffee(self, name, ingredients):
    if name in names:
        return _CoffeeDrink(name, ingredients)
    else:
        raise NameError(f"This machine takes only {names[0]}, {names[1]} and {names[2]} types of Coffee!")

class _CoffeeDrink:
    def __init__(self, name, ingredients):
        if type(name) == str:
            self.__name = name
        else:
            _type_error('name', name)
        if type(ingredients) == dict:
            if 'water' in ingredients and 'sugar' in ingredients:
                self.__ingredients = ingredients
            else:
                raise KeyError('You must specify \"water\" and \"sugar\"!')
        else:
            _type_error('ingredients', ingredients)

    def __str__(self):
      return f"\
      {'-' * 5} {self.__name} {'-' * 5}\n\
      - Water: {self.__ingredients['water']}\n\
      - Sugar: {self.__ingredients['sugar']}"