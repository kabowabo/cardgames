import random

SUITS = ["Diamond", "Heart", "Spades", "Clubs"]
SUIT_COLORS = {"Diamond": "Red", "Heart": "Red", "Spades": "Black", "Clubs": "Black"}
SPECIALS = ["King", "Queen", "Jack", "Ace"]

def makeDeck():
    cards = []
    for suit in SUITS:
        color = SUIT_COLORS[suit]
        for rank in range(2, 11):
            cards.append([color, suit, rank])
        for special in SPECIALS:
            cards.append([color, suit, special])
    return cards
    
def gameSelect():
    game = int(input("Select a game to play: \n 1.WAR \n"))
    if(game == 1):
        WAR()


def WAR():
    game=True
    computerScore = 0
    userScore = 0
    while game==True:
        user = input("What would you like to do: type 1 to play a new card or type 2 to quit: ")
        if(user=="1" or user==""):
            user = 1
        if(user=="2"):
            user=2
        if user == 1:
            userCard = cards[random.randint(0,51)]
            computerCard = cards[random.randint(0,51)]
            print("Your card is: " , userCard)
            print("Computers card is: ", computerCard) 
            if(userCard[2]==computerCard[2]):
                print("Tie, nobody gets a point")
            if(userCard[2]=='King'):
                userCard[2] = 13
            if(userCard[2]=='Queen'):
                userCard[2] = 12
            if(userCard[2]=='Jack'):
                userCard[2] = 11
            if(computerCard[2]=='King'):
                computerCard[2] = 13
            if(computerCard[2]=='Queen'):
                computerCard[2] = 12
            if(computerCard[2]=='Jack'):
                computerCard[2] = 11
            if(userCard[2]=='Ace'):
                print("User wins round")
                userScore = userScore + 1
            elif(computerCard[2]=='Ace'):
                print("Computer wins round")
                computerScore = computerScore + 1
            elif(userCard[2]>computerCard[2]):
                print("User wins round")
                userScore = userScore + 1
            elif(userCard[2]<computerCard[2]):
                print("Computer wins round")
                computerScore = computerScore + 1
        elif(user == 2):
            game = False
        print("Your score is: ", userScore)
        print("Computer score is: ", computerScore)


    
            
cards = makeDeck()

gameSelect()