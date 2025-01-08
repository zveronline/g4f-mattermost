from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message

class Help(Plugin):
    @listen_to("help", direct_only=True)
    async def help(self, message: Message):
        self.driver.create_post(channel_id=message.channel_id, message='Это бот ChatGPT.\nНа выбор 4 модели для генерации изображений, пробуйте разные для генерации разных вариантов.\n\ntxt "пишем что-то" - задать текстовый запрос в нейросеть\n\nimg "пишем что-то на английском" - генерация картинки (модель sdxl)\nimg1 "пишем что-то на английском" - генерация картинки (модель sd-3)\nimg2 "пишем что-то на английском" - генерация картинки (модель flux)\nimg3 "пишем что-то на английском" - генерация картинки (модель playground-v2.5)')