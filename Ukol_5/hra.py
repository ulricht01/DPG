import pygame
import sys
import math
import random

# Vytvoření třídy hráče
class Hrac:
    # Konstruktor
    def __init__(self, x, y, barva, velikost, rychlost):
        self.x = x
        self.y = y
        self.barva = barva
        self.velikost = velikost
        self.rychlost = rychlost
        self.barva_oci = (54, 113, 232)
        self.barva_pusa = (255, 0, 0)
        self.velikost_oci = 5
        self.velikost_pusi = 10
        self.score = 0
        self.aktivini = True

    # Pohyb hráče
    def pohyb(self, klavesy):
        nova_pozice_x, nova_pozice_y = self.x, self.y

        if klavesy[pygame.K_LSHIFT]:
            self.rychlost = 10
        else:
            self.rychlost = 5

        if klavesy[pygame.K_d]:
            nova_pozice_x += self.rychlost
        if klavesy[pygame.K_a]:
            nova_pozice_x -= self.rychlost
        if klavesy[pygame.K_w]:
            nova_pozice_y -= self.rychlost
        if klavesy[pygame.K_s]:
            nova_pozice_y += self.rychlost

        return nova_pozice_x, nova_pozice_y
    # Vykreslení hráče
    def nakreslit(self, okno):
        pygame.draw.circle(okno, self.barva, (self.x, self.y), self.velikost)
        pygame.draw.circle(okno, self.barva_oci, (self.x - 8, self.y - 8), 5)
        pygame.draw.circle(okno, self.barva_oci, (self.x + 8, self.y - 8), 5)
        pygame.draw.arc(okno, self.barva_pusa, (self.x - 10, self.y, 20, 10), math.pi, 2*math.pi, self.velikost_pusi)
    # Přidání skóre a zvětšení hráče
    def pridej_skore(self):
        self.score += 1
        self.velikost += 10

    # Vracím skóre pro výpis na obrazovce v pozdějším kódu
    def zobraz_skore(self):
        return self.score

# Inicializace Pygame
pygame.init()

# Nastavení okna
width, height = 1280, 1028
okno = pygame.display.set_mode((width, height))
pygame.display.set_caption("Who knows")

# Vytvoření hráče
hrac = Hrac(width // 2, height // 2, (150, 150, 150), 20, 5)

# Definice hran na obrazovce
hrany = [
    ((20, 20), (20, 1000)),
    ((1260, 1000), (20, 1000)),
    ((20, 20), (1260, 20)),
    ((1260, 20), (1260, 1000)),
]

# Vytvoření třídy bodu, který hráč sbírá
class Bod:
    # Konstruktor
    def __init__(self, x, y, barva, velikost):
        self.x = x
        self.y = y
        self.barva = barva
        self.velikost = velikost

    # Vykreslení bodu
    def nakreslit(self, okno):
        pygame.draw.circle(okno, self.barva, (self.x, self.y), self.velikost)

    # Zmizení a objevení se
    def zmiz_a_objev_se(self):
        self.x = random.randint(20 + velikost_bodu, width - velikost_bodu - 20)
        self.y = random.randint(20 + velikost_bodu, height - velikost_bodu - 20)

# Vytvoření bodu
velikost_bodu = 15
bod = Bod(
    random.randint(20 + velikost_bodu, width - velikost_bodu - 20),
    random.randint(20 + velikost_bodu, height - velikost_bodu - 20),
    (255, 232, 54),
    velikost_bodu
)

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Získání stisknutých kláves
    klavesy = pygame.key.get_pressed()

    nova_pozice_x, nova_pozice_y = hrac.pohyb(klavesy)

    # Kontrola kolize s hranami
    if hrac.aktivini:
        koliduje = False
        for hrana in hrany:
            if (
                nova_pozice_x + hrac.velikost > min(hrana[0][0], hrana[1][0])
                and nova_pozice_x - hrac.velikost < max(hrana[0][0], hrana[1][0])
                and nova_pozice_y + hrac.velikost > min(hrana[0][1], hrana[1][1])
                and nova_pozice_y - hrac.velikost < max(hrana[0][1], hrana[1][1])
            ):
                # Koliduje s hranou, takže není povoleno překročit
                koliduje = True
                break

        # Kontrola kolize s bodem
        if (
            nova_pozice_x + hrac.velikost > bod.x - bod.velikost
            and nova_pozice_x - hrac.velikost < bod.x + bod.velikost
            and nova_pozice_y + hrac.velikost > bod.y - bod.velikost
            and nova_pozice_y - hrac.velikost < bod.y + bod.velikost
        ):
            bod.zmiz_a_objev_se()
            hrac.pridej_skore()

        if not koliduje:
            hrac.x, hrac.y = nova_pozice_x, nova_pozice_y

    # Vykreslení černé barvy, hráče a bodu do okna
    okno.fill((0, 0, 0))
    hrac.nakreslit(okno)
    bod.nakreslit(okno)

    # Vykreslení hran
    for hrana in hrany:
        pygame.draw.line(okno, (255, 255, 255), hrana[0], hrana[1], 5)
    
    # Výýpis skóre na obrazovku
    font = pygame.font.Font(None, 36)
    text = font.render(f"Skóre: {hrac.score} / 10", True, (255, 255, 255))
    okno.blit(text, (width - text.get_width() - 20, 20))

    # Cíl hry
    if hrac.score == 10:
        gratulace_text = font.render("Gratuluji k dohrání!", True, (255, 255, 255))
        gratulace_rect = gratulace_text.get_rect(center=(width // 2, height // 2 - 50))
        okno.blit(gratulace_text, gratulace_rect)
        hrac.aktivini = False
        if klavesy[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    pygame.time.Clock().tick(30)
