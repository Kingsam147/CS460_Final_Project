# Card Memorization Game 
![image](https://github.com/user-attachments/assets/77832da2-39ab-4bf2-8f95-2baafa15ace6)

# Description 
Project is a memorization card-flipping game. The point of the game is to flip a card and find its match hidden in the layout of cards. Once you click a card it will flip over and after flipping another card the game will check to see if those cards match, if they do then the cards will remain flipped for the remainder of the game, if they don't then both cards will flip back down and you can try again. The goal is to match all the cards and have them all flipped up.

To make it feel more like a game I added a clock at the top of the screen that tracks how long the user takes to flip all the cards over, in addition to a counter at the bottom 
which tracks how many times the user failed to match a card. The game uses these two variables to calculate a score that is displayed if the user manages to flip all the cards. To make it more competitive, I added an API that allows the game to track the top 5 highest scores that have been received on that device, which is also displayed at the end if all the cards are flipped. You can also input a username of your choice at the top of the screen which will be displayed alongside your highscore at the end (if you got a highscore). 

![image](https://github.com/user-attachments/assets/9a63dbc2-0b25-403d-a6d4-068a705dd7db)


To start the game the user simply enters a username of their choice (if none is selected it defaults to "username"), then clicks on the start button at the top. 
If the user wants to restart at any point they can click the reset button at the bottom which will shuffle the card locations and 
restart the timer and attempt counter, allowing the user to start the game again from scratch. 

# My Files 
The project consist of 5 files: createCards.py, cards.json(), index.html, index.css, and index.js

## CreateCards.py 
python file that creates the cards. Uses images saved on my laptop to create 9 different cards 
and creates another file named “cards.json” to store them. The reason that I created a whole 
other program to create the json file is because it makes the project so much more flexible. This
lets me change the cards very easily, if I wanted to increase or decrease the number of cards or 
even change the images on the cards I could just make some small alterations to 
createCards.py without changing the game or the json file itself 

## Cards.json 
created by createCards.py, json file containing the cards. Is just an array that holds the image and name of each card as its indices. 

## Index.html 
Pretty basic for the most part it just imports the .css and .js files, however it also initializes some important variables and makes some function calls that will be referenced later in the .css and .js files.  

## Index.css 
Pretty standard styling, but there are a couple of things worth noting. For starters as previously mentioned, the modal that appears when all the cards are flipped is invisible most of the time. I placed it in the grid-container class and put its z-index high so that it overpowers the cards and can be seen on top of them after the modal becomes visible. I also gave it set coordinates and had its position set to absolute so that it could appear in the middle. On the flip side we put the z-index of the grid-container to 1 

## Index.js 
The bulk of the project uses a variety of functions and global variables to flip the cards when they’re clicked on, check the card pairs to see if they match, and display a “you-win” screen along with the scores when the game is finished.

### Global Variables 
gridContainer: the layout for the cards referenced in the html file 

cards: cards imported from the cards.json file 

lockBoard: whether the user can interact with the cards 

score: tracks the score of the user 

topScores: the top 5 scores received on that device

attempts: tracks the number of times the user failed to match a card 

time: tracks the total amount of time in seconds that the user has spent on a round 

minutesElement: the minute variable referenced in .html file 

secondsElement: the second variable referenced in .html file 

username: the username variable referenced in .html file 

### Notable Functions 
startTimer(): resets the time to 0 and clears the timer if it’s already running. Then updates the clock every second

updateTimeDisplay(): converts the total number of seconds (time variable) to an easy to read display of minutes and seconds. Then updates the clock variable in .html file 

shuffleCards(): randomizes the location of all the cards on the board

generateCards(): takes the data from the .json file and generates the cards in the .html file, while also giving them the desired properties 

flipCard(): Does a couple of things: firstly it locks the board, so that the user can’t interact with other cards while this is happening, then it checks if the first card flipped matches the second card if it doesn’t then it adds to the number of failed attempts. Then if the user has won it calculates a score and updates the top 5 scores if needed. Then after everything it uses an API to save the top 5 scores into a local storage to be retrieved in between uses. Then displays the top scores along with the current score for the user to see.

checkForMatch(): checks to see if first card is the same as the second card, if they’re the same then it keeps the cards face up, otherwise it flips both cards back down

disableCards(): keeps the cards face up and disallows the user from interacting with them 

restart(): resets the score, attempts, timer, removes the you-win screen, and reshuffles the cards ;creating a new round

startGame(): starts the game by starting the timer, unlocking the board and saving whatever the username the user put in (defaults to “username” if none)  

# Acessing the Game 
The game is quite simple making it very easy to access. The whole game is available via the github pages. The scores are still saved in between uses even when the game is accessed through github pages. 

# Future Plans 
There are a couple of ideas that I had to improve the game. For starters I was thinking of adding different game modes and/or difficulties. I could add an easy mode which would show all the card locations at the beggining before having the user match them; or even a hard mode which would double the amount of cards that the user has to match.  

The reason that I loved this project idea so much, was for its simplicity along with its flexibilty. As I previously mentioned, I could use the game to study by replacing the goofy/weird images that I had on the cards with study material. I could even change it so that the images were vocab words that matched to their definitions. Honestly there's a lot of different directions that I could go with this project and I'm excited to play around with some different ideas. 

# Test Video 
