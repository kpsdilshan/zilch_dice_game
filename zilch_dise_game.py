
import random

class contestant:  
    def __init__(self, name, score):  
        self.name = name  
        self.score = score 

players = []

def welcome():
    print("\nwelcome to the game ")
    print("\nMin 2 players and max 4 players")
    player_count = input("How may palyers are there: ")
    
    if(int(player_count)<2 or int(player_count)>4):
        welcome()    
        
    for i in range(int(player_count)):
        player_name = input("Enter the player's name: ")
        players.append(contestant(player_name,0))    

    for obj in players:
        print(obj.name, obj.score, sep=' ')

    print("\n")


def game():
    for player in players:
        name = player.name
        score =  player.score
        dices =6
        
        while dices>0:
            current_turn = []

            for i in range(dices):
                current_turn.append(random.randint(1,6))

            print(current_turn)

            dices_before_scoring = len(current_turn)
            #scoring
            for i in range(6):
                if(current_turn.count(i)==3):
                    if(i==1):
                        score += 1000
                    else:
                        score += i*100
                    current_turn.remove(i)
                    current_turn.remove(i)
                    current_turn.remove(i)
                
                    
            print(current_turn)
            while (current_turn.count(1)>0):
                score += 100
                current_turn.remove(1)
                
            while (current_turn.count(5)>0):
                score += 50
                current_turn.remove(5)
                    
            print("after scoring",current_turn)
            print(score)
            print("round is over")
            dices_after_scoring = len(current_turn)

            #update the current number of dices
            dices = dices_after_scoring
            
            if(dices_after_scoring ==0):
                #the player have scored from all the 6 dices
                #so that he is given another chance.
                dices =6;
            elif (dices_before_scoring == dices_after_scoring):
                #the player didn't score in this turn so his chance is over.
                print("The player\'s chance is over his final score is ",score )
                player.score = score
                break
            
            
            
def select_the_winner():
    winner = contestant("",0)

    for player in players:
        print(player.name," ",player.score)
    
    for player in players:
        if(winner.score<player.score):
            winner.name = player.name
            winner.score =  player.score
    print("\n\n")
    print("<<<<< ",winner.name, " is the winner >>>>>")
    print("<<<<< The winner\'s score is ",winner.score,">>>>>")

    
answer = "y"
while(answer=="y"):
   players = [] 
   welcome()
   game()
   select_the_winner()

   answer =  input("\nAre you want to play again (y/n): ")


    
    
                
                


            
        
