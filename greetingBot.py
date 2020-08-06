import discord
import random
import requests 
import json
import datetime
from bs4 import BeautifulSoup
from discord.ext import commands

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command(aliases=['hello'])
async def greet(ctx):
    await ctx.send("Hello.")

@client.command(aliases=['randomNumber'])
async def rng(ctx, a, b):
    c = random.randrange(int(a), int(b))

    await ctx.send(c)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = [
        'Yes.', 
        'No.',
        'Maybe.' 
    ]
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command(aliases=['jokes'])
async def joke(ctx):
    gagbag = [
        'Why did the chicken cross the road? To practice social distancing.',
        'You hear a couple of antennae got married? Yeah...the ceremony wasn\'t much, but the reception was incredible!',
        'Two drums and a symbol fell off a cliff...Ba Dum Tsss',
        'A jumper cable walks into a bar. The bartender says: "I\'ll serve you, BUT DON\'T START ANYTHING"',
        'A dyslexic man walks into a bra...',
        'Two cannibals are eating a clown. One says to the other: "Does this taste funny to you?"',
        'Why can\'t you hear a pterodactyl go to the bathroom? Because the p is silent.',
        'A man wakes up in a hospital after a terrible accident. He shouts "Doctor, Doctor! I can\'t feel my legs!".' +
         'The doctor replies "I know, I amputated you\'re arms."',
        'I went to seafood disco last week...I pulled a muscle.',
        'The American incarceration system.',
        'Suicide is the 10th leading cause of death in the United States.',
        'Chitose is best girl.',
        'Overlord is a good show.',
        'Marine-senchou is 17 years old.',
        '.joke',
        'I am just a bot...'
    ]
    await ctx.send(f'{random.choice(gagbag)}')

@client.command(aliases=['cg'])
async def cutegirl(ctx):
    async with ctx.channel.typing():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-gb',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*,q=0.8',
            'Referer': 'http://wikipedia.org/',
            'Connection': 'keep-alive'
        }
        #using 4chan api to get threads
        APIurl = "https://a.4cdn.org/c/threads.json"
        APIrequest = requests.get(url=APIurl)
        threadInfo = APIrequest.json()
        #using data from api about threads to get a random thread
        randomPageValue = random.randint(1, 10)
        randomThreadValue = threadInfo[randomPageValue]["threads"][random.randrange(len(threadInfo[randomPageValue]["threads"]))]["no"]
        
        #using bs4 to parse through the random thread and return a random image
        #will need a new requests.get for the new thread
        url = "https://boards.4channel.org/c/thread/" + str(randomThreadValue) 
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.findAll('a')
        imageList = []
        base_url = "https:"

        for t in posts:
            if '.jpg' in t["href"]:
                new_url = base_url + t["href"]
                imageList.append(new_url)
                #print(new_url) 

        await ctx.send(random.choice(imageList))

@client.command(aliases=['wp'], hidden=True)
async def wallpaper(ctx):
    async with ctx.channel.typing():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-gb',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*,q=0.8',
            'Referer': 'http://wikipedia.org/',
            'Connection': 'keep-alive'
        }
        #using 4chan api to get threads
        APIurl = "https://a.4cdn.org/wg/threads.json"
        APIrequest = requests.get(url=APIurl)
        threadInfo = APIrequest.json()
        #using data from api about threads to get a random thread
        randomPageValue = random.randint(1, 10)
        randomThreadValue = threadInfo[randomPageValue]["threads"][random.randrange(len(threadInfo[randomPageValue]["threads"]))]["no"]
        
        #using bs4 to parse through the random thread and return a random image
        #will need a new requests.get for the new thread
        url = "https://boards.4channel.org/wg/thread/" + str(randomThreadValue) 
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.findAll('a')
        imageList = []
        base_url = "https:"

        for t in posts:
            if '.jpg' in t["href"]:
                new_url = base_url + t["href"]
                imageList.append(new_url)
                #print(new_url) 

        await ctx.send(random.choice(imageList))

@client.command(aliases=['cb'])
async def cuteboy(ctx):
    async with ctx.channel.typing():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-gb',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*,q=0.8',
            'Referer': 'http://wikipedia.org/',
            'Connection': 'keep-alive'
        }
        #using 4chan api to get threads
        APIurl = "https://a.4cdn.org/cm/threads.json"
        APIrequest = requests.get(url=APIurl)
        threadInfo = APIrequest.json()
        #using data from api about threads to get a random thread
        randomPageValue = random.randint(1, 10)
        randomThreadValue = threadInfo[randomPageValue]["threads"][random.randrange(len(threadInfo[randomPageValue]["threads"]))]["no"]
        
        #using bs4 to parse through the random thread and return a random image
        #will need a new requests.get for the new thread
        url = "https://boards.4channel.org/cm/thread/" + str(randomThreadValue) 
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.findAll('a')
        imageList = []
        base_url = "https:"

        for t in posts:
            if '.jpg' in t["href"]:
                new_url = base_url + t["href"]
                imageList.append(new_url)
                #print(new_url) 

        await ctx.send(random.choice(imageList))

@client.command(aliases=['u'])
async def yuri(ctx):
    async with ctx.channel.typing():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-gb',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*,q=0.8',
            'Referer': 'http://wikipedia.org/',
            'Connection': 'keep-alive'
        }
        #using 4chan api to get threads
        APIurl = "https://a.4cdn.org/u/threads.json"
        APIrequest = requests.get(url=APIurl)
        threadInfo = APIrequest.json()
        #using data from api about threads to get a random thread
        randomPageValue = random.randint(1, 10)
        randomThreadValue = threadInfo[randomPageValue]["threads"][random.randrange(len(threadInfo[randomPageValue]["threads"]))]["no"]
        
        #using bs4 to parse through the random thread and return a random image
        #will need a new requests.get for the new thread
        url = "https://boards.4channel.org/u/thread/" + str(randomThreadValue) 
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.findAll('a')
        imageList = []
        base_url = "https:"

        for t in posts:
            if '.jpg' in t["href"]:
                new_url = base_url + t["href"]
                imageList.append(new_url)
                #print(new_url) 

        await ctx.send(random.choice(imageList))

@client.command(aliases=['awp'], hidden=True)
async def animeWallpaper(ctx):
    async with ctx.channel.typing():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-gb',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*,q=0.8',
            'Referer': 'http://wikipedia.org/',
            'Connection': 'keep-alive'
        }
        #using 4chan api to get threads
        APIurl = "https://a.4cdn.org/w/threads.json"
        APIrequest = requests.get(url=APIurl)
        threadInfo = APIrequest.json()
        #using data from api about threads to get a random thread
        randomPageValue = random.randint(1, 10)
        randomThreadValue = threadInfo[randomPageValue]["threads"][random.randrange(len(threadInfo[randomPageValue]["threads"]))]["no"]
        
        #using bs4 to parse through the random thread and return a random image
        #will need a new requests.get for the new thread
        url = "https://boards.4channel.org/w/thread/" + str(randomThreadValue) 
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        posts = soup.findAll('a')
        imageList = []
        base_url = "https:"

        for t in posts:
            if '.jpg' in t["href"]:
                new_url = base_url + t["href"]
                imageList.append(new_url)
                #print(new_url) 

        await ctx.send(random.choice(imageList))

@client.command()
async def weather(ctx, city):
    async def getWeather():
        url = "http://api.openweathermap.org/data/2.5/weather?q="
        apikey = "&appid=2b224bf41e456f4432d30b7ec99b77cf"
        unitChanger = "&units=imperial"
        response = requests.get(url + city + unitChanger + apikey)
        weatherData = response.json()
        return weatherData
    
    weatherValue = await getWeather()

    await ctx.send('Weather forecast for: ')
    await ctx.send(weatherValue["name"])
    await ctx.send('Sky condition: ')
    await ctx.send(weatherValue["weather"][0]["main"])
    await ctx.send('Additional notes:')
    await ctx.send(weatherValue["weather"][0]["description"])
    await ctx.send('Temperature: ')
    await ctx.send(weatherValue["main"]["temp"])
    await ctx.send('Will feel like: ')
    await ctx.send(weatherValue["main"]["feels_like"])
    await ctx.send("Day's low: ")
    await ctx.send(weatherValue["main"]["temp_min"])
    await ctx.send("Day's high: ")
    await ctx.send(weatherValue["main"]["temp_max"])
    await ctx.send('Humidity (%): ')
    await ctx.send(weatherValue["main"]["humidity"])
    await ctx.send('Sunrise: ')
    await ctx.send(datetime.datetime.fromtimestamp(weatherValue["sys"]["sunrise"]))
    await ctx.send('Sunset: ')
    await ctx.send(datetime.datetime.fromtimestamp(weatherValue["sys"]["sunset"]))

#using a url for an image, you can do something like this
        #with open('filename', 'wb') as f:
        #   f.write(r.content)
        #essentially what this does is that it takes the content of the url - which is given as an image in bytes, and writes it to
        #a filename of your choosing with wb (write bytes) and downloads the image in the same directory as the python program
client.run('NzM2NDAyMTA0MjQ3MTI0MDUw.XxuR5w.qFgtpzBIfMNIIHYjWv_RmQdISsE')