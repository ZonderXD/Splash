import discord
import asyncio
import datetime
import random as r
import random
import io
import os
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='<')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'          [Splash Bot]')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('EXPLOIT SPLASH'))
    print(f"[Splash Bot] Bot successfully launched!;")
    print(f"[Splash bot] Name: [{bot.user}];")
    print(f'[Splash Bot] ID: [{bot.user.id}]')
    print('[------------------------------]')
    print(f'          [Other]')

@bot.event
async def is_owner(ctx):
    return ctx.author.id == 668325441224048641 # Айди создателя бота
    return ctx.author.id == 492354378083336194

@bot.event
async def on_message(message):
	await bot.process_commands(message)
	
	if '<скрипты 1' in message.content.lower():
		await message.channel.send(embed = discord.Embed(description = f'**Страница 1:\n\n `(1)` - Break In\n `(2)` - Bubble Gum Simulator\n `(3)` - Blade Throwing Simulator\n `(4)` - Boss Fighting Simulator\n `(5)` - EggHunt 2020\n `(6)` - Ghost Simulator\n `(7)` - Hide and Seek Extreme\n `(8)` - Hole Simulator\n `(9)` - Mad City\n `(10)` - Soda Simulator**', color=0xbb1d))
		return

	if '<скрипты 2' in message.content.lower():
		await message.channel.send(embed = discord.Embed(description = f'**Страница 2:\n\n `(11)` - Restaurant Tycoon 2\n `(12)` - \n `(13)` - **', color=0xbb1d))
		return

	if '<скрипты 3' in message.content.lower():
		await message.channel.send(embed = discord.Embed(description = f'**Coming Soon**', color=0xbb1d))
		return

	if '<скрипты' in message.content.lower():
		await message.channel.send(embed = discord.Embed(description = f'**Скрипты:\n\n `<скрипты 1` - Страница 1\n `<скрипты 2` - Страница 2\n `<скрипты 3` - Страница 3**', color=0xbb1d))
		await message.channel.send(embed = discord.Embed(description = f'**F.A.Q**\n\n```Наш сервер не несёт ответственность если Вам выдадут бан. Этот бот создан только для скриптов и развличения. Если вы будете писать к примеру: <Jail Break, то Вам выдадут пред. Спасибо за внимание!```\n ```Что бы узнать скрипт введите название игры или напишите например: <скрипт 1```\n ```По 1 причине Вы не сможете использовать команду: <скрипт 11, так как она не работает```', color=0xbb1d))
		return

	if 'Break In' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Break In__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700718076886515752/2020-04-17_16-10-15.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Break_In_GUI.txt'))
		return

	if '<скрипт 1' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Break In__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
        
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700718076886515752/2020-04-17_16-10-15.png')
		
		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Break_In_GUI.txt'))
		return

	if 'Blade Throwing Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Blade Throwing Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723653297438730/2020-04-17_17-05-10.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Blade Throwing Simulator.txt'))
		return

	if '<скрипт 3' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Blade Throwing Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723653297438730/2020-04-17_17-05-10.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Blade Throwing Simulator.txt'))
		return

	if 'Bubble Gum Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Bubble Gum Simulator__\n\n Ключ: `Weeb`\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723726639038474/2020-04-17_16-58-09.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Bubble Gum Simulator.txt'))
		return

	if '<скрипт 2' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Bubble Gum Simulator__\n\n Ключ: `Weeb`\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723726639038474/2020-04-17_16-58-09.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Bubble Gum Simulator.txt'))
		return

	if 'Boss Fighting Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Boss Fighting Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723682070233118/2020-04-17_16-38-19.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Boss Fighting Simulator.txt'))
		return

	if '<скрипт 4' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Boss Fighting Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700723682070233118/2020-04-17_16-38-19.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Boss Fighting Simulator.txt'))
		return

	if 'EggHunt 2020' in message.content:
		embed = discord.Embed(description = f'**Скрипт на __EggHunt 2020__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700724167590412388/2020-04-17_16-33-15.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/EggHunt2020.txt'))
		return

	if '<скрипт 5' in message.content:
		embed = discord.Embed(description = f'**Скрипт на __EggHunt 2020__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700724167590412388/2020-04-17_16-33-15.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/EggHunt2020.txt'))
		return

	if 'Ghost Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Ghost Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728205157597325/2020-04-17_16-36-54.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Ghost Simulator.txt'))
		return

	if '<скрипт 6' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Ghost Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728205157597325/2020-04-17_16-36-54.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Ghost Simulator.txt'))
		return

	if 'Hide and Seek Extreme' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Hide and Seek Extreme__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728230239404142/2020-04-17_16-48-42.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Hide and Seek Extreme.txt'))
		return

	if '<скрипт 7' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Hide and Seek Extreme__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728230239404142/2020-04-17_16-48-42.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Hide and Seek Extreme.txt'))
		return

	if 'Hole Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Hole Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728329183166534/2020-04-17_16-18-50.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Hole Simulator.txt'))
		return

	if '<скрипт 8' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Hole Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728329183166534/2020-04-17_16-18-50.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Hole Simulator.txt'))
		return

	if 'Mad City' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Mad City__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728329363259472/2020-04-17_17-13-14.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Mad Lads V7.txt'))
		return

	if '<скрипт 9' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Mad City__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728329363259472/2020-04-17_17-13-14.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Mad Lads V7.txt'))
		return

	if 'Soda Simulator' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Soda Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728334962917497/2020-04-17_16-26-47.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Soda Simulator.txt'))
		return

	if '<скрипт 10' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Soda Simulator__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/700728334962917497/2020-04-17_16-26-47.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Soda Simulator.txt'))
		return

	if 'Restaurant Tycoon 2' in message.content:
		embed = discord.Embed(description = f'**Скрипт на игру __Restaurant Tycoon 2__\n\n\n\n :point_down:Картинка GUI:point_down:**', color=0xbb1d)
		
		embed.set_image(url = 'https://cdn.discordapp.com/attachments/691953915196997689/701029586422595594/2020-04-18_01-04-32.png')

		await message.channel.send(embed = embed)
		await message.channel.send(file=discord.File(fp = 'C:/Users/User/Desktop/Windows/Bots/Splash Bot/Scripts/Restaurant Tycoon 2.txt'))
		return
	
	ctx = message.content
	author = message.author
	channel = message.channel.name
	guild = message.guild.name
	print(" [Message]: {0}\n [Author]: {1}\n [Channel]: {2}\n [Guild]: {3}".format(ctx,author,channel,guild))
	print("[------------------------------]")
	print(f'          [Next]')

@bot.command()
@commands.check(is_owner)
@commands.cooldown(1, 10, commands.BucketType.user)
async def spammer(ctx, user, number):
              if int(number) <= int(25):
                        men = bot.get_user(int(user[3:-1]))

                        i = 0

                        while i <= int(number):

                                if i >= int(number):
                                        await ctx.send(f'**Все! Вы заспамили пользователя, {ctx.message.author}**')
                                        break

                                i += 1
                                await men.send(f'Ты заспамлен!!!!**')
                                print(f'spamming user - {men}, ctx.author - {ctx.message.author}, server - {ctx.guild.name} -')

@bot.command(name = "8ball")
async def ball(ctx, *, arg):

    message = ['Нет','Да','Возможно','Опредленно нет'] 
    s = random.choice( message )
    await ctx.send(embed = discord.Embed(description = f'**:crystal_ball: Знаки говорят:** {s}', color=0x0c0c0c))
    return

# Работа с ошибками шара

@ball.error 
async def ball_error(ctx, error):

    if isinstance( error, commands.MissingRequiredArgument ): 
        await ctx.send(embed = discord.Embed(description = f'Пожалуйста, укажите вопрос.', color=0x0c0c0c))

@bot.command()
async def server(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"Сервер {ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
    embed.description=(
        f":timer: **Сервер создали: `{ctx.guild.created_at.strftime('%A, %b %#d %Y')}`**\n\n"
        f":flag_white: **Регион: `{ctx.guild.region}`**\n\n"
        f":cowboy:  **Глава сервера: `{ctx.guild.owner}`**\n\n"
        f":tools: **Ботов на сервере: `{len([m for m in members if m.bot])}`**\n\n"
        f":green_circle: **Онлайн: `{online}`**\n\n"
        f":black_circle: **Оффлайн: `{offline}`**\n\n"
        f":yellow_circle: **Отошли: `{idle}`**\n\n"
        f":red_circle: **Не трогать: `{dnd}`**\n\n"
        f":shield: **Уровень верификации: `{ctx.guild.verification_level}`**\n\n"
        f":musical_keyboard: **Всего каналов: `{allchannels}`**\n\n"
        f":loud_sound: **Голосовых каналов: `{allvoice}`**\n\n"
        f":keyboard: **Текстовых каналов: `{alltext}`**\n\n"
        f":briefcase: **Всего ролей: `{allroles}`**\n\n"
        f":slight_smile: **Людей на сервере: `{ctx.guild.member_count}`**\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Информация о сервере: {ctx.guild.name}")
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_owner)
async def say(ctx, *, arg):

    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = f'{arg}', color=0x0c0c0c))

@bot.command()
@commands.check(is_owner)
async def off(ctx):
	await ctx.message.delete()
	await ctx.send(embed = discord.Embed(description = f'**Бот Splash был выключен. И поэтому Вы не сможете его использовать. Вам надо просто ждать пока бот включится! Спасибо за внимание :3**', color=0x0c0c0c))

@bot.command(aliases = ['count', 'calc', 'вычисли', 'math'])
async def __count(ctx, *, args = None):
    text = ctx.message.content

    if args == None:
        await ctx.send(embed = discord.Embed(description = 'Пожалуйста, укажите выражение для оценки.', color = 0x39d0d6))
    else:
        result = eval(args)
        await ctx.send(embed = discord.Embed(description = f'Результат примера: `{args}`: \n`{result}`', color = 0x39d0d6))

@bot.command()
async def avatar(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
	emb = discord.Embed( title = 'Команды:', color=0x6fdb9e )

	emb.add_field(name='Информационные:', value='`<user` - Узнать информацию о пользователе\n `<server` - Узнать информацию о сервере', inline = False)
	emb.add_field(name='Скрипты:', value='`<скрипты` - Страницы\n `<скрипты 1` - Страница 1\n `<скрипты 2` - Страница 2\n `<скрипты 3` - Soon',inline = False)
	emb.add_field(name='Чит:', value='`<download` - Скачать чит',inline = False)
	emb.add_field(name='Разное:', value=' `<avatar` - Аватар пользоватлея\n `<time` - Узнать время',inline = False)
	emb.add_field(name='Весёлости:', value='`<coin` - Бросить монетку\n `<math` - Решить пример\n `<8ball` - Волшебный шар\n `<ran_color` - Рандомный цвет в формате HEX',inline = False)
	emb.set_thumbnail(url=ctx.guild.icon_url)
	emb.set_footer(text='卄卂匚Ҝ乇尺 ㄒ卂#3588 © | Все права защищены', icon_url='https://cdn.discordapp.com/avatars/492354378083336194/e7ffb35260c29ea4fb9ec3beba9c5e55.png?size=512')

	await ctx.send( embed = emb )

@bot.command()
async def user(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                      f"Имя: {Member.name}\n\n"
                                                                                      f"Никнейм: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Высшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)

@bot.command()
async def time(ctx):
    emb = discord.Embed(colour= discord.Color.green(), url= 'https://www.timeserver.ru')
    
    emb.set_author(name= bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text= 'Если у вас время по МСК, то к этому добавляйте +1 час', icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://www.worldtimeserver.com/img/dst/dst-2-3.png')

    now_date = datetime.datetime.now()
    emb.add_field(name='Time', value='{}'.format(now_date))

    await ctx.send( embed = emb )

@bot.command()
async def ran_color(ctx):
    clr = (random.randint(0,16777215))
    emb = discord.Embed(
        description= f'Сгенерированый цвет : ``#{hex(clr)[2:]}``',
        colour= clr
    )

    await ctx.send(embed=emb)

@bot.command()
async def download(ctx):
	emb = discord.Embed(title = 'Скачать чит:', color=0x4400)

	emb.add_field(name='Инфо:', value='**Название чита : `Splash` !\n Функционал : `Executer & Games`**',inline = False)
	emb.add_field(name='Скачать:', value='**Ссылка на чит [Я.Диск | Пароль:hackerta] ▬ https://is.gd/DpKwpl\n Вторая ссылка [Oxy.cloud] ▬ https://is.gd/RdYE42\n Чит со всеми файлами и тп. (Для тех у кого не работает Splash Bootstrapper) ▬ https://oxy.st/d/HgOb\n `[Версия Splash Bootstrapper 3.0]`**',inline = False)
	emb.set_footer(text='卄卂匚Ҝ乇尺 ㄒ卂#3588 © | Все права защищены', icon_url='https://cdn.discordapp.com/avatars/492354378083336194/e7ffb35260c29ea4fb9ec3beba9c5e55.png?size=512')
    
	await ctx.send( embed = emb )

@bot.command()
async def coin( ctx ):
    coins = [ 'орел', 'решка' ]
    coins_r = random.choice( coins )
    coin_win = 'орел'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':tada: { ctx.message.author.name }, выиграл! 
            Тебе повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':thumbsdown:  { ctx.message.author.name }, проиграл! 
            Тебе не повезло у тебя: ``{ coins_r }``''', color = 0x0c0c0c))

# Token Bot XD
token = os.environ.get("Token")
bot.run(str(token))
