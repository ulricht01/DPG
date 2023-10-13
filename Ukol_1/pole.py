class Pole:
    def __init__(self, cislo_pole, barva, zasobnik = None):
        self.cislo_pole = cislo_pole
        self.barva = barva
        self.zasobnik = zasobnik if zasobnik is not None else []