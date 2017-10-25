import datetime
import time
import threading
import player_api


class Video:
    def __init__(self, hour: int, minute: int, second: int, name: str, flags: list):
        # self.thread = threading.Thread(name=name, target=self.play_at_time())
        self.hour = hour
        self.minute = minute
        self.second = second
        self.filename = name
        self.flags = flags
        print(self.hour, self.minute, self.second)

    def set_play_time(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def start_clock(self):
        """
        starts a new thread which plays this video at the time requested
        the time to play can change during this time as long as
        a) the time is after current time
        b) the video has NOT started playing yet
        """
        # self.thread.start()
        self.play_at_time()

    def play_at_time(self):
        while datetime.datetime.now().time() < datetime.time(self.hour, self.minute, self.second):
            time.sleep(0.05)
        self.play()

    def play(self, player=player_api.PLAYER_VLC):
        player_api.play(player, self.filename, self.flags)
