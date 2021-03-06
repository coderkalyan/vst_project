import datetime
import time
import threading
import player_api


class Video:
    def __init__(self, hour: int, minute: int, second: int, name: str, flags: list, length: str, auto_schedule: bool, id: int = None):
        print (hour, "KILL MEEE")
        self.killswitch = False
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        self.filename = name
        self.flags = flags
        self.length = length
        self.id = id
        print(flags, self.flags, "flagz")
        if auto_schedule:
            print("YES MOM I AM DOING HOMEWORK")
            t = threading.Thread(target=self.play_at_time)
            t.start()

    def __str__(self):
        if self.hour == -1:
            return "{} playing manually".format(self.filename)
        else:
            return "{} will play at {}:{}:{}".format(self.filename, self.hour, self.minute,
                                                     self.second)

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
        pass

    def play_at_time(self):
        try:
            if datetime.datetime.now().time() > datetime.time(self.hour, self.minute, self.second):
                return

            while datetime.datetime.now().time() <= datetime.time(self.hour, self.minute,
                                                                  self.second):
                if self.killswitch == True:
                    print("return")
                    return
                
                time.sleep(0.05)
            print("It's time")
            self.play()
        except Exception as e:
            print(e, "exception")
            pass

    @staticmethod
    def num_columns():
        return 3

    def play(self, player=player_api.PLAYER_FFPLAY):
        print("play() called")
        print(self.filename, self.flags, "YYEEE")
        player_api.play(player, self.filename, self.flags)
    
    def terminate(self):
        print("Flipping killswitch")
        self.killswitch = True
