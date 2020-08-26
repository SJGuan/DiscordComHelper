import time
song_file = open("./songs.txt","r")
commands = song_file.readlines()
song_file.close()
random.shuffle(commands)
output_songs()

def output_songs(mins = None, commands = commands):
    #each song defaut 3 mins for ease
    import random
    from pynput.keyboard import Key, Controller
    import time
    keyboard = Controller()
    time.sleep(5)
    if mins == None:
        running_num = len(commands)
        counting = 1
        for i in commands:
            keyboard.type(i)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            str = "Running~~: " +countting + "/"+running_num
            counting += 1
            keyboard.type(str)
        else:
            keyboard.type("Done! This is Snugs' Radio 24/7 ~~")
    else:
        songs_num = mins/3
        for i in commands[:songs_num]:
            keyboard.type(i)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(3)
            str = "Running~~: " +countting + "/"+running_num
            counting += 1
            keyboard.type(str)
        else:
            keyboard.type("Done! This is Snugs' Radio 24/7 ~~")
