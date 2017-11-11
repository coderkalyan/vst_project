from schedule_saver import DBManager, Schedule
from video import Video

def i_need_help():
    with DBManager("schedules.vstx") as conn:
        schedule = Schedule(conn)
        schedlist = schedule.list_all()
        for row in schedlist:
            print(row.minute, "please help me")
        # schedule.insert(
        # Video(1,
        #       2,
        #       3,
        #       "/home/bbworld/git/vst_project/title.mp4",
        #       ["--fullscreen"],
        #       "1:00",
        #       False))