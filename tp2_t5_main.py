from gomoku import Gomoku
from colorama import Style,init,Fore

init()

def start_game():
    game= Gomoku()
    game.inicializa_tabuleiro()

    current_player= 1
    while game.ha_jogadas_possiveis() and not game.terminou():
        game.mostra_tabuleiro()

        if current_player ==1:
            game.joga_humano(current_player)
        else:
            game.joga_computador(current_player)

        current_player = 1 - current_player
    
    game.mostra_tabuleiro()
    if game.terminou():
        print("Winner")
    else:
        print("Draw")

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

