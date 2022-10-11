import random
import os
import time
def play_game():
  play = input("Do you want to play blackjack? Type 'y' or 'n'")
    
  card_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
  
  #player card will be stored in player list
  player = [] 
  #computer card will be stored in computer list
  computer = []
  for i in range(1,3):
    card = card_list[random.randint(1,13)-1]
    if card>10:
      player.append(10)
    elif card==1:
      player.append(11)
    else:
      player.append(card)
      
  for i in range(1,3):
    card = card_list[random.randint(1,13)-1]
    if card>10:
      computer.append(10)
    elif card==1:
      computer.append(11)  
    else:
      computer.append(card)
  
  def start():
    #should choose will be true until player does not want to fetch 
    #another card
    should_choose = True
    print(f"Your cards: {player}") 
    print(f"Computer's first card: {computer[0]}")
  
    while should_choose :
    
      want_card = input('type y to get new card or n to pass ')
      if want_card == 'y':
        new_card = card_list[random.randint(1,13)-1]
        if new_card >10:
          player.append(10)
          #if new_card is 1 then check for the sum of all cards
        elif new_card==1:
          if sum(player)<=10:
            #if sum <10 then ace value is 11
            player.append(11)
          else:
            #otherwise ace value is 1
            player.append(1)
        else:
          #if new_card is between 2 and 10 then append as it is
          player.append(new_card)
        print(f"Your cards: {player}") 
        if sum(player)>21:
          #if sum is >21 the break out of the while loop
          break
      else:
        #if player does not want to choose new card then execute below
        should_choose=False
        print(f'Your final hand: {player}')
        #below function will check for the computer card sum 
        # if it is <17 the will add new card
        def computer_hand():
          if sum(computer)<17:
            computer_new_card = card_list[random.randint(1,13)-1]
            if computer_new_card ==1:
              if sum(computer)<=10:
                computer.append(11)
              else:
                computer.append(1)
            elif computer_new_card >10:
              computer.append(10)
            else:
              computer.append(computer_new_card)
            computer_hand()
          else:
            print(f"Computer's final hand: {computer}")
        computer_hand()    
    if sum(computer)<sum(player)<=21:
      print('You win')
  
    elif sum(player)<sum(computer)<=21:
      print('Computer win')
    elif sum(player)==sum(computer):
      print("it's a draw")
    elif sum(player)>21 and sum(computer) >21:
      print('it is a draw')
    elif sum(player) >21:
      print('you lose')
    elif sum(computer)>21:
      print('computer lose')
  #player choose to play then he needs to type 'y'  
  if play=="y":
    #call start function which is inside our main play_game() function
    start()
    #wait 5 second before clearing console.
    time.sleep(5)
    os.system('clear')
    #once it is clear then we can call play_game function 
    play_game()
  else:
    play_game()
    
play_game()  
  
