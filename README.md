### Card Memorization Game 
![Alt text] (![image](https://github.com/user-attachments/assets/77832da2-39ab-4bf2-8f95-2baafa15ace6)

### Description 
Project is a memorization card-flipping game. The point of the game is to flip a card and find its match hidden 
in the layout of cards. Once you click a card it will flip over and after flipping another card the game will check 
to see if those cards match, if they do then the cards will remain flipped for the remainder of the game, if they don't  
then both cards will flip back down and you can try again. The goal is to match all the cards and have them all flipped up.

To make it feel more like a game I added a clock at the top of the screen that tracks how long the user takes to flip all the cards over, in addition to a counter at the bottom 
which tracks how many times the user failed to match a card. The game uses these two variables to calculate a score that is displayed if the user manages 
to flip all the cards. To make it more competitive, the game tracks the top 5 highest scores that have been received 
on that device, which is also displayed at the end if all the cards are flipped. You can also input a username of your choice at 
the top of the screen which will be displayed alongside your highscore at the end (if you got a highscore). 

To start the game the user simply enters a username of their choice (if none is selected it defaults to "username"), then clicks on the start button at the top. 
If the user wants to restart at any point they can click the reset button at the bottom which will shuffle the card locations and 
restart the timer and attempt counter, allowing the user to start the game again from scratch. 

### My Files 
The project consist of 5 files: createCards.py, cards.json(), index.html, index.css, and index.js

## CreateCards.py 
python file that creates the cards. Uses images saved on my laptop to create 9 different cards 
and creates another file named “cards.json” to store them. The reason that I created a whole 
other program to create the json file is because it makes the project so much more flexible. This
lets me change the cards very easily, if I wanted to increase or decrease the number of cards or 
even change the images on the cards I could just make some small alterations to 
createCards.py without changing the game or the json file itself 
