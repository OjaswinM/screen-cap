import time
from mss import mss
import os

sct = mss()

def screencap(filename):
    sct.shot(output = filename)

os.system('mkdir temp')
i = 1

tEnd = time.time() + 10
print("Recording started: ")
while(time.time() < tEnd):
    out = "temp/out" + str(i) + ".png"
    screencap(out)
    i=i+1
print("Saving video...")
os.system('ffmpeg -y -i temp/out%01d.png output.mp4')
os.system('rm -r temp')
