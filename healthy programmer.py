from pygame import mixer
from datetime import datetime
from time import time
def loop_music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def recorn(string):
    with open("sample2.txt","a") as f:
        f.write(f"the time is {string }  {datetime.now()} \n")

if __name__ == '__main__':

    water_time= time()
    eye_time=time()
    exe_time=time()
    water_last=30*60
    eye_last=35*60
    exe_last=45*60

    while True:
        if time()-water_time > water_last:
            print("type grank to stop the music \n")
            loop_music("water.mp3","drank")
            recorn("the time of drinking water")
            water_time=time()

        if time()-eye_time > eye_last:
            print("type done to stop the music \n")
            loop_music("eye.mp3","done")
            recorn("the time of eye execrice")
            eye_time=time()

        if time()-exe_time > exe_last:
            print("type done to stop the music \n")
            loop_music("eye.mp3","done")
            recorn("the time of execrice physical ")
            exe_time=time()
