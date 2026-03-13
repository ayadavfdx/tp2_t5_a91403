# gomoku.py (template)
"""
Template para implementar o jogo Gomoku (Cinco em Linha).
Deve implementar todos os métodos abstratos herdados de Jogo.
"""

from jogo_abs import Jogo
from colorama import Style,Fore,init

class Gomoku(Jogo):
    """
    Classe concreta que herda da classe Jogo e implementa o jogo Gomoku.
    """

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
        if jogador == 1:
            jogador= f"X"
        elif jogador == 0:
            jogador= f"O"
        else:
            return None

        while True:
            try:
                ask_row=int(input("Choose a row (number (0-9)): "))  
                ask_colum=int(input("Choose a colum (number (0-9)): "))
                
                row= ask_row
                colum= ask_colum
                options= ["X","O"]

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
                    self.tabuleiro[row][colum]=jogador
                break
            except ValueError:
                print(f"MUST BE A NUMBER")


    def joga_computador(self, jogador: int) -> None:
        """
        Realiza uma jogada aleatória do computador numa posição livre.
        - Jogador 0 usa 'O', Jogador 1 usa 'X'.
        :param jogador: número do jogador (computador).
        """
        raise NotImplementedError("Implementar este método")

    def ha_jogadas_possiveis(self) -> bool:
        """
        Verifica se ainda há espaços vazios no tabuleiro.
        :return: True se ainda há jogadas possíveis, False caso contrário.
        """
        raise NotImplementedError("Implementar este método")

    def terminou(self) -> bool:
        """
        Verifica se alguém ganhou (5 peças seguidas em qualquer direção:
        horizontal, vertical, diagonal ↘️, diagonal ↗️).
        :return: True se o jogo terminou (alguém ganhou), False caso contrário.
        """
        raise NotImplementedError("Implementar este método")

game = Gomoku()
game.inicializa_tabuleiro()
game.mostra_tabuleiro()
game.joga_humano(0)
game.mostra_tabuleiro()