import json 
import os

def createCard(image: str, name: str):
     card = {
          "image": image,
          "name": name
     } 
     return card

def main(): 
    cards = [
        createCard('resized-images/chopper.jpg', 'cardOne'),
        createCard('resized-images/download.jpg', 'cardTwo'),
        createCard('resized-images/Duke_Dennis.jpg', 'cardThree'),
        createCard('resized-images/IMG_0399.jpg', 'cardFour'),
        createCard('resized-images/IMG_9253.jpg', 'cardFive'),
        createCard('resized-images/IMG_9346.jpg', 'cardSix'),
        createCard('resized-images/Lebron_Sunshine.jpg', 'cardSeven'),
        createCard('resized-images/Luffy.jpg', 'cardEight'),
        createCard('resized-images/shooters_gonna_shoot.jpg', 'cardNine'),
        createCard('resized-images/Sigma_Man.jpg', 'cardTen') 
    ] 

    with open("data.json", "w") as f: 
         json.dump(cards, f, indent=2)

if __name__ == "__main__":
     main()