

class Jezdec:
    def __init__(self, pole):
        self.pole = pole

    def pohyb(self, cil):
        if self.is_valid_move(cil):
            # Remove the knight from the current position
            self.pole[self.cislo_pole].zasobnik.remove(self)

            # Move the knight to the target position
            self.cislo_pole = cil
            self.pole[cil].zasobnik.append(self)

            print(f"Pohyb jezdce na pole {cil}")
        else:
            print("Neplatný pohyb pro jezdce")

    def vypis_validni_tahy(self):
        validni_tahy = []

        for cil in range(64):
            if self.is_valid_move(cil):
                validni_tahy.append(cil)

        return print(validni_tahy)

    def is_valid_move(self, cil):

        delta_x = abs(cil % 8 - self.cislo_pole % 8)
        delta_y = abs(cil // 8 - self.cislo_pole // 8)

        return (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)