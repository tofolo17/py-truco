"""Funções auxiliares do jogo."""


def analise_de_jogo(cartas, rodada, ultima_carta):
    """Pontua a mão do bot contra a carta do humano (2 vence, 1 empata)."""
    poder_bot = 0
    niveis_naipes = rodada.naipes
    niveis_cartas = rodada.cartas
    nivel_humano = niveis_cartas.index(ultima_carta[0])
    nivel_humano_manilha = niveis_naipes.index(ultima_carta[1])
    for carta in cartas:
        nivel_bot = niveis_cartas.index(carta[0])
        nivel_bot_manilha = niveis_naipes.index(carta[1])
        if nivel_bot > nivel_humano or (
            nivel_bot == nivel_humano
            and nivel_bot == 9
            and nivel_bot_manilha > nivel_humano_manilha
        ):
            poder_bot += 2
        elif nivel_bot == nivel_humano:
            poder_bot += 1
    return poder_bot


def escolhe(cartas, escolha):
    """Remove e devolve a carta na posição `escolha`."""
    carta_escolhida = cartas[escolha]
    cartas.remove(carta_escolhida)
    return carta_escolhida
