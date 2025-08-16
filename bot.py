import discord
from discord.ext import commands
from discord import app_commands
import os
from flask import Flask
import threading
from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Flask pour Render
app = Flask(__name__)
@app.route("/")
def home():
    return "Say/Embed bot actif."
def run_web():
    app.run(host="0.0.0.0", port=8080)
threading.Thread(target=run_web).start()

@tree.command(name="say", description="Envoyer un message via le bot")
async def say(interaction: discord.Interaction, message: str):
    await interaction.channel.send(message)
    await interaction.response.send_message("✅ Message envoyé.", ephemeral=True)

@tree.command(name="embed", description="Envoyer un embed")
async def embed(interaction: discord.Interaction, titre: str, description: str):
    embed = discord.Embed(title=titre, description=description, color=discord.Color.blurple())
    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Embed envoyé.", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Bot say/embed prêt : {bot.user}")

keep_alive()
bot.run(TOKEN)
bot.run(os.getenv("DISCORD_TOKEN"))
