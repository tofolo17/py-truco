"""Esboço do bot de Discord do PyTruco (cria a "mesa" e o canal de cartas).

O token vem da variável de ambiente TRUCO_TOKEN.
"""

import asyncio
import os

import discord
from discord import PermissionOverwrite
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='?')


# Events
@client.event
async def on_ready():
    status_list = [
        'o zap na testa do bêbado',
        'truco consigo mesmo',
        'a mesa do bar pela janela',
        'um 4 depois de ter pedido 12',
    ]
    cont = 0
    while True:
        status = status_list[cont]
        await client.change_presence(
            status=discord.Status.online, activity=discord.Game(status)
        )
        await asyncio.sleep(30)
        if cont < len(status_list) - 1:
            cont += 1
        else:
            cont = 0


@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Cheguei rapaziada!')
        break


@client.event
async def on_guild_channel_create(channel):
    await channel.send('Bora!')


# Async functions
async def create_secret_channel(guild, category, member, channel_name):
    overwrites = {
        guild.default_role: PermissionOverwrite(read_messages=False),
        get(guild.roles, name="Admin"): PermissionOverwrite(
            read_messages=True
        ),
        member: PermissionOverwrite(read_messages=True),
    }
    new_channel = await guild.create_text_channel(
        name=channel_name, category=category, overwrites=overwrites
    )
    return new_channel


# Commands
@client.command()
async def truco(ctx):
    guild = ctx.guild
    member = ctx.author
    category = (
        get(guild.categories, name="Mesa de bar")
        if get(guild.categories, name="Mesa de bar") is not None
        else await guild.create_category("Mesa de bar")
    )
    secret_channel_name = f"cartas-do-{member.name}{member.discriminator}"
    if get(guild.text_channels, name=secret_channel_name) is None:
        await ctx.send(
            'Acha que ganha de mim? Não fode. '
            'Entre no canal de texto com seu nome, zé.'
        )
        await create_secret_channel(
            guild, category, member, secret_channel_name
        )
    else:
        await ctx.send(
            "Suas cartas já foram entregues! "
            "Verifique a existência do canal de texto com seu nome!"
        )


@client.command()
async def desistir(ctx):
    member = ctx.author
    channel = ctx.channel
    category = channel.category
    channels = category.channels
    if member.discriminator in channel.name:
        if len(channels) == 1:
            await category.delete()
        await channel.delete()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Não sei o que fazer com isso, parça.')


client.run(os.environ.get("TRUCO_TOKEN"))
