'''This program will allow the user to play the war card game
     '''
import random

#create empty list
cardDeck = []

#create nested loop for deck of cards with value of
# cards outside and suits on the inside
cardValues = [*range(1,14)]
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

#for loop to add J,Q,K,A
for card in cardValues:
    if card == 1:
        card = "Ace"
    elif card == 11:
        card = "Jack"
    elif card == 12:
        card = "Queen"
    elif card == 13:
        card = "King"
    for suit in suits:
        cardDeck.append((card, suit))

#shuffle deck
random.shuffle(cardDeck)

#deal out cards to each player
player1 = cardDeck[0:int(len(cardDeck)/2)]
player2 = cardDeck[int(len(cardDeck)/2):len(cardDeck)]

#keep track of scores
p1Score = 0
p2Score = 0

#start game with event loop
print("Ready to play War?")

playGame = input("Type start to play game: ").lower()
#print("Type quit to stop playing")

#while loop
while playGame != "quit":
    if playGame != "quit":
        p1Cards = player1.pop(0)
        print("Player 1:", p1Cards)
        p2Cards = player2.pop(0)
        print("Player 2:", p2Cards)
        p1Cards = list(p1Cards)
        p2Cards = list(p2Cards)
        #change values back
        for i in p1Cards or p2Cards:
            if p1Cards[0] == "Jack":
                p1Cards[0]= 11
            elif p2Cards[0] == "Jack":
                p2Cards[0] = 11
            elif p1Cards[0] == "Queen":
                p1Cards[0] = 12
            elif p2Cards[0] == "Queen":
                p2Cards[0] = 12
            elif p1Cards[0] == "King":
                p1Cards[0] = 13
            elif p2Cards[0] == "King":
                p2Cards[0] = 13
            elif p1Cards[0] == "Ace":
                p1Cards[0] = 1
            elif p2Cards[0] == "Ace":
                p2Cards[0] = 1
            else:
                continue
        
        #who wins each round
        if p1Cards > p2Cards:
            print("Player 1 wins")
            player1.append(p1Cards)
            player1.append(p2Cards)
            p1Score += 2
        elif p2Cards > p1Cards:
            print("Player 2 wins")
            player2.append(p2Cards)
            player2.append(p1Cards)
            p2Score += 2
        elif p1Cards == p2Cards:
            print("Tie")
        playGame = input("Type quit to stop playing \n>").lower()
    
    if playGame == "quit":
        p1Score = p1Cards.count(player1)
        p2Score = p2Cards.count(player2)
        if p1Score == p2Score:
            print("Tie")
        elif p1Score > p2Score:
            print("Player 1 wins")
        elif p1Score < p2Score:
            print("Player 2 wins")
        else:
            break