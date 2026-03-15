from gomoku import Gomoku
from colorama import Style,init,Fore
import json

init()

def load_game(data):
    try:
        with open("save_game.json","r")as f:
            return json.load(f)
    
    except FileNotFoundError:
        with open("save_game.json","w") as f:
            json.dump(data,f,indent=4)
            return data

def save_game(name,board,current_player):
    data={
        "name": name,
        "board": board, 
        "current_player": current_player
    }
    with open("save_game.json","w")as f:
        json.dump(data,f,indent=4,)



def start_game():
    game= Gomoku()
    game.inicializa_tabuleiro()

    current_player= 1
    while game.ha_jogadas_possiveis() and not game.terminou():
        print("\n"*7)
        game.mostra_tabuleiro()

        if current_player ==1:
            #Add exit validation
            result=game.joga_humano(current_player)
            if result == "exit":
                
                name=input("Write your name: ")
                board= game.tabuleiro
                current_p= game.player_symbol(current_player)

                save_game(name,board,current_p)
                print("Your game was saved")
                break

        else:
            game.joga_computador(current_player)
        current_player = 1-current_player
    
    game.mostra_tabuleiro()
    if game.terminou():
        print(f"{Fore.LIGHTGREEN_EX}Winner")
    else:
        print(f"{Fore.MAGENTA}Draw")

def show_menu():
    while True:
        print(f"\n{Fore.LIGHTWHITE_EX}---GOMOKU---")
        print(f"{Fore.LIGHTWHITE_EX}1) Start Game")
        print(f"{Fore.LIGHTWHITE_EX}2) Exit")

        option= input(f"Choose an option: {Style.RESET_ALL}")
        if option== "1":
            start_game()
        elif option== "2":
            print(f"{Fore.LIGHTGREEN_EX}Bye")
            break
        else:
            print(f"{Fore.RED}Invalid option")

show_menu()