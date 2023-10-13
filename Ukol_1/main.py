from sachovnice import Sachovnice


sachovnice = Sachovnice()

if __name__ == "__main__":
    while True:
        sachovnice.vykresli_sachovnici()
        sachovnice.jezdec.vypis_validni_tahy()
        sachovnice.jezdec.pohyb(int(input("")))
