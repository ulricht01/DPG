import numpy as np
import cv2 as cv
import numpy.random as rnd

class Bilek:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = np.ones((self.height, self.width, 3), np.uint8) * 255
        self.spots = [] 

    def vytvor_se(self):
        cv.imwrite('obraz.jpg', self.image)

    def vytvor_skvrnu(self):
        for i in range(rnd.randint(5,10)):
            radius = rnd.randint(5, min(self.width, self.height) // 5)
            overlap = True
            while overlap:
                overlap = False
                x = rnd.randint(0, self.width)
                y = rnd.randint(0, self.height)
                for spot in self.spots:
                    distance = np.sqrt((spot[0] - x)**2 + (spot[1] - y)**2)
                    if distance < spot[2] + radius:
                        overlap = True
                        break
            self.spots.append((x, y, radius))
            cv.circle(self.image, (x, y), radius, (rnd.randint(0, 200), rnd.randint(0, 200), rnd.randint(0, 200)), -1)
        
        cv.imwrite('obraz.jpg', self.image)

    def count_spots_in_image(self, image):
        image = cv.imread(image)
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        _, binary_image = cv.threshold(gray_image, 220, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(binary_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        return len(contours)

if __name__ == "__main__":
    try:
        width = int(input("Zadej šířku daného obrázku: "))
        if width > 2000:
            raise Exception("Maximálně 2000!")
        elif width <= 0:
            raise Exception("Minimálně 1!")

        height = int(input("Zadej výšku daného obrázku: "))
        if height > 2000:
            raise Exception("Maximálně 2000!")
        elif height <= 0:
            raise Exception("Minimálně 1!")
            
        bilek = Bilek(width, height)
        bilek.vytvor_se()
        bilek.vytvor_skvrnu()
        print(f"Počet skvrn je dle seznamu: {len(bilek.spots)}")
        print(f"Počet skvrn je dle obrazu: {bilek.count_spots_in_image('obraz.jpg')}")

    except ValueError:
        print("Toto musí být číslo!")
