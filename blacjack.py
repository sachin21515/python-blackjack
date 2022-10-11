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
  def intial_cards(game_players):
    for i in range(1,3):
      card = card_list[random.randint(1,13)-1]
      if card>10:
        game_players.append(10)
      elif card==1:
        game_players.append(11)
      else:
        game_players.append(card)

  intial_cards(player) 
  intial_cards(computer)
  
  def start():
    #should choose will be true until player does not want to fetch 
    #another card
    should_choose = True
    print(f"Your cards: {player}") 
    print(f"Computer's first card: {computer[0]}")
  
    while should_choose :
      def new_card(game_players):
          new_card = card_list[random.randint(1,13)-1]
          if new_card >10:
            game_players.append(10)
          #if new_card is 1 then check for the sum of all cards
          elif new_card==1:
            if sum(game_players)<=10:
            #if sum <10 then ace value is 11
              game_players.append(11)
            else:
            #otherwise ace value is 1
              game_players.append(1)
          else:
          #if new_card is between 2 and 10 then append as it is
            game_players.append(new_card)
  
      want_card = input('type y to get new card or n to pass ')
      if want_card == 'y':

        new_card(player)
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
            new_card(computer)
            
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
  
