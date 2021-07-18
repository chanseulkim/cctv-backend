import cv2
import datetime as dt
import os
from pathlib import Path

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("resolution: {0} x {1}".format(width, height))
codec = 'x264' #'HEVC' #h264
fourcc = cv2.VideoWriter_fourcc(*codec)

def RecStart():
    print("RecStart")
    start_date = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    #os.path.dirname(os.path.realpath(__file__)) #현재경로
    video_dir = str(Path.home()) + '/records/' + dt.datetime.now().strftime("%Y-%m") +"/" 
    if os.path.isdir(video_dir) == False :
        os.makedirs(video_dir)
    file_fullpath = video_dir + start_date + '.mkv'
    writer = cv2.VideoWriter(file_fullpath, fourcc, 24, (int(width), int(height)))
    startday = dt.datetime.now().strftime("%d")
    while cap.isOpened():
        if (int(dt.datetime.now().strftime("%d")) != int(startday)) :
            break
        success, frame = cap.read()
        if success:
            x = writer.write(frame)  # 프레임 저장
            cv2.imshow('Video Window', frame)
            # q 를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                exit(0)
        else:
            break
    pass

while True :
    RecStart()
    pass
 
cap.release()
writer.release()  # 저장 종료
cv2.destroyAllWindows()