from channels.generic.websocket import AsyncWebsocketConsumer
import json

from marko_pollo.utils import gen_marko_polo


class MarkoPoloConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            print(type(data))
            print(data)
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({'error': 'Отправьте данные в JSON формате'}, ensure_ascii=False))
            return

        if not isinstance(data, dict):
            await self.send(text_data=json.dumps(
                {'Неправильный запрос. Пример запроса:': {'command': 'mp_one', 'data': {'mp_one': 1}}},
                ensure_ascii=False))
            return

        elif "command" not in data:
            await self.send(text_data=json.dumps({'error': 'Неправильный формат данных'}, ensure_ascii=False))
            return

        command = data["command"]
        if command == 'mp_one':
            if "mp_one" in data["data"]:
                num = data["data"]["mp_one"]
                response = gen_marko_polo.generate_one(num)
            else:
                response = "Отправьте необходимые данные согласно образцу:'{'command': 'mp_one', 'data': {'mp_one': '<number>'}}'"

        elif command == 'mp_list':
            if "mp_list" in data["data"]:
                arr = data["data"]["mp_list"]
                response = gen_marko_polo.generate_list(arr)
            else:
                response = "Отправьте необходимые данные согласно образцу:'{'command': 'mp_list', 'data': {'mp_list': ['<number_1>, <number_2>, ...']}}'"

        elif command == 'mp_range':
            if "mp_start" and "mp_end" in data["data"]:
                start = data["data"]["mp_start"]
                end = data["data"]["mp_end"]
                response = gen_marko_polo.generate_range(start, end)
            else:
                response = "Отправьте необходимые данные согласно образцу:'{'command': 'mp_range', 'data': {'mp_start': '<number_start>, 'mp_end': <number_end>}}'"

        else:
            response = "Неизвестная команда"

        await self.send(text_data=json.dumps({'response': response}, ensure_ascii=False))
