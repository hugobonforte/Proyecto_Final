import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")


ECOFACTOS = [
    "La última década (2014-2023) fue la más cálida jamás registrada desde que existen mediciones globales en 1850.",
    "Los océanos absorben alrededor del 90% del exceso de calor atrapado por los gases de efecto invernadero, lo que provoca su acidificación y el blanqueamiento de corales.",
    "El dióxido de carbono (CO2) puede permanecer en la atmósfera entre 300 y 1,000 años, lo que significa que las emisiones actuales afectan el clima durante siglos.",
    "La concentración de CO2 en la atmósfera ha aumentado más de un 50% desde el inicio de la Revolución Industrial, alcanzando niveles no vistos en millones de años.",
    "La quema de combustibles fósiles (carbón, petróleo y gas) representa más del 75% de las emisiones mundiales de gases de efecto invernadero.",
    "El deshielo de los glaciares de montaña y las capas polares de Groenlandia y la Antártida es la causa principal del aumento acelerado del nivel del mar.",
    "El cambio climático intensifica los fenómenos meteorológicos extremos, haciendo que las olas de calor, las sequías prolongadas y los huracanes sean más frecuentes y severos.",
    "Los bosques y selvas tropicales actúan como sumideros de carbono al absorber miles de millones de toneladas de CO2 cada año, pero la deforestación libera ese carbono de vuelta a la atmósfera.",
]


@bot.command()
async def ecofacto(ctx):
    mensaje_elegido = random.choice(ECOFACTOS)
    embed = discord.Embed(
        title="🌡️ Dato sobre el Cambio Climático",
        description=mensaje_elegido,
        color=discord.Color.green(),
    )
    await ctx.send(embed=embed)


bot.run("")
