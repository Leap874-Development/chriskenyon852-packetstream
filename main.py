from discord.ext import commands
import json
import discord
import aiohttp
import asyncio

with open('config.json', 'r') as f:
    CONFIG = json.load(f)

# api constants
HEADERS = {'Authorization': 'Bearer %s' % CONFIG['auth_token']}
MY_INFO = '%sreseller/my_info' % CONFIG['api_url']
ALL_SUBS = '%sreseller/sub_users/view_all' % CONFIG['api_url']
NEW_SUB = '%sreseller/sub_users/create' % CONFIG['api_url']
SUB_INFO = '%sreseller/sub_users/view_single' % CONFIG['api_url']

bot = commands.Bot(command_prefix=CONFIG['prefix'])

class ProxyEmbed(discord.Embed):
    def __init__(self, user, authkey):
        self.color = discord.Color.from_rgb(*CONFIG['embed']['info_color'])

        self.user = user
        self.authkey = authkey
        self.host = CONFIG['proxy_defaults']['host']
        self.port = CONFIG['proxy_defaults']['port']

        self.proxy = 'http://%s:%s@%s:%s' % (
            self.user, self.authkey,
            self.host, self.port)

        discord.Embed.__init__(self, color=self.color)
        self.add_field(name="Username", value=self.user, inline=True)
        self.add_field(name="Access Key", value=self.authkey, inline=True)
        self.add_field(name="Host", value=self.host, inline=True)
        self.add_field(name="Port", value=self.port, inline=True)
        self.set_footer(text=self.proxy)

class ErrorEmbed(discord.Embed):
    def __init__(self, code, message):
        self.color = discord.Color.from_rgb(*CONFIG['embed']['error_color'])

        self.code = code
        self.message = message

        discord.Embed.__init__(self,
            color=self.color, title="An error occured (%s)" % self.code,
            description=self.message )

async def on_ready():
    guild_names = ', '.join([ a.name for a in bot.guilds ])
    print('PacketStream bot online and logged in as %s' % (bot.user))
    print('Connected to %s guild(s): %s' % (len(bot.guilds), guild_names))
    print('Now awaiting messages...')

@bot.command()
async def proxy(ctx, ):
    proxies = []

    # data = json.dumps({'username': username})
    # async with aiohttp.ClientSession(loop=bot.loop) as sesh:
    #     async with sesh.post(SUB_INFO, headers=HEADERS, data=data) as resp:
    #         data = await resp.json()

    if data['status'] == 200:
        embed = ProxyEmbed(data['data']['username'], data['data']['proxy_authkey'])
    else:
        embed = ErrorEmbed(data['status'], data['message'])

    await ctx.send(embed=embed)

bot.add_listener(on_ready)
bot.run(CONFIG['discord_token'])