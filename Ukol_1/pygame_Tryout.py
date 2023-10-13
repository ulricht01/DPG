import pygame
from pygame.locals import *
import sys

class Jezdec:
    def __init__(self, pole):
        self.pole = pole
        self.cislo_pole = 0

    def pohyb(self, cil):
        if self.is_valid_move(cil):
            self.pole[self.cislo_pole].zasobnik.remove(self)
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

        return validni_tahy

    def is_valid_move(self, cil):
        delta_x = abs(cil % 8 - self.cislo_pole % 8)
        delta_y = abs(cil // 8 - self.cislo_pole // 8)

        return (delta_x == 1 and delta_y == 2) or (delta_x == 2 and delta_y == 1)

class Pole:
    def __init__(self, cislo_pole, barva, zasobnik=None):
        self.cislo_pole = cislo_pole
        self.barva = barva
        self.zasobnik = zasobnik if zasobnik is not None else []
        self.mozny_tah = False

class Sachovnice:
    def __init__(self):
        self.pole = []
        self.create_pole()
        self.nahod_jezdce()
        self.validni_tahy = []  # Seznam platných tahů

    def create_pole(self):
        for i in range(64):
            if (i // 8 + i % 8) % 2 == 0:
                barva = "Cerna"
            else:
                barva = "Bila"
            pole = Pole(i, barva)
            self.pole.append(pole)

    def vykresli_sachovnici(self, screen):
        for radek in range(8):
            for sloupec in range(8):
                cislo_pole = radek * 8 + sloupec
                pole = self.pole[cislo_pole]
                x = sloupec * 50
                y = radek * 50

                if cislo_pole != self.jezdec.cislo_pole:
                    if pole.barva == "Cerna":
                        pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))
                    else:
                        pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))

        # Zde zobrazte "X" na polích, kde jezdec může jít
        for radek in range(8):
            for sloupec in range(8):
                cislo_pole = radek * 8 + sloupec
                pole = self.pole[cislo_pole]
                x = sloupec * 50
                y = radek * 50
                if pole.mozny_tah:
                    font = pygame.font.Font(None, 36)
                    text = font.render("X", True, (0, 255, 0))
                    screen.blit(text, (x + 20, y + 10))

        # Zde zobrazte trojúhelník jezdce nad polem s průhledností
        x_jezdce = (self.jezdec.cislo_pole % 8) * 50
        y_jezdce = (self.jezdec.cislo_pole // 8) * 50
        jezdec_surface = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(jezdec_surface, (255, 0, 0, 128), [(25, 0), (0, 50), (50, 50)])  # Průhledný trojúhelník jezdce
        screen.blit(jezdec_surface, (x_jezdce, y_jezdce))

    def nahod_jezdce(self):
        self.jezdec = Jezdec(self.pole)
        self.pole[20].zasobnik.append(self.jezdec)
        self.jezdec.cislo_pole = 20

    def update_validni_tahy(self):
        self.validni_tahy = self.jezdec.vypis_validni_tahy()

        for i in range(64):
            self.pole[i].mozny_tah = False

        for i in self.validni_tahy:
            self.pole[i].mozny_tah = True

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    sachovnice = Sachovnice()

    while True:
        sachovnice.update_validni_tahy()  # Aktualizace platných tahů
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                radek = y // 50
                sloupec = x // 50
                cil = radek * 8 + sloupec

                if sachovnice.jezdec.is_valid_move(cil):
                    sachovnice.jezdec.pohyb(cil)

        screen.fill((255, 255, 255))
        sachovnice.vykresli_sachovnici(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()