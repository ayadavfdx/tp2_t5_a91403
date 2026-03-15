# gomoku.py (template)
"""
Template para implementar o jogo Gomoku (Cinco em Linha).
Deve implementar todos os métodos abstratos herdados de Jogo.
"""

from jogo_abs import Jogo
from colorama import Style,Fore,init
import random

init()

class Gomoku(Jogo):
    """
    Classe concreta que herda da classe Jogo e implementa o jogo Gomoku.
    """
    #Method to validate player
    def player_symbol(self,jogador: int)->str:
        if jogador == 1:
            return f"{Fore.LIGHTCYAN_EX}X{Style.RESET_ALL}"
        elif jogador == 0:
            return f"{Fore.LIGHTYELLOW_EX}O{Style.RESET_ALL}"
        else:
            return (f"{Fore.LIGHTRED_EX}Invalid player number (0-1)")

    def inicializa_tabuleiro(self) -> None:
        """
        Inicializa o tabuleiro 10x10 com espaços vazios ' '.
        """
        self.tabuleiro = [[' ' for _ in range(10)] for _ in range(10)]

    def mostra_tabuleiro(self) -> None:
        """
        Desenha o tabuleiro na consola.
        Dica: Pode usar enumerate() para numerar as linhas.
        """
        #Header
        print("  0 1 2 3 4 5 6 7 8 9")

        for i,row in enumerate(self.tabuleiro):
            print(i,end=" ")

            for col in row:
                if col != " ":
                    print(col, end=" ")
                else:
                    print(".", end=" ")

            print()
    def joga_humano(self, jogador: int) -> None:
        """
        Pede ao jogador humano as coordenadas (linha, coluna) da jogada
        e coloca a peça no tabuleiro.
        - Jogador 0 usa 'O', Jogador 1 usa 'X'.
        - Deve validar se a posição está dentro do tabuleiro e está livre.
        :param jogador: número do jogador (0 ou 1).
        """
        #Player symbol
        p_symbol=self.player_symbol(jogador)
        while True:
            try:
                print("Type ´s´ to leave")
                ask_row=input("Choose a row (number (0-9)/s): ").lower()  
                ask_colum=input("Choose a colum (number (0-9)/s): ").lower()

                #Validation for exit
                if ask_row =="s" or ask_colum == "s":
                    return "exit"

                row= int(ask_row)
                colum= int(ask_colum)
                options= [
                        f"{Fore.LIGHTCYAN_EX}X{Style.RESET_ALL}",
                        f"{Fore.LIGHTCYAN_EX}O{Style.RESET_ALL}"
                        ]
                
                #Validation for range
                if 0>row or row>9:
                    print("Out of range!")
                    continue
                elif 0>colum or colum >9:
                    print("Out of range!")
                    continue

                #Validation for cell occupied
                elif self.tabuleiro[row][colum] in options:
                    print("Occupied")
                    continue
                else:
                    self.tabuleiro[row][colum]=p_symbol
                break
            except ValueError:
                print(f"{Fore.LIGHTRED_EX}MUST BE A NUMBER{Style.RESET_ALL}")


    def joga_computador(self, jogador: int) -> None:
        """
        Realiza uma jogada aleatória do computador numa posição livre.
        - Jogador 0 usa 'O', Jogador 1 usa 'X'.
        :param jogador: número do jogador (computador).
        """
        #Player symbol
        p_symbol=self.player_symbol(jogador)

        #Put random chip
        options= [
                f"{Fore.LIGHTCYAN_EX}X{Style.RESET_ALL}",
                f"{Fore.LIGHTCYAN_EX}O{Style.RESET_ALL}"
                        ]
        occupied= []

        #Choose empty cells
        for a, row in enumerate(self.tabuleiro):
            for b, column in enumerate(row):
                if column in options:
                    occupied.append((a,b))

        #Choose random play
        while True:
            row= random.randint(0,9)
            col= random.randint(0,9)

            if (row,col) not in occupied:
                self.tabuleiro[row][col]= p_symbol
                break
            

    def ha_jogadas_possiveis(self) -> bool:
        """
        Verifica se ainda há espaços vazios no tabuleiro.
        :return: True se ainda há jogadas possíveis, False caso contrário.
        """
        for row in self.tabuleiro:
            for colum in (row):
                if colum == " ":
                    return True
        return False

    def terminou(self) -> bool:
        """
        Verifica se alguém ganhou (5 peças seguidas em qualquer direção:
        horizontal, vertical, diagonal ↘️, diagonal ↗️).
        :return: True se o jogo terminou (alguém ganhou), False caso contrário.
        """
        #Horizontal verification
        for i in range (10):
            counter= 1
            for j in range(1,10):

                current_piece_x= self.tabuleiro[i][j] 
                last_piece_x= self.tabuleiro[i][j-1]

                if current_piece_x != " " and current_piece_x == last_piece_x:
                    counter += 1
                else:
                    counter = 1

                if counter == 5:
                    return True

        #Vertical verification
        for j in range (10):
            counter= 1
            for i in range (1,10):

                current_piece_y= self.tabuleiro[i][j] 
                last_piece_y= self.tabuleiro[i-1][j]

                if current_piece_y != " " and current_piece_y == last_piece_y:
                    counter +=1
                else:
                    counter = 1
                
                if counter == 5:
                    return True
        
        #Diagonal down verification
        for i in range (1,10):
            counter=1
            for j in range (1,10):

                current_p_diagonal_d= self.tabuleiro[i][j]
                last_p_diagonal_d= self.tabuleiro[i-1][j-1]

                if current_p_diagonal_d != " " and current_p_diagonal_d == last_p_diagonal_d:
                    counter += 1
                else:
                    counter= 1
            
                if counter == 5:
                    return True
            
        #Diagoanl up verification
        for i in range(8,-1,-1):
            counter=1
            for j in range(1,10):

                current_p_diagonal_u= self.tabuleiro[i][j]
                last_p_diagonal_u= self.tabuleiro[i+1][j-1]

                if current_p_diagonal_u != " " and current_p_diagonal_u == last_p_diagonal_u:
                    counter +=1
                else:
                    counter= 1
                
                if counter ==5:
                    return True
