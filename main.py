import sys
from argparse import ArgumentParser
from pathlib import Path

from file_watcher import Watcher
from telegram_bot import TelegramBotWrapper


def create_args_parser():
    args_parser = ArgumentParser()
    args_parser.add_argument('filepath', nargs='?', type=Path)
    args_parser.add_argument('bot_token', nargs='?', type=str)

    return args_parser


def main(filepath, token):
    bot = TelegramBotWrapper(token)
    watcher = Watcher(filepath, bot)

    watcher.run()


if __name__ == '__main__':
    parser = create_args_parser()
    args = parser.parse_args(sys.argv[1:])

    if getattr(args, 'filepath') and getattr(args, 'bot_token'):
        main(args.filepath, args.bot_token)
    else:
        print('Error! Specify filepath and Telegram Bot token.')
