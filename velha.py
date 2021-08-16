from random import choice
from bisect import insort
from time import sleep

def imprimeTabuleiro(tabuleiro:list[str]) -> None:
    print("\n")
    print(f"  {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("--------------")
    print(f"  {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("--------------")
    print(f"  {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")


def escolheAdversario() -> int:
    while True:
        try:
            cpu = int(input("Gostaria de jogar contra outra pessoa (1) ou CPU (2) ou AI (3)? "))
            if cpu == 1 or cpu == 2 or cpu == 3:
               return cpu
            raise ValueError
        except ValueError:
            print("Escolha inválida!\n")
     

def leJogador() -> tuple[str, str]:  
    jog1 = ''
    while jog1 != 'X' and jog1 != 'O':
        jog1 = input("Escolha X ou O: ").upper()

    if jog1 == 'X':
        jog2 = 'O'
    else:
        jog2 = 'X'
    return jog1, jog2


def escreveJogada(tabuleiro:list[str], pos:int, jogadorVez:str, jogadasDisp:list[str]):
    print(f"{jogadorVez} jogou na posição: {pos+1}")
    tabuleiro[pos] = jogadorVez
    jogadasDisp.remove(pos)



def jogadorCPU(tabuleiro:list[str], jogadasDisp:list[int], jogadorVez:str) -> None:
    pos = choice(jogadasDisp)
    escreveJogada(tabuleiro, pos, jogadorVez, jogadasDisp)
    sleep(1)

    
def jogadorAI(tabuleiro:list[str], jogadasDisp:list[int], jogadorVez:str, jog1:str, jog2:str) -> None:   
    if len(jogadasDisp) == 9:
        jogadorCPU(tabuleiro, jogadasDisp, jogadorVez)
        return

    mPontuacao = -10
    mPos = -1
    for pos in jogadasDisp:    
        tabuleiro[pos] = jogadorVez 
        jogadasDisp.remove(pos)
        if jogadorVez == jog1:
            pontuacao = minMax(tabuleiro, True, jog2, jog1, jog2, jogadasDisp)
        else:
            pontuacao = minMax(tabuleiro, False, jog1, jog1, jog2, jogadasDisp)
        tabuleiro[pos] = ' '
        insort(jogadasDisp, pos)
        
        if pontuacao > mPontuacao:
            mPontuacao = pontuacao
            mPos = pos
    
    escreveJogada(tabuleiro, mPos, jogadorVez, jogadasDisp)
    

    

def minMax(tabuleiro:list[str], isMax:bool, jogadorVez:str, jog1:str, jog2:str, jogadasDisp:list[int]) -> int:
    if verificaVitoria(tabuleiro):
        if jogadorVez == jog1:
            return 1*len(jogadasDisp)+1
        return -1*len(jogadasDisp)-1
    if verificaVelha(tabuleiro):
        return 0

    if isMax:
        mPontuacao = -10
        for pos in jogadasDisp:
            tabuleiro[pos] = jogadorVez 
            jogadasDisp.remove(pos)
            pontuacao = minMax(tabuleiro, False, jog1, jog1, jog2, jogadasDisp)
            tabuleiro[pos] = ' '
            insort(jogadasDisp, pos)
            
            if pontuacao > mPontuacao:
                mPontuacao = pontuacao
    else:
        mPontuacao = 10
        for pos in jogadasDisp:     
            tabuleiro[pos] = jogadorVez 
            jogadasDisp.remove(pos)
            pontuacao = minMax(tabuleiro, True, jog2, jog1, jog2, jogadasDisp)
            tabuleiro[pos] = ' '
            insort(jogadasDisp, pos)
            
            if pontuacao < mPontuacao:
                mPontuacao = pontuacao
    return mPontuacao

def sorteiaJogador(jogadores:list[str]) -> str:   
    return choice(jogadores)


def leJogada(tabuleiro:list[str], jogadasDisp:list[int], jogadorVez:str) -> None: 
    while True:
        try:
            pos = int(input(f"{jogadorVez} escolha onde voce quer jogar: "))-1
            if verificaJogada(jogadasDisp, pos):
                tabuleiro[pos] = jogadorVez
                jogadasDisp.remove(pos)
                return 
            raise ValueError
        except ValueError:
            print("jogada inválida!\n")


def verificaJogada(jogadasDisp:list[int], pos:int) -> bool:
    if pos in jogadasDisp:
        return True
    return False


def verificaVitoria(tabuleiro:list[str]) -> bool:
    if (tabuleiro[0] != ' ') and (tabuleiro[0] == tabuleiro[1]) and (tabuleiro[1] == tabuleiro[2]):
        return True
    if (tabuleiro[3] != ' ') and (tabuleiro[3] == tabuleiro[4]) and (tabuleiro[4] == tabuleiro[5]):
        return True
    if (tabuleiro[6] != ' ') and (tabuleiro[6] == tabuleiro[7]) and (tabuleiro[7] == tabuleiro[8]):
        return True
    if (tabuleiro[0] != ' ') and (tabuleiro[0] == tabuleiro[3]) and (tabuleiro[3] == tabuleiro[6]):
        return True
    if (tabuleiro[1] != ' ') and (tabuleiro[1] == tabuleiro[4]) and (tabuleiro[4] == tabuleiro[7]):
        return True
    if (tabuleiro[2] != ' ') and (tabuleiro[2] == tabuleiro[5]) and (tabuleiro[5] == tabuleiro[8]):
        return True
    if (tabuleiro[0] != ' ') and (tabuleiro[0] == tabuleiro[4]) and (tabuleiro[4] == tabuleiro[8]):
        return True
    if (tabuleiro[2] != ' ') and (tabuleiro[2] == tabuleiro[4]) and (tabuleiro[4] == tabuleiro[6]):
        return True
    return False


def verificaVelha(tabuleiro:list[str]) -> bool:   
    for i in range(9):
        if tabuleiro[i] == ' ':
            return False
    return True
