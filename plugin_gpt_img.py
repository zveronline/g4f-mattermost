from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message

import g4f
from g4f.client import AsyncClient

# Словарь для хранения истории разговоров

class GPTimg(Plugin):
    @listen_to('img (.*)', direct_only=True)
    async def model_sdxl(self, message: Message, something):
        try:
            client = AsyncClient()
            response = await client.images.generate(
                model="sdxl",
                prompt=message.text,
                response_format="url"
                # Add any other necessary parameters
            )
            image_url = response.data[0].url
            print(f"Generated image URL: {image_url}")
            self.driver.create_post(channel_id=message.channel_id, message=image_url)
        except Exception as e:
            print(f"{g4f.Provider.GeekGpt.__name__}:", e)
            msg = "Что-то пошло не так. Попробуйте еще раз."
            self.driver.create_post(channel_id=message.channel_id, message=msg)

    @listen_to('img1 (.*)', direct_only=True)
    async def model_sd3(self, message: Message, something):
        try:
            client = AsyncClient()
            response = await client.images.generate(
                model="sd-3",
                prompt=message.text,
                response_format="url"
                # Add any other necessary parameters
            )
            image_url = response.data[0].url
            print(f"Generated image URL: {image_url}")
            self.driver.create_post(channel_id=message.channel_id, message=image_url)
        except Exception as e:
            print(f"{g4f.Provider.GeekGpt.__name__}:", e)
            msg = "Что-то пошло не так. Попробуйте еще раз."
            self.driver.create_post(channel_id=message.channel_id, message=msg)

    @listen_to('img2 (.*)', direct_only=True)
    async def model_flux(self, message: Message, something):
        try:
            client = AsyncClient()
            response = await client.images.generate(
                model="flux",
                prompt=message.text,
                response_format="url"
                # Add any other necessary parameters
            )
            image_url = response.data[0].url
            print(f"Generated image URL: {image_url}")
            self.driver.create_post(channel_id=message.channel_id, message=image_url)
        except Exception as e:
            print(f"{g4f.Provider.GeekGpt.__name__}:", e)
            msg = "Что-то пошло не так. Попробуйте еще раз."
            self.driver.create_post(channel_id=message.channel_id, message=msg)
			
	@listen_to('img3 (.*)', direct_only=True)
    async def model_playground2_5(self, message: Message, something):
        try:
            client = AsyncClient()
            response = await client.images.generate(
                model="playground-v2.5",
                prompt=message.text,
                response_format="url"
                # Add any other necessary parameters
            )
            image_url = response.data[0].url
            print(f"Generated image URL: {image_url}")
            self.driver.create_post(channel_id=message.channel_id, message=image_url)
        except Exception as e:
            print(f"{g4f.Provider.GeekGpt.__name__}:", e)
            msg = "Что-то пошло не так. Попробуйте еще раз."
            self.driver.create_post(channel_id=message.channel_id, message=msg)