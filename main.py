import cv2
import datetime as dt
import os

cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("resolution: {0} x {1}".format(width, height))
codec = 'x264' #'HEVC' #h264
fourcc = cv2.VideoWriter_fourcc(*codec)

def Start():
    start_date = dt.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    mon = dt.datetime.now().strftime("%Y-%m")
    video_dir = os.path.dirname(os.path.realpath(__file__)) + '/records/' + mon +"/" 
    if os.path.isdir(video_dir) == False :
        os.makedirs(video_dir)
    file_fullpath = video_dir + start_date + '.mkv'
    writer = cv2.VideoWriter(file_fullpath, fourcc, 24, (int(width), int(height)))
    file_size = 0
    day = dt.datetime.now().strftime("%d")
    dayint = int(day)
    while cap.isOpened():
        if (int(dt.datetime.now().strftime("%d")) - dayint) > 0:
            break;
        success, frame = cap.read()
        if success:
            file_size += frame.size
            x = writer.write(frame)  # 프레임 저장
            cv2.imshow('Video Window', frame)
            # q 를 누르면 종료
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                print(file_size)
                break
        else:
            break
    pass

 
cap.release()
writer.release()  # 저장 종료
cv2.destroyAllWindows()