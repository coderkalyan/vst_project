import threading
import player_api
import time
import datetime
from video import Video

# this is a file to provide functionality to schedule, override, and cancel
# playback of videos

# by default, we are using cvlc for playing
player = player_api.PLAYER_CVLC


isOverride = False


def override():
    global isOverride
    isOverride = True


def set_player(new_player):
    global player
    player = new_player


queue = []


def enqueue(video: Video) -> None:
    """
    Enqueues a video to play AFTER COMPLETION of the previous video
    :param video: Video object to play.
    """
    queue.append(video)


def start_queue(start_time: datetime.datetime = datetime.datetime.now()
                + datetime.timedelta(seconds=1)) -> None:
    """
    Starts video queue playback at a certain time
    :param start_time: datetime object, start time for playing - we aren't using date part
    Default value for start_time is 1 second from function call
    """

    global isOverride

    # we want to wait to load video until current time is start_time,
    # but we want to be able to override that
    while not isOverride and datetime.datetime.now().time() != start_time.time():
        time.sleep(0.05)

    isOverride = False
    # load_first()


if __name__ == '__main__':
    enqueue(Video(17, 39, 0, "video_1.mp4", ["--fullscreen"]))
    t = threading.Thread(target=start_queue)
    t.start()
    override()
