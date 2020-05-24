import threading
import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class Handler(PatternMatchingEventHandler):

    def __init__(self, filepath, bot, patterns=None, ignore_patterns=None, ignore_directories=False,
                 case_sensitive=False):
        self.filepath = filepath
        self.bot = bot
        super().__init__(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_any_event(self, event):
        if not self.filepath.match(event.src_path):
            return
        if event.event_type in ['created', 'modified']:
            self.bot.notify(self.filepath.read_text())


class Watcher:
    def __init__(self, filepath, bot, **kwargs):
        self.observer = Observer()
        self.filepath = filepath
        self.bot = bot

        self.event_handler = Handler(filepath, bot, **kwargs)

    def run(self):
        bot_thread = threading.Thread(target=self.bot.start, daemon=True)
        watch_dir_path = str(self.filepath.parents[0].resolve())

        self.observer.schedule(self.event_handler, watch_dir_path, recursive=False)
        self.observer.start()
        bot_thread.start()

        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print('Stopped')

        self.observer.join()
