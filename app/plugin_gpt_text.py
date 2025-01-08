from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message

import g4f
from g4f.client import AsyncClient

# Словарь для хранения истории разговоров
conversation_history = {}

class GPTtext(Plugin):
	@listen_to('txt (.*)', direct_only=True)
	async def hi(self, message: Message, something):
		user_info = self.driver.users.get_user(user_id='me')
		user_id = user_info['id']
#        print (user_id)
		user_input = message.text

		if user_id not in conversation_history:
			conversation_history[user_id] = []

		conversation_history[user_id].append({"role": "user", "content": user_input})

		chat_history = conversation_history[user_id]

		try:
			response = await g4f.ChatCompletion.create_async(
				provider="Blackbox",
				model="gemini-pro",
				messages=chat_history,
			)
			chat_gpt_response = response
#            self.driver.create_post(channel_id=message.channel_id, message=chat_gpt_response)
		except Exception as e:
			print(f"{g4f.Provider.Blackbox.__name__}:", e)
			chat_gpt_response = "Извините, произошла ошибка."

		conversation_history[user_id].append({"role": "assistant", "content": chat_gpt_response})
		print(conversation_history)
		length = sum(len(message["content"]) for message in conversation_history[user_id])
		print(length)
		self.driver.create_post(channel_id=message.channel_id, message=chat_gpt_response)