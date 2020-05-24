from telebot import TeleBot


class TelegramBotWrapper:

    def __init__(self, token) -> None:
        self.chat_ids = set()
        self.bot = TeleBot(token)

        for handler_dict in self.__build_handler_dicts():
            self.bot.add_message_handler(handler_dict)

    def __build_handler_dicts(self):
        defaults = {
            'commands': None,
            'regexp': None,
            'func': None,
            'content_types': ['text']
        }
        handlers_info_list = [
            {'handler': self._subscribe, 'commands': ['subscribe']},
            {'handler': self._unsubscribe, 'commands': ['unsubscribe']}
        ]
        handler_dicts = []

        for h_info in handlers_info_list:
            handler_dicts.append(
                TeleBot._build_handler_dict(h_info['handler'], **{**defaults, 'commands': h_info['commands']})
            )
        return handler_dicts

    def _subscribe(self, message):
        self.chat_ids.add(message.chat.id)
        self.bot.send_message(message.chat.id, 'Successfully subscribed on updates.')

    def _unsubscribe(self, message):
        self.chat_ids.remove(message.chat.id)
        self.bot.send_message(message.chat.id, 'Successfully unsubscribed from updates.')

    def start(self):
        self.bot.polling()

    def stop(self):
        self.bot.stop_bot()

    def notify(self, message):
        for chat_id in self.chat_ids:
            self.bot.send_message(chat_id, message)
