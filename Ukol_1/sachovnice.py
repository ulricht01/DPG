from jezdec import Jezdec
from pole import Pole

class Sachovnice:

    def __init__(self):
        self.pole = []

        for i in range(0,63, 2):
            pole = Pole(i, "Cerna")
            self.pole.append(pole)

        for i in range(1,64, 2):
            pole = Pole(i, "Bila")
            self.pole.append(pole)

        self.pole.sort(key=lambda x: x.cislo_pole)
        self.nahod_jezdce()
        
    def vykresli_sachovnici(self):
        for radek in range(8):
            for sloupec in range(8):
                cislo_pole = radek * 8 + sloupec
                pole = self.pole[cislo_pole]
                
                if cislo_pole == self.jezdec.cislo_pole:
                    symbol = "♘ "  # Symbol pro jezdce (kůň)
                else:
                    if (radek + sloupec) % 2 == 0:
                        symbol = "██"  # Černé pole
                    else:
                        symbol = "  "  # Bílé pole
                print(symbol, end="")
            print()
            
    def nahod_jezdce(self):
        self.jezdec = Jezdec(self.pole)  # Pass the 'pole' attribute
        self.pole[20].zasobnik.append(self.jezdec)
        self.jezdec.cislo_pole = 20


