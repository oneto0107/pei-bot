import discord
import asyncio
import random
import os

client = discord.Client()


@client.event
async def on_ready():

        print(client.user.name)
        print('성공적으로 봇이 실행됨 :D')
        game = discord.Game('파이야 도움말')
        await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
        if message.content == "p/soud/개발자 포털 0481234123!":
            await message.channel.send("개발자 포털이 열렸습니다.")
            await message.channel.send("`SPOT CAL TALM`")

        if message.content == "파이야 도움말":
                embed = discord.Embed(title="도움말", description="---", color=0x00ff00)
                embed.add_field(name="도움 명령어: ", value="파이야 도움말",inline=False)
                embed.add_field(name="운세 명령어: ", value="파이야 오늘의 운세/파이야 운세",inline=True)
                embed.add_field(name="투표 명령어: ", value="p/투표 투표이름,내용1,내용~,내용~",inline=True)
                embed.add_field(name="초대: ", value="https://discord.com/api/oauth2/authorize?client_id=863353536750026762&permissions=0&scope=bot",inline=False)
                embed.set_footer(text="수정일 : 21/07/10")
                await message.channel.send(embed=embed)

        if message.content == "파이야 오늘의 운세":
                ran = random.randint(0,3)
                if ran == 0:
                    d = "좋아요! 오늘 하루는 느낌이 좋아요!"
                if ran == 1:
                    d = "으스스.....오늘 하루 조심해요...!"
                if ran == 2:
                    d = "흠...오늘하루 물을 조심해요!"
                if ran == 3:
                    d = "흠...오늘하루 불을 조심해요!"
                await message.channel.send(d)

        if message.content == "파이야 운세":
                ran = random.randint(0,3)
                if ran == 0:
                    d = "좋아요! 오늘 하루는 느낌이 좋아요!"
                if ran == 1:
                    d = "으스스.....오늘 하루 조심해요...!"
                if ran == 2:
                    d = "흠...오늘하루 물을 조심해요!"
                if ran == 3:
                    d = "흠...오늘하루 불을 조심해요!"
                await message.channel.send(d)

        if message.content.startswith("p/투표"):
            vote = message.content[4:].split(",")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')

        if message.content == "파이야 사랑해":
            await message.channel.send("개발자 포털이 열렸습니다.")

access_token = os.environ["BOT TOKEN"]
client.run(access_token)
