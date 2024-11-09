import urllib.parse, urllib.request, re
import asyncio
from youtube_dl import YoutubeDL
from discord.ext import commands
import time
import json
import discord
from random import randint
from discord import FFmpegPCMAudio
import random
import yt_dlp
from ast import alias
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from asyncio import sleep

file = open('config.json', 'r')
config = json.load(file)

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS ={}

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(config["prefix"], intents=intents) # intents=discord.Intents.all())


queues = {}

def check_queue(ctx, id):
    if queues[id] !=[]:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)


#----------События----------
@bot.event
async def on_member_join(ctx):
    await ctx.send(embed=discord.Embed(title= f'Привет, я бот созданный Кетцалем, префикс - p! , подробная информация о командах p!Help', color = 0x2BC7CD))
    

@bot.event
async def on_ready():
    game = discord.Game("Жизнь")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    print("Бот запущен")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} команды можно использовать")
    except Exception as e:
        print(e)

#----------команды----------
@bot.command(name = 'hello')
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention} Привет, и я бот созданный кетцалем, / - команды в разработке')
'''
@bot.command(name = 'random_int')
async def random_int(ctx, arg1, arg2):
    try:
        await ctx.send(embed=discord.Embed(title= f'{ctx.message.content}:', description=f'Случайное число {randint(int(arg1),int(arg2))}', color = 0x2BC7CD))
    except Exception as e:
        await ctx.send("нет допустимых аргументов")
 '''   

@bot.command(name="sync")
async def sync(ctx):
    
    if ctx.author.id == 454176883232342017 or ctx.author.id == 270924630452207616:
        synced = await bot.tree.sync()
        await ctx.send(f'Command {len(synced)} tree synced.')
    else:
        await ctx.send('Прости,ты не имеешь доступ к этой команде')


@bot.tree.command(name = 'random',description="random number")
async def randomize(interaction: discord.Interaction, arg1: str, arg2: str):
    await interaction.response.send_message(embed=discord.Embed(title= f'random', description=f'Ваше случайное число {randint(int(arg1),int(arg2))}', color = 0x2BC7CD))

@bot.tree.command(name = 'hello',description="Ку")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} Привет, и я бот созданный кетцалем", ephemeral=True)


@bot.command(name = "Help")
async def Help(ctx):
    await ctx.send(f'{ctx.author.mention}Привет, пока что команд не так много как бы хотелось, но пока что да. ' )
    
    await ctx.send(embed=discord.Embed(title= f'Список команд', description='-------------:fox:Команды для развлекухи:fox:------------- \n fox - случайная гифка/картинка лисы \n cat - случайная гифка/картинка кота \n arc - neco arc в студии! \n---------------:headphones:команды для музыки:headphones:---------------- \n join - приглашает бота в голосовой канал \n play - запускает музыку(нужно вставлять музыку из списка) \n  stop - прекращает работу аудио и удаляет очередь \n pause/resume - останавливае прогрывание/возобновляет проигрывание \n leave - бот покидает голосовой канал \n queue - добавляет в очередь аудио ', color = 0x2BC7CD))
    


@bot.tree.command(name = "fox", description="случайная гифка/картинка лисы")
async def fox(interaction: discord.Interaction):
    embed= discord.Embed(description="Твоя лиса на день", color= 0x2BC7CD)
    gif = [
    'https://media.tenor.com/HLcwNOIAbXEAAAAj/samifying-cheers.gif',
    'https://media.tenor.com/ete36usU32cAAAAM/siritops-cute-fox.gif',
    'https://avatars.mds.yandex.net/i?id=6696fed94fb7e20e4f26b3c6cb09f445-5402592-images-thumbs&n=13',
    'https://i.pinimg.com/originals/b4/92/9c/b4929cd8d7c1179b8ffd3ce7124dbf1f.gif',
    'https://steamuserimages-a.akamaihd.net/ugc/782979956675499954/0FBF9E4299131E02016472951D8283E32089FF28/?imw=512&amp;imh=410&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true',
    'https://pa1.narvii.com/7700/3f3372eb29da59bbcc58f3f0ef2dd1330e0c5015r1-498-498_hq.gif',
    'https://steamuserimages-a.akamaihd.net/ugc/782979956675499954/0FBF9E4299131E02016472951D8283E32089FF28/?imw=512&amp;imh=410&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true',
    'https://avatars.mds.yandex.net/i?id=02468013b3d5348efcfd8464c682de4d-4901367-images-thumbs&n=13',
    'https://media.tenor.com/3qicL0hVKkMAAAAd/fox-cute.gif',
    'https://media.tenor.com/yO7B6Zur2O0AAAAj/fox-love.gif',
    'https://media.tenor.com/eIgvoJQOx8oAAAAj/fox-cute.gif',
    'https://media.tenor.com/e4RAw8KYoRkAAAAj/fox-pat.gif',
    'https://media.tenor.com/FBKW80Hyq2kAAAAM/yumi-fox.gif',
    'https://media.tenor.com/f7D3hS56QTsAAAAM/senko-san-stare.gif',
    'https://media.tenor.com/sNRIeFtEai4AAAAM/fox-cute.gif',
    'https://media.tenor.com/oZndkc3eygYAAAAM/kaioura-love-kaioura.gif',
    'https://media.tenor.com/mUZISqUbilgAAAAM/anime-cute.gif',
    'https://media.tenor.com/DhrtKsCapUEAAAAM/senko.gif',
    'https://media.tenor.com/E5UL_DGo_KQAAAAM/anime-cute.gif',
    'https://media.tenor.com/gC6aF3fLDAYAAAAM/happy-fox.gif',
    'https://media.tenor.com/-fLpLo6MLqUAAAAM/kamiko-kana-vtuber.gif']
    fox = random.choice(gif)
    embed.set_image(url = fox)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name = "arc", description="neco arc в студии!")
async def neco_arc(interaction: discord.Interaction):
    embed = discord.Embed(description="Dori dori dori", color= 0x2BC7CD)
    gif = [
        'https://media.tenor.com/GMNmwhvGBPwAAAAM/neco-arc.gif',
        'https://media.tenor.com/adACx7g26agAAAAj/neco-arc-dance.gif',
        'https://media.tenor.com/S0Dmy6UrlXwAAAAM/neco-arc.gif',
        'https://media.tenor.com/Qj3meRpU2hgAAAAj/cute-neko.gif',
        'https://media.tenor.com/hdl1-Mdo5XkAAAAM/neko-arc.gif',
        'https://media.tenor.com/12RxYu2lUkIAAAAM/neco-arc.gif'
    ]
    arc = random.choice(gif)
    embed.set_image(url = arc)
    await interaction.response.send_message(embed=embed)
@bot.tree.command(name = "cat", description="случайная гифка/картинка кота")
async def cat(interaction: discord.Interaction):
    embed= discord.Embed(description="Твой кот на день", color= 0x2BC7CD)
    gif = [
        'https://media.tenor.com/-HntKfzsd8sAAAAM/cute-cat.gif',
        'https://media.tenor.com/wL59aqQiwzAAAAAS/cat-kitty.gif',
        'https://media.tenor.com/KzRk6gKYpfMAAAAj/cat.gif',
        'https://media.tenor.com/2aSuT7p_a_UAAAAj/peachcat-cat.gif',
        'https://media.tenor.com/2aSuT7p_a_UAAAAj/peachcat-cat.gif',
        'https://media.tenor.com/fTTVgygGDh8AAAAM/kitty-cat-sandwich.gif',
        'https://media.tenor.com/XAJx1NnLN50AAAAS/this-cat-is-d-d-cat.gif',
        'https://media.tenor.com/WHyUIiHwjXIAAAAS/vat-cat.gif',
        'https://media.tenor.com/w-aJLf05-5kAAAAM/chat.gif',
        'https://media.tenor.com/zX5F3-umlYQAAAAM/nyan-cat.gif',
        'https://media.tenor.com/Db7jp2DaS6MAAAAM/cat-smiling.gif',
        'https://media.tenor.com/tntdTtC8x1MAAAAM/cat-kitty.gif',
        'https://media.tenor.com/P9DFtD3HjcwAAAAM/cat-cats-love.gif',
        'https://media.tenor.com/8ZcT-XPCVhkAAAAM/cute-cat.gif',
        'https://media.tenor.com/LLLRvDwzXuMAAAAM/bongo-cat-cat-meme.gif',
        'https://media.tenor.com/gRfq9aJPE3MAAAAM/cat-cat-love.gif'
    ]
    cat = random.choice(gif)
    embed.set_image(url = cat)
    await interaction.response.send_message(embed=embed)


@bot.command(pass_context = True)
async def join(ctx):

    if (ctx.author.voice):
        channel =  ctx.message.author.voice.channel
        voice = await channel.connect()
        song = 'music\zvuk-windows-95-2000-nt-the-microsoft-sound-30532.mp3'
        source = FFmpegPCMAudio(song)        
        voice.play(source)
    else:
        await ctx.send(f'{ctx.author.mention} Извини, но я не знаю к какому голосовому каналу подключаться')

@bot.command(pass_context = True)
async def leave(ctx):

    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(f'{ctx.author.mention} Досвидания, было приятно посидеть')
    else:
        await ctx.send(f'{ctx.author.mention} Извини, но я не могу отключиться от канала к которому я даже не подключен')


queues = {}
voice_clients = {}
youtube_base_url = 'https://www.youtube.com/'
youtube_results_url = youtube_base_url + 'results?'
youtube_watch_url = youtube_base_url + 'watch?v='
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.25"'}





@bot.command(name="play_next")
async def play_next(ctx):
    if queues[ctx.guild.id] != []:
        link = queues[ctx.guild.id].pop(0)
        await play(ctx, link=link)
    
@bot.command(name="play")
async def play(ctx, *, link):
    try:
        voice_client = await ctx.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as e:
        print(e)

    try:

        if youtube_base_url not in link:
            query_string = urllib.parse.urlencode({
                'search_query': link
            })

            content = urllib.request.urlopen(
                youtube_results_url + query_string
            )

            search_results = re.findall(r'/watch\?v=(.{11})', content.read().decode())

            link = youtube_watch_url + search_results[0]
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(link, download=False))
        song = data['url']
        player = discord.FFmpegOpusAudio(song, **ffmpeg_options)
        voice_clients[ctx.guild.id].play(player, after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx), client.loop))
    except Exception as e:
        print(e)

@bot.command(name="clear_queue")
async def clear_queue(ctx):
    if ctx.guild.id in queues:
        queues[ctx.guild.id].clear()
        await ctx.send("Очеред очищена")
    else:
        await ctx.send("Простите, но я не нашел очередь, которую нужно очистить")

@bot.command(name="pause")
async def pause(ctx):
    try:
        voice_clients[ctx.guild.id].pause()
    except Exception as e:
        print(e)

@bot.command(name="resume")
async def resume(ctx):
    try:
        voice_clients[ctx.guild.id].resume()
    except Exception as e:
        print(e)

@bot.command(name="stop")
async def stop(ctx):
    try:
        voice_clients[ctx.guild.id].stop()
        await voice_clients[ctx.guild.id].disconnect()
        del voice_clients[ctx.guild.id]
    except Exception as e:
        print(e)

@bot.command(name="queue")
async def queue(ctx, *, url):
    if ctx.guild.id not in queues:
        queues[ctx.guild.id] = []
    queues[ctx.guild.id].append(url)
    await ctx.send("Добавлено в очередь")



bot.run(config["token"])