import os
from mmpy_bot import Bot, Settings
from plugin_gpt_text import GPTtext
from plugin_gpt_img import GPTimg
from plugin_help import Help
from g4f.client import Client

mm_url = os.environ.get("MM_URL")
mm_token = os.environ.get("MM_TOKEN")
mm_team = os.environ.get("MM_TEAM")

bot = Bot(
	settings=Settings(
		MATTERMOST_URL = mm_url,
        MATTERMOST_PORT = 443,
		BOT_TOKEN = mm_token,
		BOT_TEAM = mm_team,
        SSL_VERIFY = True
	),  # Either specify your settings here or as environment variables.
	plugins=[GPTtext(), GPTimg(), Help()],  # Add your own plugins here.
)
bot.run()