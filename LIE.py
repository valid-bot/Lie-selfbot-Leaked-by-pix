class SELFBOT():
    __linecount__ = 1933
    __version__ = 2.1
    

	
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'[Lie Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:", 
    ":three:", 
    ":four:", 
    ":five:", 
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            SIX.run(token, bot=False, reconnect=True)
            os.system(f'title (6ix Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.CYAN}this token ain't workin my guy"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Gmail: ')
    password = input('Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW} Incorrect Password or gmail, make sure you've enabled less-secure apps access"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

async def SendWhook():
    url = ""
    whook = {
        "embeds": [
            {
                "title": "",
                "description": "",
                "thumbnail": {
                    "url": ""
                },
                "footer": {
                    "text": ""
                }
            }
        ]
    }
    async with aiohttp.ClientSession() as session:
        await session.post(url, json=whook)

def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return        

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "Lie wizzed"

colorama.init()
SIX = discord.Client()
SIX = commands.Bot(
    description='Lie Selfbot',
    command_prefix=prefix,
    self_bot=True
)
SIX.remove_command('help') 


@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="LIE ON TOP: "+value+"$ USD", 
        url="https://www.twitch.tv/syrusisthebestcoder", 
    )
    await SIX.change_presence(activity=btc_stream)

@SIX.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{error_str}"+Fore.RESET)

@SIX.event
async def on_message_edit(before, after):
    await SIX.process_commands(after)

@SIX.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.GREEN}[{message.channel}]"
        f"{Fore.WHITE} - SERVER: {Fore.GREEN}[{message.guild}]"   
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.GREEN}[{message.channel}]"
        f"{Fore.WHITE} - SERVER: {Fore.GREEN}[{message.guild}]"   
    +Fore.RESET)  

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.GREEN}[{message.channel}]" 
        f"{Fore.WHITE} - SERVER: {Fore.GREEN}[{message.guild}]"
        f"{Fore.WHITE} - AUTHOR: {Fore.GREEN}[{message.author}]"
        f"{Fore.WHITE} - SPEED: {Fore.GREEN}[{elapsed}]"
        f"{Fore.WHITE} - CODE: {Fore.GREEN}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.GREEN}[{message.channel}]" 
        f"{Fore.WHITE} - SERVER: {Fore.GREEN}[{message.guild}]"
        f"{Fore.WHITE} - CONTENT: {Fore.GREEN}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)        

    time = datetime.datetime.now().strftime("%H:%M %p")  
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
                
            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', 
                headers=headers,
            ).text
        
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.microseconds}'

            if 'This gift was already redeemed -_- what a scam' in r:
                print(""
                f"\n{Fore.WHITE}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.WHITE}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.WHITE}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return
            
    if 'Some goofy kid dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.WHITE}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()                     
                print(""
                f"\n{Fore.WHITE}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:    
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.WHITE}[{time} - Giveaway Couldnt React :(]"+Fore.RESET)
                    GiveawayData()            
                print(""
                f"\n{Fore.WHITE}[{time} - Giveaway Finessed]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{SIX.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:    
                print(""
                f"\n{Fore.WHITE}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)    
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.WHITE}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await SIX.process_commands(message)

@SIX.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Active" 
    else:
        giveaway = "Disabled"

    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"

    if slotbot_sniper == True:
        slotbot = "Active"
    else:
        slotbot = "Disabled"

    if privnote_sniper == True:
        privnote = "Active"
    else:
        privnote = "Disabled"    

    print(f'''{Fore.RESET}
                      


{Fore.MAGENTA} ──────────────────────────────────────────
{Fore.MAGENTA} ─██████─────────██████████─██████████████─
{Fore.MAGENTA} ─██░░██─────────██░░░░░░██─██░░░░░░░░░░██─
{Fore.MAGENTA} ─██░░██─────────████░░████─██░░██████████─
{Fore.MAGENTA} ─██░░██───────────██░░██───██░░██─────────
{Fore.MAGENTA} ─██░░██───────────██░░██───██░░██████████─
{Fore.MAGENTA} ─██░░██───────────██░░██───██░░░░░░░░░░██─
{Fore.MAGENTA} ─██░░██───────────██░░██───██░░██████████─
{Fore.MAGENTA} ─██░░██───────────██░░██───██░░██─────────
{Fore.MAGENTA} ─██░░██████████─████░░████─██░░██████████─
{Fore.MAGENTA} ─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─
{Fore.MAGENTA} ─██████████████─██████████─██████████████─
{Fore.MAGENTA} ──────────────────────────────────────────
                                                  
                                {Fore.MAGENTA}Loggin => {Fore.RED}{SIX.user.name}#{SIX.user.discriminator}{Fore.LIGHTYELLOW_EX}  ||{Fore.LIGHTYELLOW_EX}  {Fore.MAGENTA}ID => {Fore.RED}{SIX.user.id}   
                                {Fore.MAGENTA}Privnote => {Fore.RED}{privnote}{Fore.LIGHTYELLOW_EX} ||  {Fore.MAGENTA}Nitro => {Fore.RED}{nitro} 
                                {Fore.MAGENTA}Giveaway => {Fore.RED}{giveaway}{Fore.LIGHTYELLOW_EX}   ||  {Fore.MAGENTA}SlotBot => {Fore.RED}{slotbot}
                                {Fore.MAGENTA}Prefix => {Fore.GREEN}{prefix}{Fore.LIGHTYELLOW_EX}           ||  {Fore.MAGENTA}LIE =>{Fore.GREEN} v{SELFBOT.__version__}                                                     
    '''+Fore.RESET)
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Lie Selfbot v{SELFBOT.__version__}] | Logged in as {SIX.user.name}')
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    r = requests.post('https://discordapp.com/api/v6/invite/4jTxrpT', headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False

@SIX.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@SIX.command()
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@SIX.command()
async def lmgtfy(ctx, *, message):
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@SIX.command()
async def login(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')    

@SIX.command()
async def botlogin(ctx, _token):
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([  
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = '6ix-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ 
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@SIX.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@SIX.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.add_field(name="`HELP`",value="`HELP COMMAND`",inline=False)
    em.add_field(name="`INFO`",value="`INFO COMMAND`",inline=False)
    em.add_field(name="`NOKID`",value="`NOKID COMMAND`",inline=False)
    em.add_field(name="`SETUP`",value="`SETUP COMMANDS`",inline=False)
    em.add_field(name="`STEALL`",value="`STEALL COMMAND`",inline=False)
    em.add_field(name="`FUN`",value="`FUN COMMAND`",inline=False)
    em.add_field(name="`TOKEN`",value="`TOKEN COMMAND`",inline=False)   
    em.add_field(name="`NUKE`",value="`NUKE COMMAND`",inline=False)   
    em.add_field(name="`RAIDSPAM`",value="`COMINGSSOON`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADE THIZ")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/709866941736681512/711580094702944266/image0.gif")
    await ctx.send(embed=em)
@SIX.command()
async def info(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="INFO")
    em.add_field(name="`AV`",value="`SEE YOUR PFP OR SOMEONE PFP`",inline=False)
    em.add_field(name="`REVAV`",value="`WHO EVER TRY TO GET YOUR PFP U WILL GET THERE LINK PFP`",inline=False)
    em.add_field(name="`WHOIS`",value="`WHO ARE THEY INFO`",inline=False)
    em.add_field(name="`ROLEHEXCODE`",value="`GET A GOOD ROLE`",inline=False)
    em.add_field(name="`GUILDICON`",value="`DISPLAY GUILDICON`",inline=False)
    em.add_field(name="`ROLEINFO`",value="`THERE ROLE INFO`",inline=False)
    em.add_field(name="`CLS`",value="`CLEAR CONSOL`",inline=False)
    em.add_field(name="`LOGOUT`",value="`LOGOUT FORM SELFOBT`",inline=False)
    em.add_field(name="`DM`",value="`DM EVERYONE`",inline=False)
    em.add_field(name="`EVERYONE`",value="`PING EVERYONE`",inline=False)
    em.add_field(name="`EMPTY`",value="`SEND EMPTY DM`",inline=False)
    em.add_field(name="`GETWID`",value="`PRINT HWID CONSOL`",inline=False)
    em.add_field(name="`SECRET`",value="`HIDDEN MSG`",inline=False)
    em.add_field(name="`BOLD`",value="`BOLD MSG`",inline=False)
    em.add_field(name="`REVERSE`",value="`REVERSE MSG`",inline=False)
    em.add_field(name="`ASCII`",value="`ASCCI AND MAKE FANCY TEXT`",inline=False)
    em.add_field(name="`READ`",value="`READ ALL SERVER DM`",inline=False)
    em.add_field(name="`GROUPLEAVER`",value="`LEAVE ALL GROUP`",inline=False)
    em.add_field(name="`PURGE`",value="`PURGE AMOUNT U WANT`",inline=False)
    em.add_field(name="`UPTIME`",value="`SHOW HOW LONG YOUR SELFBOT WAS ON`",inline=False)
    em.add_field(name="`HASTBIN`",value="`SAVE YOUR TEXT IN HASTBIN`",inline=False)
    em.add_field(name="`FIRSTMESSAGE`",value="`GET YOUR FIRST MSG IN CHANNEL`",inline=False)
    em.add_field(name="`ABC`",value="`READ ABC`",inline=False)
    em.add_field(name="`DEVOWEL`",value="`DEVOWELS MSG`",inline=False)
    em.add_field(name="`SPEAK`",value="`1337 LANGUAGEl`",inline=False)
    em.add_field(name="`COMBINE`",value="`MATCH THERE NAME`",inline=False)
    em.add_field(name="`PINGWEB`",value="`PINGWEB`",inline=False)
    em.add_field(name="`SPAM`",value="`SPAM AMOUNT AND NAME`",inline=False)
    em.add_field(name="`CLEAR`",value="`CLEAR/GLITCH CHAT`",inline=False)
    em.add_field(name="`TTS`",value="`AUDIO MSG`",inline=False)
    em.add_field(name="`UPPER`",value="`MAKE THE TEXT ALL CAP`",inline=False)
    em.add_field(name="`IMGTFY`",value="`USE IMGTFY TO SEARCH UP SOMETHING`",inline=False)
    em.add_field(name="`GENNAME`",value="`MAKE RANDOM NAME IN SERVER`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADE THIZ")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)
@SIX.command()
async def nokid(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="NOKID")
    em.add_field(name="`LESBIAN`",value="`RANDOM LESBIAN PIC`",inline=False)
    em.add_field(name="`LEWDJEKO`",value="`RANDOM LEWDJEKO PIC`",inline=False)
    em.add_field(name="`BLOWJOB`",value="`RANDOM BLOWJOB PIC`",inline=False)
    em.add_field(name="`TITS`",value="`RANDOM TITS PIC`",inline=False)
    em.add_field(name="`BOOBS`",value="`RANDOM BOOBS PIC`",inline=False)
    em.add_field(name="`HENTAI`",value="`RANDOM HENTAI PIC`",inline=False)
    em.add_field(name="`FEET`",value="`RANDOM FEET PIC`",inline=False)
    em.add_field(name="`EROFEET`",value="`RANDOM EROFEET PIC`",inline=False)
    em.add_field(name="`ANAL`",value="`RANDOM ANAL PIC`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADE THIZ")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)

@SIX.command()
async def setup(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="SETUP")
    em.add_field(name="`SETPFP`",value="`SETPFP LINK`",inline=False)
    em.add_field(name="`BTCSTREAM`",value="`STREAM HOW MUCH CASH U HAVE`",inline=False)
    em.add_field(name="`PFPSTEAL`",value="`STEAL PEOPLE PIC`",inline=False)
    em.add_field(name="`BLANK`",value="`REMOVE PFP AND NAME`",inline=False)
    em.add_field(name="`HYPESQUAD`",value="`HYPESQUAD BRAVERY`",inline=False)
    em.add_field(name="`FAKENET`",value="`FAKENET SKYPE`",inline=False)
    em.add_field(name="`STEALALLPFP`",value="`STEAL ALL PFP`",inline=False)
    em.add_field(name="`SETS`",value="`STREAM STATUS`",inline=False)
    em.add_field(name="`SETG`",value="`GAMEING STATUS`",inline=False)
    em.add_field(name="`SETL`",value="`LISTENING STATUS`",inline=False)
    em.add_field(name="`SETW`",value="`WATCHING STATUS`",inline=False)
    em.add_field(name="`MASSCON`",value="`MASSCON SKYPE LIE`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADZ THIS")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)

@SIX.command()
async def fun(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="FUN")
    em.add_field(name="`FOX`",value="`RANDOM FOX PIC`",inline=False)
    em.add_field(name="`DOG`",value="`RANDOM DOG PIC`",inline=False)
    em.add_field(name="`CAT`",value="`RANDOM CAT PIC`",inline=False)
    em.add_field(name="`MINESWEEPER`",value="`PLAY GAME IN CHAT`",inline=False)
    em.add_field(name="`8BALL`",value="`ASK QUESTION AND TELL U`",inline=False)
    em.add_field(name="`JOKE`",value="`JOKE FOR PACKING`",inline=False)
    em.add_field(name="`SLOT`",value="`RANDOM SLOT GAME`",inline=False)
    em.add_field(name="`TOPIC`",value="`TOPIC TO GET A GIRL`",inline=False)
    em.add_field(name="`WYR`",value="`WHAT WOULD U RATHER`",inline=False)
    em.add_field(name="`FEED`",value="`FEED SOMEONE`",inline=False)
    em.add_field(name="`TICKLE`",value="`TICKLE SOMEONE`",inline=False)
    em.add_field(name="`HUG`",value="`HUG SOMEONE`",inline=False)
    em.add_field(name="`SLAP`",value="`SLAP SOMEONE`",inline=False)
    em.add_field(name="`SMUG`",value="`SMUG SOMEONE`",inline=False)
    em.add_field(name="`PAT`",value="`PAT SOMEONE`",inline=False)
    em.add_field(name="`KISS`",value="`KISS SOMEONE`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADZ THIS")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)
@SIX.command()
async def steall(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="STEALL")
    em.add_field(name="`BITLY`",value="`SHORTEN BITLY URL`",inline=False)
    em.add_field(name="`TINYURL`",value="`SHORTEN TINY URL`",inline=False)
    em.add_field(name="`BACKUPF`",value="`BACKUP NAME`",inline=False)
    em.add_field(name="`AUTOBUMP`",value="`AUTOMATICALLY BUM SERVER`",inline=False)
    em.add_field(name="`MAC`",value="`INFO ABOUT YOUR MAC`",inline=False)
    em.add_field(name="`COPY`",value="`COPY SERVER`",inline=False)
    em.add_field(name="`ENCODE`",value="`ENCODE RANDOM`",inline=False)
    em.add_field(name="`DECODE`",value="`DECODE RANDOM`",inline=False)
    em.add_field(name="`ETH`",value="`MONEY SHIT`",inline=False)
    em.add_field(name="`BTC`",value="`BITCOIN MONEY`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADE THIZ")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)
@SIX.command()
async def token(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="TOKEN")
    em.add_field(name="`TOKENINFO`",value="`GET THERE INFO FROM TOKEN`",inline=False)
    em.add_field(name="`TOKENFUCK`",value="`MESS UP THERE ACCOUNT`",inline=False)
    em.add_field(name="`GEOIP`",value="`GET THE IP INFO`",inline=False)
    em.add_field(name="`GMAILBOME`",value="`SPAM THE GMAIL`",inline=False)
    em.add_field(name="`NITRO`",value="`MAKE RNADOM NITRO CODE`",inline=False)
    em.add_field(name="`PROXIES`",value="`SCRAPS HTTP/HTTPS/SOCKS4/SOCKS5`",inline=False)
    em.add_field(name="`ADDRESS`",value="`MAKE FAKE ADDRESS`",inline=False)
    em.add_field(name="`MASSLOGIN`",value="`TOKEN LOGIN`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADZ THIS")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)
@SIX.command()
async def nuke(ctx):
    await ctx.message.delete()
    em = discord.Embed(colour = discord.Colour.blue())
    em.set_author(name="NUKE")
    em.add_field(name="`LIE`",value="`MASS UP THE SERVER`",inline=False)
    em.add_field(name="`DMALL`",value="`DM EVERYONE`",inline=False)
    em.add_field(name="`BANALL`",value="`BAN ALL MEMBERS`",inline=False)
    em.add_field(name="`KICKALL`",value="`KICK ALL MEMBERS`",inline=False)
    em.add_field(name="`MAKER`",value="`MAKE MASS ROLES`",inline=False)
    em.add_field(name="`MAKEC`",value="`MAKE MASS CHANNEL`",inline=False)
    em.add_field(name="`REMOVER`",value="`REMOVE ALL ROLES`",inline=False)
    em.add_field(name="`REMOVEC`",value="`REMOVE ALL CHANNEL`",inline=False)
    em.add_field(name="`BANALL`",value="`UNBANALL MEMBERS`",inline=False)
    em.set_image(url="")
    em.set_footer(text="SYRUS MADE THIZ")
    em.set_thumbnail(url="")
    await ctx.send(embed=em)


@SIX.command(aliases=['shorteen'])
async def bitly(ctx, *, link):
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r) 
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{req.text}"+Fore.RESET)

@SIX.command()
async def cuttly(ctx, *, link):
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{req.text}"+Fore.RESET)

@SIX.command() 
async def cat(ctx):
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Cat API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f"fhttps://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{req.text}"+Fore.RESET)

@SIX.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@SIX.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])    

@SIX.command()
async def encode(ctx, string):
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@SIX.command()
async def decode(ctx, string):
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@SIX.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int):
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }        
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@SIX.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@SIX.command()
async def pingweb(ctx, website = None):
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)       

@SIX.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@SIX.command()
async def revav(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
	    format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))      

@SIX.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@SIX.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@SIX.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@SIX.command()
async def combine(ctx, name1, name2):
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)       

@SIX.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text):
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@SIX.command(aliases=['dvwl'])
async def devowel(ctx, *, text):
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@SIX.command()
async def blank(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:  
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:      
             await SIX.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await SIX.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await SIX.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command(aliases=['dong', 'penis', 'pp'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@SIX.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }    
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def tokenfuck(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': "daddy 6ix",
        'icon': "https://cdn.discordapp.com/attachments/699828368840982578/702719106406809610/giphy.gif",
        'name': "6ix NUKED U",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   

@SIX.command()
async def masslogin(ctx, choice = None):
    await ctx.message.delete()
    _masslogin(choice)

@SIX.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None):
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json', 
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:            
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@SIX.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@SIX.command()
async def copy(ctx):
    await ctx.message.delete()
    await SIX.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in SIX.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
                    if isinstance(chann, discord.Role):
                        await x.create_role(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@SIX.command()
async def six(ctx):
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
           await  channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass 
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
        )  
    except:
        pass                 
    for _i in range(999):
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name=" 6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")
        await ctx.guild.create_text_channel(name="6ix wizzed")
        await ctx.guild.create_voice_channel(name="6ix wizzed")
        await ctx.guild.create_category(name="6ix wizzed")


@SIX.command()
async def dmall(ctx, *, message):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@SIX.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@SIX.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@SIX.command()
async def maker(ctx):
    await ctx.message.delete()
    for _i in range(900):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@SIX.command()
async def makec(ctx):
    await ctx.message.delete()
    for _i in range(900):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@SIX.command()
async def removec(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@SIX.command() 
async def remover(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@SIX.command()
async def unbanll(ctx):
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@SIX.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@SIX.command()
async def dm(ctx, user : discord.Member, *, message):
    await ctx.message.delete()
    user = SIX.get_user(user.id)
    if ctx.author.id == SIX.user.id:
        return
    else:
        try:
            await user.send(message) 
        except:
            pass       


@SIX.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour):
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em) 

@SIX.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@SIX.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@SIX.command(name='8ball')
async def _ball(ctx, *, question):
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
	  'Maybe',
	  'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@SIX.command(aliases=['slots', 'bet'])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} All matchings, you won!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 in a row, you won!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} No match, you lost"}))



@SIX.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@SIX.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid):
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = SIX.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.LIGHTGREEN_EX}Something is wrong ==> {Fore.YELLOW}{e}"+Fore.RESET)

@SIX.command()
async def tts(ctx, *, message):
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@SIX.command()
async def upper(ctx, *, message):
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@SIX.command(aliases=['guildpfp'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@SIX.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx):
    await ctx.message.delete()
    for friend in SIX.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)   
       with open('Backup/Friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in SIX.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/Blocked.txt', 'a+') as f: 
            f.write(blocklist+"\n" )

@SIX.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@SIX.command()
async def mac(ctx, mac):
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='MAC Lookup Result', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Finder', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@SIX.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@SIX.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@SIX.command(aliases=['ethereum'])
async def eth(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@SIX.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@SIX.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@SIX.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@SIX.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@SIX.command()
async def anal(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *did anal with* '+user.mention, colour = discord.Colour.dark_teal())   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   


@SIX.command()
async def poke(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/poke")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *wants attention* '+user.mention, colour = discord.Colour.dark_teal())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def fuck(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *fucked* '+user.mention, colour = discord.Colour.dark_teal())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@SIX.command()
async def boobs(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *is showing* '+user.mention+ ' *boobs*', colour = discord.Colour.dark_teal())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@SIX.command()
async def head(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *gave* '+ user.mention + ' *head*', colour = discord.Colour.dark_teal())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)
  

@SIX.command()
async def lesbian(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *and* '+ user.mention + ' *are having lesbian sex*', colour = discord.Colour.dark_teal())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()  
async def feed(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *is feeding*  '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def tickle(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *tickling*  '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *slapped*  '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *hugged* '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *smugged at* '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *just gave u a pat* '+ user.mention + ' *for being good :)*', colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=SIX.user.name+' *gave u a smooch* '+ user.mention, colour = discord.Colour.magenta())
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@SIX.command(aliases=['proxy'])
async def proxies(ctx):
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@SIX.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@SIX.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == SIX.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@SIX.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in SIX.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@SIX.command()
async def setS(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await SIX.change_presence(activity=stream)    

@SIX.command()
async def setG(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await SIX.change_presence(activity=game)

@SIX.command()
async def setL(ctx, *, message):
    await ctx.message.delete()
    await SIX.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@SIX.command()
async def setW(ctx, *, message):
    await ctx.message.delete()
    await SIX.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@SIX.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in SIX.guilds:
        await guild.ack()

@SIX.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)


@SIX.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@SIX.command()
async def secret(ctx, *, message):
	await ctx.message.delete()
	await ctx.send('||'+message+'||')

@SIX.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@SIX.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx):
    await ctx.message.delete()
    print(f"HWID: {Fore.CYAN}{hwid}"+Fore.RESET)

@SIX.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))

@SIX.command()
async def everyone(ctx):
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@SIX.command()
async def logout(ctx):
    await ctx.message.delete()
    await SIX.logout()

@SIX.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()   
    btc_status.start()        

@SIX.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx):
    await ctx.message.delete()
    Dump(ctx)

@SIX.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx):
    await ctx.message.delete()
    Clear()

@SIX.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

@SIX.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
	Init()
