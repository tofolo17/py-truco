# py-truco

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Primeiros estudos explorando orientação a objetos em Python aplicados ao meu jogo favorito: o truco paulista. Feito em
**maio de 2021**.

Nem todas as [regras do jogo](https://www.jogatina.com/regras-como-jogar-truco.html) foram implementadas, como as rodadas
especiais ou a chamada do TRUCO. No entanto, é possível jogar de forma fluida contra um simples bot, com carta da mesa,
manilha (desempatada pelo naipe) e partidas até 12 pontos.

O objetivo é, em algum dia, transformá-lo em um bot do Discord, com modo singleplayer e multiplayer. Para conseguir isso,
tenho estudado o básico da biblioteca discord.py, como pode-se ver no arquivo [main.py](main.py).

### Estrutura

```
├── singleplayer.py      # partida no terminal: você contra o bot
├── Classes/__init__.py  # Humano, Bot, Rodada e Turno
├── Functions/__init__.py # análise de mão do bot e escolha de carta
└── main.py              # esboço do bot de Discord (cria a "mesa de bar" e o canal de cartas)
```

### Como jogar

```bash
git clone https://github.com/tofolo17/py-truco.git
cd py-truco
python singleplayer.py
```

A cada turno, suas cartas aparecem numeradas: digite o número da carta que quer jogar. O jogo de terminal usa só a
biblioteca padrão do Python.

**Bot de Discord (esboço):** instale `pip install -r requirements.txt` (discord.py 1.7, que roda até o Python 3.9),
defina a variável de ambiente `TRUCO_TOKEN` com o token do seu bot e rode `python main.py`. Comandos: `?truco` e
`?desistir`.

### Licença

[MIT](LICENSE)

---

## What will you find in this repository?

First studies exploring object orientation in Python applied to one of my favorite games: the "truco paulista". Built in
**May 2021**.

Not all [game rules](https://www.jogatina.com/regras-como-jogar-truco.html) have been implemented so far, such as the
special rounds or the TRUCO call. However, it is possible to play fluidly against a simple bot, with the table card, the
"manilha" (ties broken by suit) and matches up to 12 points.

The aim is to, someday, transform this into a Discord bot, with both singleplayer and multiplayer mode. To achieve this,
I have been studying the basics of the discord.py library, as you can see in the [main.py](main.py) file.

### How to play

```bash
git clone https://github.com/tofolo17/py-truco.git
cd py-truco
python singleplayer.py
```

Each turn, your cards are listed with numbers: type the number of the card you want to play. The terminal game only uses
Python's standard library.

**Discord bot (sketch):** run `pip install -r requirements.txt` (discord.py 1.7, which runs up to Python 3.9), set the
`TRUCO_TOKEN` environment variable to your bot's token and run `python main.py`. Commands: `?truco` and `?desistir`.

### License

[MIT](LICENSE)
