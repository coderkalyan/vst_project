from schedule_saver import DBManager, Schedule
from video import Video


def i_need_help(hours, minutes, seconds, name, flags, length, switch):
    with DBManager("schedules.vstx") as conn:
        schedule = Schedule(conn)
        # schedule.update(
        #     Video(
        #         1,
        #         2,
        #         3,
        #         "help",
        #         ["--fullscreen"],
        #         "1:00",
        #         False, 1))
        schedlist = schedule.list_all()
        print(schedlist[0].filename)
        print(schedlist)
        schedule.clear()
        # schedule.insert(
        # Video(hours,
        #       minutes,
        #       seconds,
        #       name,
        #       flags,
        #       length,
        #       switch))
        print("this function is returning now, ya stupid")
if __name__ == "__main__":
    i_need_help(1,2,3,"/home/bbworld/git/vst_project/title.mp4",["--fullscreen"],"1:00",False)