import velha as jv


def main():

    print("\n                                Bem vindos ao jogo da velha estruturado!\n")
    print("Utilize numeros de 1 ~ 9 para escolher onde jogar:")

    tabuleiro = [' ']*9
    jogadasDisp = list(range(9))

    cpu = jv.escolheAdversario()
    jog1, jog2 = jv.leJogador()
    jv.imprimeTabuleiro(tabuleiro)
    
    jogadores = [jog1, jog2]

    jogadorVez = jv.sorteiaJogador(jogadores)
    while True:
        
        if cpu == 3 and (jog2 == jogadorVez):
            jv.jogadorAI(tabuleiro, jogadasDisp, jogadorVez, jog1, jog2)
        elif cpu == 2 and (jog2 == jogadorVez):
            jv.jogadorCPU(tabuleiro, jogadasDisp, jogadorVez)
        else:
            jv.leJogada(tabuleiro, jogadasDisp, jogadorVez)
        jv.imprimeTabuleiro(tabuleiro)

        if jv.verificaVitoria(tabuleiro):
            print(f"Parabéns {jogadorVez} voce venceu!!!\n")
            break

        if jv.verificaVelha(tabuleiro):
            print("Poxa :( deu velha!!!\n")
            break
            
        if jogadorVez == jog1:
            jogadorVez = jog2
        else:
            jogadorVez = jog1

if __name__ == '__main__':
    main()