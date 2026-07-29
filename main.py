import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import os

# --- 1. Web Server صغير باش يحافظ على البوت فايق ---
app = Flask('')

@app.route('/')
def home():
    return "Shadow Anti-Cheat is Live 24/7!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

# --- 2. كود البوت ---
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'🛡️ {bot.user} is ONLINE 24/7 and Protecting Shadow Rift!')

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client:
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect(reconnect=True, timeout=60.0, self_deaf=True)
        await ctx.send(f'🛡️ **Shadow Anti-Cheat** متصل الآن بـ **{channel.name}**!')
    else:
        await ctx.send("❌ خاصك تكون داخل لـ Voice Room بعدا!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("🛡️ **Shadow Anti-Cheat** خرج من الـ Voice Room.")

# تشغيل الـ Web Server والتسجيل فـ ديسكورد
keep_alive()

# ⚠️ من الأحسن حط التوكن هنا ولا فـ Environment Variable
TOKEN = "MTUzMTg1MjIzOTMwMjI5OTY3OA.GU76ZY.wpA7HRpu5jxwX20bhgVegz8LJDUxDA0IoFqWOk"
bot.run(TOKEN)