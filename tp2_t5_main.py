from gomoku import Gomoku
from colorama import Style,init,Fore
import json

init()

def load_game():
    try:
        with open("save_game.json","r")as f:
            return json.load(f)
    
    except FileNotFoundError:
            return None

def save_game(name,board,current_player):
    data={
        "name": name,
        "board": board, 
        "current_player": current_player
    }
    with open("save_game.json","w")as f:
        json.dump(data,f,indent=4,)

def game(game,name,current_player):

    while game.ha_jogadas_possiveis() and not game.terminou():
        print("\n"*7)
        game.mostra_tabuleiro()

        if current_player ==1:
            
            #Add exit validation
            result=game.joga_humano(current_player)
            if result == "exit":
                
                name=input("Write your name: ")
                board= game.tabuleiro

                save_game(name,board,current_player)
                print(f"{Fore.LIGHTBLUE_EX}Your game was saved")
                return

        else:
            game.joga_computador(current_player)
        current_player = 1-current_player
    
    game.mostra_tabuleiro()
    if game.terminou():
        print(f"{Fore.LIGHTGREEN_EX}Winner")
    else:
        print(f"{Fore.MAGENTA}Draw")

def start_game():
    game= Gomoku()
    game.inicializa_tabuleiro()
    name=input("Write your name: ")
    current_player= 1

    game(game,name,current_player)

def start_loaded_game():
    #Verificate if any session was saved
    data= load_game()
    if data == None:
        print(f"{Fore.RED}No saved game found{Style.RESET_ALL}")
        return
    
    #Initialize game
    game=Gomoku()
    game.tabuleiro= data["board"]
    current_player= data["current_player"]
    name= data["name"]

    
def show_menu():
    while True:
        print(f"\n{Fore.LIGHTWHITE_EX}---GOMOKU---")
        print(f"{Fore.LIGHTWHITE_EX}1) Start Game")
        print(f"{Fore.LIGHTWHITE_EX}2) Load  Game")
        print(f"{Fore.LIGHTWHITE_EX}3) Exit")

        option= input(f"Choose an option: {Style.RESET_ALL}")
        if option== "1":
            start_game()
        if option== "2":
            #add function
            pass
        elif option== "3":
            print(f"{Fore.LIGHTGREEN_EX}Bye")
            break
        else:
            print(f"{Fore.RED}Invalid option")

show_menu()