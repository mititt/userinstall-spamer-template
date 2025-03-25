@bot.tree.command(name="spam", description="スパムをする")
@app_commands.user_install
@app_commands.guild_only
@app_commands.private_channel_only
async def send_messages(interaction: discord.Interaction):
    await interaction.response.send_message("開始します！", ephemeral=True)

    for i in range(10):　#回数
        try:
            await interaction.followup.send("ないよー",allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True, replied_user=True))
        except discord.HTTPException:
            pass
