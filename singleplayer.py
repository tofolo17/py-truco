from Classes import *

pontos_bot = pontos_humano = 0
situacao = "Humano começa"
while pontos_humano < 12 and pontos_bot < 12:  # Loop do jogo
    rodada = Rodada(situacao)
    print(f"Nova rodada {[pontos_humano, pontos_bot]}.")

    rodada.virar_cartas()

    humano = Humano(cartas=rodada.entregar_cartas())
    bot = Bot(cartas=rodada.entregar_cartas())

    turno = Turno(rodada, humano, bot)
    while True:  # Loop da rodada
        print(f"Novo turno: {turno.placar}.")
        turno.mostra_cartas()  # Mostra as cartas do jogador
        turno.confronto()  # Recebe as cartas dos participantes
        turno.compara()  # Compara as cartas e atualiza o placar
        if sum(turno.placar) >= 2:
            situacao = turno.analisa()  # Retorna quem deve começar a próxima rodada, logo, o vencedor
            if situacao == "Humano começa":
                pontos_humano += 1
            elif situacao == "Bot começa":
                pontos_bot += 1
            break
