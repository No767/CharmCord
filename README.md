# <span style="color:pink">CharmCord</span>

### CharmCord is the best python string-based package for Discord bot creators!

---
## Stats ✨
![PyPI](https://img.shields.io/pypi/v/charmcord)
![PyPI - Downloads](https://img.shields.io/pypi/dm/aoipy?color=green&label=downloads)
![Downloads](https://static.pepy.tech/personalized-badge/aoipy?period=total&units=international_system&left_color=grey&right_color=green&left_text=downloads)
![PyPI - License](https://img.shields.io/pypi/l/aoipy)
![](https://tokei.rs/b1/github/tomschimansky/aoipy)
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

---
![logo](https://github.com/LilbabxJJ-1/AoiPy/blob/master/CharmCord%20logo.png)

---
## <span style="color:pink">CharmCord</span> Setups

Install [CharmCord](https://pypi.org/charmcord)
```bash
pip install CharmCord
```
##### Warning: Package is still in Alpha and not meant to be used on public bots
---
Simple Bot:

```python

from CharmCord import CharmClient
# ---------------Imports--------------------

bot = CharmClient(prefix="!", case_insensitive=False, intents=("all",))

bot.onReady(
    Code="$console[Bot is Ready]"
)

bot.command(
    Name="Ping", # Command Name
    Code="""
    $sendMessage[$channelID; Pong!! $ping]
    """ # Command Code
)


bot.run("*******<<TOKEN>>***********")
```


Slash Interactions/Outside Commands/Activity:

```python

from CharmCord import CharmClient, setActivity
# ---------------Imports--------------------

# Activity message is the actual status, the type is whether it'll
# be a game status, listening status, etc
act = setActivity(message="my servers", type="watching")

# For Commands outside the main.py file, you should add the 
# load_command_dir parameter with the name of your command file
bot = CharmClient(prefix="!", case_insensitive=False, intents=("all",), activity=act,  load_command_dir="Commands")


bot.onReady(
    Code="$console[Bot is Ready]"
)


bot.slashCommand(
    Name="repeat", # Name of the slash command
    Args=["sentence"], #The required arguments
    Description="Repeats what you say", # Description of command
    Code="""
    $slashSend[$slashArgs[1]]
    """ # Code running on the command
)


bot.run("*******<<TOKEN>>***********")
```

## New and still a work in progress
![](https://github.com/LilbabxJJ-1/CharmCord/blob/master/logo.gif)
## Contributors ✨

<a href="https://github.com/LilbabxJJ-1/AoiPy2.0/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LilbabxJJ-1/AoiPy2.0"  alt="aoi.py-contributors"/>
</a>
