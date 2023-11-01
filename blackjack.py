import random 
import os
import scoreBoard
#=========== Variables=========

deck = [                                #Card deck
    2,3,4,5,6,7,8,9,10,'J','Q','K','A',
    2,3,4,5,6,7,8,9,10,'J','Q','K','A',
    2,3,4,5,6,7,8,9,10,'J','Q','K','A',
    2,3,4,5,6,7,8,9,10,'J','Q','K','A',
]

playerHand = [] #Player Deck
dealerHand = []
scoreBoard.loadScores()
scores = scoreBoard.scores
#===========Functions=================
#Deals player/dealer cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#Calculates total value of cards at hand
def total(turn):
    total = 0
    faceCards = ['J','K','Q']
    for card in turn:
        if(card in range(1,11)):
            total+=card 
        elif(card in faceCards):
            total+= 10
        else:
            if total>11:
                total+= 1
            else:
                total+= 11
    return total

#Check for winner
def revealDealerHand():
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0],dealerHand[1]
    
#Main Menu
def mainMenu():
    os.system('cls||clear')
    print("\n--Welcome to the blackjack game!--\n")
    print('''
                               _____
   _____                _____ |6    |
  |2    | _____        |5    || & & | 
  |  &  ||3    | _____ | & & || & & | _____
  |     || & & ||4    ||  &  || & & ||7    |
  |  &  ||     || & & || & & ||____9|| & & | _____
  |____Z||  &  ||     ||____S|       |& & &||8    | _____
         |____E|| & & |              | & & ||& & &||9    |
                |____h|              |____L|| & & ||& & &|
                                            |& & &||& & &|
                                            |____8||& & &|
                                                   |____6|
    ''')
    print('[1] New Game')
    print('[2] Continue Game')
    print('[3] Restart Game')
    print('[4] View Scores')
    print('[5] Exit')
    choice = input('\nEnter your choice: ')
    return choice

#New Game()
def newGame():
    global deck 
    if(len(deck)<10):
        deck = [                                #Card deck
        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
        2,3,4,5,6,7,8,9,10,'J','Q','K','A',
    ]
        
    currentGameScore = 0
    dealerHand.clear()
    playerHand.clear()
    playerIn = True
    dealerIn = True
    for _ in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)
    print(f'\nDealer deals you {dealerHand}')
    print('\nWhat do you do?')
    while playerIn or dealerIn:
        if total(playerHand) > 21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\n You busted! Dealer wins!')
            print(
                '''
                    ░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
                    ░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
                    ░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
                    ░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
                    ░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
                    ░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
                    ░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
                    ░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
                    ░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
                    ░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
                    ░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
                    ░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
                    ░░░░░░░░████████▀████████░░░░░░░░
                    ░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
                    ░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░░░░░░
                '''
            )
            currentGameScore+=10
            break 
        elif total(dealerHand)>21 and total(playerHand)<21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\n Dealer busted! You win!')
            print(
                '''
                    █████████████▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████
                    ████████▀▀░░░░░░░░░░░░░░░░░░░▀▀████████
                    ██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████
                    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████
                    ████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████
                    ████░░▄██████████░░░░░░██▀░░░▀██▄░░████
                    ████░░███████████░░░░░░█▄░░▀░░▄██░░████
                    █████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████
                    ██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████
                    █████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████
                    █████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████
                    ██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀
                    ▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄
                    ▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄
                    ██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████
                    ██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██
                    ███████████░██░▄██▄▄▄▄█▄░▄░████████░███
                '''
            )
            currentGameScore-=10
            break 
        else:     
            if playerIn:
                print('\n[1] Stay')
                print('[2] Hit')
                stayOrHit = input('\nEnter your choice: ')
            if total(dealerHand)>16:
                dealerIn = False 
            if stayOrHit == '1':
                playerIn = False
            else:
                dealCard(playerHand)

        if total(playerHand)== 21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nBlackjack! You win!')
            print(
                '''
                    ░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
                    ░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
                    ░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
                    ░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
                    ░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
                    ░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
                    ░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
                    ░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
                    ░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
                    ░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
                    ░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
                    ░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
                    ░░░░░░░░████████▀████████░░░░░░░░
                    ░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
                    ░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░░░░░░
                '''
            )
            currentGameScore+=21
            break
        elif total(dealerHand) == 21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nBlackjack! Dealer win!')
            print(
                '''
                    █████████████▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████
                    ████████▀▀░░░░░░░░░░░░░░░░░░░▀▀████████
                    ██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████
                    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████
                    ████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████
                    ████░░▄██████████░░░░░░██▀░░░▀██▄░░████
                    ████░░███████████░░░░░░█▄░░▀░░▄██░░████
                    █████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████
                    ██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████
                    █████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████
                    █████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████
                    ██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀
                    ▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄
                    ▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄
                    ██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████
                    ██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██
                    ███████████░██░▄██▄▄▄▄█▄░▄░████████░███
                '''
            )
            currentGameScore-=10
            break
        elif total(playerHand)>21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nYou bust! Dealer wins!')
            print(
                '''
                    █████████████▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████
                    ████████▀▀░░░░░░░░░░░░░░░░░░░▀▀████████
                    ██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████
                    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████
                    ████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████
                    ████░░▄██████████░░░░░░██▀░░░▀██▄░░████
                    ████░░███████████░░░░░░█▄░░▀░░▄██░░████
                    █████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████
                    ██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████
                    █████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████
                    █████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████
                    ██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀
                    ▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄
                    ▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄
                    ██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████
                    ██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██
                    ███████████░██░▄██▄▄▄▄█▄░▄░████████░███
                '''
            )
            currentGameScore-=10
            break
        elif total(dealerHand)>21:
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nDealer bust! You win!')
            print(
                '''
                    ░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
                    ░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
                    ░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
                    ░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
                    ░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
                    ░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
                    ░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
                    ░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
                    ░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
                    ░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
                    ░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
                    ░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
                    ░░░░░░░░████████▀████████░░░░░░░░
                    ░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
                    ░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░░░░░░
                '''
            )
            currentGameScore+=10
            break
        elif 21-total(dealerHand)< 21-total(playerHand):
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nDealer wins')
            print(
                '''
                    █████████████▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████
                    ████████▀▀░░░░░░░░░░░░░░░░░░░▀▀████████
                    ██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████
                    █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████
                    ████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████
                    ████░░▄██████████░░░░░░██▀░░░▀██▄░░████
                    ████░░███████████░░░░░░█▄░░▀░░▄██░░████
                    █████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████
                    ██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████
                    █████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████
                    █████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████
                    ██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀
                    ▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄
                    ▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄
                    ██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████
                    ██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██
                    ███████████░██░▄██▄▄▄▄█▄░▄░████████░███
                '''
            )
            currentGameScore-=10
            break
        elif 21-total(dealerHand)> 21-total(playerHand):
            print(f'\nYou have {playerHand} for a  total of {total(playerHand)} and the dealer has  {dealerHand} for a total of {total(dealerHand)}')
            print('\nYou win')
            print(
                '''
                    ░░░░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░░░░░░
                    ░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░
                    ░░░░░░░░█░░░░░░░░░░▄▄▄░░█░░░░░░░░
                    ░░░░░░░░█░░▄▄▄░░▄░░███░░█░░░░░░░░
                    ░░░░░░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░░░░░░
                    ░░░░░░░░█░░▀█▀█▀█▀█▀█▀░░█░░░░░░░░
                    ░░░░░░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░░░░░░
                    ░░░░░░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░░░░░░
                    ░░░░░▄▀░▄▄▀▄▄▀▀▀▄▀▀▀▄▄▀▄▄░▀▄░░░░░
                    ░░░░░█░░░░▀▄░█▄░░░▄█░▄▀░░░░█░░░░░
                    ░░░░░░▀▄▄░█░░█▄▄▄▄▄█░░█░▄▄▀░░░░░░
                    ░░░░░░░░▀██▄▄███████▄▄██▀░░░░░░░░
                    ░░░░░░░░████████▀████████░░░░░░░░
                    ░░░░░░░▄▄█▀▀▀▀█░░░█▀▀▀▀█▄▄░░░░░░░
                    ░░░░░░░▀▄▄▄▄▄▀▀░░░▀▀▄▄▄▄▄▀░░░░░░░
                '''
            )
            currentGameScore+=10
            break
    return currentGameScore
#Restart Game()
def restartGame():
    scores.clear() 
    
def viewScores(scores): #Function used to view scores
    print('\nHIGH SCORES\n')
    if(len(scores)==0): 
        print('     No one is playing')
    else:
        highScores = sorted(scores.items(), key=lambda x:x[1])
        print('Rank     Name    Score')
        for i in range(len(highScores)):
            print(str(i+1)+'     '+str(highScores[len(highScores)-(i+1)][0])+'     '+str(highScores[len(highScores)-(i+1)][1]))

#==========================================   
#Main Program
while(True):
    choice = mainMenu()
    if(choice=='1'):
        os.system('cls||clear')
        print(
            '''
                                    ██████████████████
                            ░░░░████░░░░░░░░░░░░░░░░░░████
                            ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██
                            ░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██
                            ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
                            ██░░░░░░░░░░░░░░░░░░░░██████░░░░██
                            ██░░░░░░░░░░░░░░░░░░░░██████░░░░██
                            ██░░░░██████░░░░██░░░░██████░░░░██
                            ░░██░░░░░░░░░░██████░░░░░░░░░░██
                            ████░░██░░░░░░░░░░░░░░░░░░██░░████
                            ██░░░░██████████████████████░░░░██
                            ██░░░░░░██░░██░░██░░██░░██░░░░░░██
                            ░░████░░░░██████████████░░░░████
                            ░░░░░░████░░░░░░░░░░░░░░████
                            ░░░░░░░░░░██████████████
            '''
        )
        print("\nHi! I'm Keane and I'll be your dealer today! Who am I playing blackjack with?")
        player = input('\nEnter your name: ')
        if player in scores.keys():
            print('\nPlayer already exists! Do you want to overwrite data?')
            c = input('Overwrite? (Y/N) :')
            if(c.lower()=='y'):
                scores[player] = newGame()
                input('Press anything to continue')
            else:
                scores[player] += newGame()
                again = input('\nPlay again? (Y/N): ')
                while(again.lower()=='y'):    
                    scores[player] += newGame()
                    again = input('\nPlay again? (Y/N): ')
        else:
            scores[player] = newGame()
            again = input('\nPlay again? (Y/N): ')
            while(again.lower()=='y'):    
                scores[player] += newGame()
                again = input('\nPlay again? (Y/N): ')
    elif(choice=='2'):
        print('\nWelcome back to the blackjack game! Who is this returning player?')
        player = input('\nEnter your name: ')
        if(player in scores.keys()):
            scores[player] += newGame()
            again = input('\nPlay again? (Y/N): ')
            while(again.lower()=='y'):    
                scores[player] += newGame()
                again = input('\nPlay again? (Y/N): ')
        else:
            print('\nPlayer does not exist, please enter a returning player:')
            input('Press anything to continue...')
    elif(choice=='3'):
        restartGame()
    elif(choice=='4'):
        os.system('cls||clear')
        viewScores(scores)
        proceed = input('\nPress any key to proceed')
    elif(choice=='5'):
        print('\nGood game!')
        scoreBoard.saveScores(scores)
        break
    else:
        print('\nMake a valid choice!')
        input('Press anything to continue...')


