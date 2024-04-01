def calculaPontuacao(jogadas):
    pontuacao = 0
    rodada_atual = 0
    jogadas = list(jogadas)

    for _ in range(1, 11):
        if jogadas[rodada_atual] == 'X':
            pontuacao += 10
            pontuacao += pontuacaoFrame(jogadas, rodada_atual + 1, 2)
            rodada_atual += 2
        elif jogadas[rodada_atual + 1] == '/':
            pontuacao += 10
            pontuacao += pontuacaoFrame(jogadas, rodada_atual + 2, 1)
            rodada_atual += 2
        else:
            soma_par = analisaJogada(jogadas[rodada_atual]) + analisaJogada(jogadas[rodada_atual + 1])
            pontuacao += soma_par
            rodada_atual += 2

    return pontuacao

def analisaJogada(jogada):
    if jogada == '-':
        return 0
    elif jogada == 'X' or jogada == '/':
        return 10
    else:
        return int(jogada)

def pontuacaoFrame(jogadas, inicio, num_jogadas):
    pontuacao_bonus = 0
    for i in range(inicio, inicio + num_jogadas):
        pontuacao_bonus += analisaJogada(jogadas[i])
    return pontuacao_bonus

jogada1 = "8070539/9/X-80513/90-"
jogada2 = "8/90447290X-X-80359/7"
print("Pontuação total:", calculaPontuacao(jogada1))