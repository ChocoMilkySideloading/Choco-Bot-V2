import os
import discord
from discord.ext import commands
from discord import app_commands
import random
import math  # For math command

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Logged in as {bot.user} | Slash commands synced.")

TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    raise ValueError("No Discord token found in environment variables!")

bot.run(TOKEN)


# /pfp
@tree.command(name="pfp", description="Get a user's profile picture.")
async def pfp(interaction: discord.Interaction, user: discord.User = None):
    user = user or interaction.user
    await interaction.response.send_message(user.avatar.url)

# /dns
@tree.command(name="dns", description="Get the DNS install config link.")
async def dns(interaction: discord.Interaction):
    await interaction.response.send_message(
        "📡 DNS Install:\nhttps://cdn.discordapp.com/attachments/1376994219649929388/1398794767084683274/Neb_DNS__Webclip.mobileconfig?ex=688de8e4&is=688c9764&hm=b61ec89bedd7a640ba4aadd7bdc522a117f68f91c0336c4b12e98a43563e0ba7&"
    )

# /chocomilky_app
@tree.command(name="chocomilky_app", description="Get the Choco Milky app link.")
async def chocomilky_app(interaction: discord.Interaction):
    await interaction.response.send_message(
        "📲 Choco Milky App:\nhttps://cdn.discordapp.com/attachments/1373569891994697888/1378195101104476232/choco_milky_app.mobileconfig?ex=688d74b5&is=688c2335&hm=1ded2c12cd49bccb9d3fb48beadd07a1e4b22c63a99b74e3e9ba4e5271fc32bd&"
    )

# /coin
@tree.command(name="coin", description="Flip a coin.")
async def coin(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"🪙 {result}")

# /dice
@tree.command(name="dice", description="Roll a dice.")
async def dice(interaction: discord.Interaction):
    await interaction.response.send_message(f"🎲 You rolled a {random.randint(1, 6)}")

# /8ball
@tree.command(name="8ball", description="Ask the magic 8-ball a question.")
@app_commands.describe(question="What do you want to ask?")
async def eightball(interaction: discord.Interaction, question: str):
    responses = [
        "Yes.", "No.", "Maybe.", "Definitely.",
        "Absolutely not.", "Ask again later.",
        "I'm not sure.", "Without a doubt."
    ]
    await interaction.response.send_message(f"🎱 {random.choice(responses)}")

# /kick
@tree.command(name="kick", description="Kick a user (requires permissions).")
@app_commands.checks.has_permissions(kick_members=True)
@app_commands.describe(user="User to kick", reason="Reason for kick")
async def kick(interaction: discord.Interaction, user: discord.Member, reason: str = "No reason"):
    await user.kick(reason=reason)
    await interaction.response.send_message(f"👢 {user.mention} was kicked.\nReason: {reason}")

# /ban
@tree.command(name="ban", description="Ban a user (requires permissions).")
@app_commands.checks.has_permissions(ban_members=True)
@app_commands.describe(user="User to ban", reason="Reason for ban")
async def ban(interaction: discord.Interaction, user: discord.Member, reason: str = "No reason"):
    await user.ban(reason=reason)
    await interaction.response.send_message(f"🔨 {user.mention} was banned.\nReason: {reason}")

# /math
@tree.command(name="math", description="Solve a math question.")
@app_commands.describe(question="Type a math expression like 2 + 2 or (5 * 3) / 2")
async def math_cmd(interaction: discord.Interaction, question: str):
    try:
        allowed = "0123456789+-*/(). "
        if not all(char in allowed for char in question):
            await interaction.response.send_message("❌ Only numbers and math symbols (+-*/().) are allowed.")
            return

        result = eval(question)
        await interaction.response.send_message(f"🧮 `{question}` = **{result}**")
    except Exception:
        await interaction.response.send_message("⚠️ Invalid math expression.")

# /joke
@tree.command(name="joke", description="Tell a random joke.")
async def joke(interaction: discord.Interaction):
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
        "Why did the math book look sad? Because it had too many problems.",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    await interaction.response.send_message(random.choice(jokes))

import os
bot.run(os.getenv("DISCORD_TOKEN"))

