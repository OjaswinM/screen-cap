import pyautogui
import numpy as np
import cv2

frame = np.array(pyautogui.screenshot())
height,width, channel = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (width,height))
for i in range(60):
    pyautogui.screenshot("hello.png")
    frame = cv2.imread("hello.png")
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # cv2.imshow('hi',frame)
    out.write(frame)
    # if(cv2.waitKey(1) & 0xFF == ord('q')):
    #     cv2.destroyAllWindows()
    #     break

out.release()
