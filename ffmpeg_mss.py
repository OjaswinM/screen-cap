import time
from mss import mss
import os

def screencap(filename):
    sct.shot(output = filename)

sct = mss()

print("Enter the number of seconds to record for: ")
sec = int(input("> "))

print("Press any key to start: ")
input(">")

os.system('mkdir temp')
i = 1

tEnd = time.time() + sec
print("Recording started: ")
while(time.time() < tEnd):
    out = "temp/out" + str(i) + ".png"
    screencap(out)
    i=i+1
print("Saving video...")
os.system('ffmpeg -y -i temp/out%01d.png output.mp4')
os.system('rm -r temp')
