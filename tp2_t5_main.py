from gomoku import Gomoku
from colorama import Style,init,Fore

init()

def start_game():
    game= Gomoku()
    game.inicializa_tabuleiro()

    current_player= 1
    while game.ha_jogadas_possiveis() and not game.terminou():
        game.mostra_tabuleiro()

        
def show_menu():
    while True:
        print("\n---GOMOKU---")
        print("1) Start Game")
        print("2) Exit")

        option= input("Choose an option: ")
        if option== "1":
            start_game()
        elif option== "2":
            print("Bye")
        else:
            print("Invalid option")

