import os
import subprocess

# this is a file to provide functionality to play a video file
# should work with all media formats as long as the player being used
# supports the format
# the player also needs to have a functionality for
# command line usage

# constants for different players
PLAYER_VLC = 1
PLAYER_CVLC = 2

# paths to the different players - for now, we don't put full path,
# assuming that the program is in the user's PATH
PATH_VLC = "vlc"
PATH_CVLC = "cvlc"


def play(player, file, args):
    if player == PLAYER_VLC:
        # os.system(PATH_VLC + " " + " ".join(args) + " " + file)
        p = subprocess.Popen([PATH_VLC, " ".join(args), file])
    if player == PLAYER_CVLC:
        os.system(PATH_CVLC + " " + " ".join(args) + " " + file)


def stop():
    """
    Crude stop method - just runs killall vlc
    """
    os.system("killall " + PATH_VLC)


def main():
    play(PLAYER_CVLC, "video_1.mp4", ["--fullscreen"])


if __name__ == "__main__":
    main()
