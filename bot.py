from mmpy_bot import Bot, Settings
from plugin_gpt_text import GPTtext
from plugin_gpt_img import GPTimg
from plugin_help import Help

bot = Bot(
	settings=Settings(
		MATTERMOST_URL = "https://mattermost.zveronline.ru",
        MATTERMOST_PORT = 443,
		BOT_TOKEN = "9huy5zqt1in9jj79db7hiydpyw",
		BOT_TEAM = "z-network",
        SSL_VERIFY = True,
	),  # Either specify your settings here or as environment variables.
	plugins=[GPTtext(), GPTimg(), Help()],  # Add your own plugins here.
)
bot.run()