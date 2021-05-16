from random import randint, choice

from Functions import *


class Humano:
    def __init__(self, cartas: list):
        self.cartas = cartas

    def joga_carta(self):
        escolha = int(input("Sua vez. Qual a sua escolha? "))
        carta = escolhe(self.cartas, escolha)
        print(f"Humano joga {carta}.")
        return carta


class Bot:
    def __init__(self, cartas: list):
        self.cartas = cartas

    def joga_carta(self, rodada, placar: list, ultima_carta: str = None):
        carta = None
        poder_bot = analise_de_jogo(self.cartas, rodada, ultima_carta) if ultima_carta is not None else 0
        if len(self.cartas) == 3:
            if ultima_carta is not None:
                if poder_bot in [0, 1, 5, 6]:
                    carta = escolhe(self.cartas, 0)
                elif (poder_bot in [3, 4]) or (len(self.cartas) == 2 and placar == [1, 0]):
                    carta = escolhe(self.cartas, 1)
                elif poder_bot == 2:
                    carta = escolhe(self.cartas, 2)
            else:
                carta = escolhe(self.cartas, choice([0, 2]))
        else:
            if placar == [0, 1]:
                carta = escolhe(self.cartas, 0)
            else:
                carta = escolhe(self.cartas, 1)
        print(f"Bot joga {carta}")
        return carta


class Rodada:
    def __init__(self, situacao):
        self.cartas_entregues = []
        self.situacao = situacao
        self.naipes = ['Ouros', 'Espadas', 'Copas', 'Paus']
        self.cartas = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']

    def virar_cartas(self):
        # Carta da mesa
        carta_aleatoria = randint(0, 9)
        naipe_aleatorio = randint(0, 3)
        carta_da_mesa = [self.cartas[carta_aleatoria], self.naipes[naipe_aleatorio]]
        print(f'Carta da mesa: {carta_da_mesa}\n')

        # Reorganizando self.cartas
        manilha = self.cartas[carta_aleatoria + 1] if carta_aleatoria != 9 else self.cartas[0]
        self.cartas.append(self.cartas.pop(self.cartas.index(manilha)))

    def entregar_cartas(self):
        cartas_em_numeros = []
        while len(cartas_em_numeros) < 3:
            carta = [randint(0, 9), randint(0, 3)]
            if carta not in self.cartas_entregues:
                self.cartas_entregues.append(carta)
                cartas_em_numeros.append(carta)
        cartas_em_numeros.sort()
        cartas_em_valores = [[self.cartas[c[0]], self.naipes[c[1]]] for c in cartas_em_numeros]
        return cartas_em_valores


class Turno:
    def __init__(self, rodada: Rodada, humano: Humano, bot: Bot):
        # Cartas
        self.carta_humano = None
        self.carta_bot = None

        # Classes
        self.rodada = rodada
        self.humano = humano
        self.bot = bot

        # Fluxo do jogo
        self.placar = [0, 0]
        self.situacao = self.rodada.situacao

    def mostra_cartas(self):
        print("Suas cartas:")
        for pos, val in enumerate(self.humano.cartas):
            print(f"[{pos}] | {val}")

    def confronto(self):
        if self.situacao == "Humano começa" and self.placar in [[0, 0], [1, 0]]:
            self.carta_humano = self.humano.joga_carta()
            self.carta_bot = self.bot.joga_carta(self.rodada, self.placar, self.carta_humano)
        else:
            self.carta_bot = self.bot.joga_carta(self.rodada, self.placar)
            self.carta_humano = self.humano.joga_carta()
        print()

    def compara(self, desempate=False):
        # Cartas
        carta_humano = self.carta_humano if not desempate else self.humano.cartas[-1]
        carta_bot = self.carta_bot if not desempate else self.bot.cartas[-1]
        manilha_humano = self.carta_humano if not desempate else self.humano.cartas[-1]
        manilha_bot = self.carta_bot if not desempate else self.bot.cartas[-1]

        # Níveis
        poder_humano = self.rodada.cartas.index(carta_humano[0])
        poder_bot = self.rodada.cartas.index(carta_bot[0])
        poder_humano_manilha = self.rodada.naipes.index(manilha_humano[1])
        poder_bot_manilha = self.rodada.naipes.index(manilha_bot[1])

        # Comparação
        print(f"{carta_humano} x {carta_bot}")
        if poder_humano > poder_bot or (
                poder_humano == poder_bot and poder_bot == 9 and poder_humano_manilha > poder_bot_manilha
        ):
            print("Humano ganha turno.\n")
            if not desempate:
                self.placar[0] += 1
            else:
                return "Humano começa"
        elif poder_humano == poder_bot:
            print("Turno empatado.\n")
            if not desempate:
                self.placar[0] += 1
                self.placar[1] += 1
            else:
                return "Empate"
        else:
            print("Bot ganha turno.\n")
            if not desempate:
                self.placar[1] += 1
            else:
                return "Bot começa"

        # Removendo
        if desempate:
            self.humano.cartas.pop(-1)
            self.bot.cartas.pop(-1)

    def analisa(self):
        if self.placar[0] == 2:
            return "Humano começa"
        elif self.placar[1] == 2:
            return "Bot começa"
        else:
            s = self.compara(desempate=True)
            if s == "Empate":
                s = self.compara(desempate=True)
            return s
