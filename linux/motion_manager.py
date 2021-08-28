# records: /home/motion_records
# configs: /etc/motion

from os import listdir
from os.path import isfile, join, isdir
import os

import time
import shutil

import datetime as dt
from datetime import date, timedelta

record_path = "/home/motion_records"
file_ext = ".mkv"
thumnail_codec = "png"
# 보관 기간 기본 2주
maxstore_days = 14
exclude_hms_cnt = 6

def remove_ext(file):
    extpos = file.find(file_ext)
    return file[0: extpos]

def delete_old_files(filename):
    filename_fullpath = join(record_path, filename)
    if isfile(filename_fullpath): 
        extpos = filename.find(file_ext)
        filename = filename[0: extpos]
        filename = filename.replace("-", "")
        filename = filename[0: len(filename) - exclude_hms_cnt]
    elif isdir(filename_fullpath):
        filename = filename.replace("-", "")

    fromdate = str(date.today() - timedelta(days = maxstore_days))
    fromdate = fromdate.replace("-", "")
    
    #expired
    filedate = int(filename)
    if (filedate - int(fromdate)) <= 0 :
        if isdir(filename_fullpath):
            os.rmdir(filename_fullpath)
            return True
        else:
            os.remove(filename_fullpath)
            return True
    return False

def move_yesterday_records(file, target_date, target_dir):
    if target_date in file :
        yesterday_rec = join(record_path, file)
        if isfile(yesterday_rec):
            cmd = "ffmpeg -i "
            cmd += yesterday_rec + " "
            cmd += "-ss 000:00:01 "
            cmd += "-vcodec " + thumnail_codec + " "
            cmd += target_dir + "/" + remove_ext(file) + "." + thumnail_codec
            os.system(cmd)
            shutil.move(yesterday_rec, target_dir)
    pass

def Work():
    yesterday = date.today() - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    today_date = dt.datetime.now().strftime("%Y-%m-%d")
    #yesterday_date = yesterday.strftime("%Y%m%d")
    #today_date = dt.datetime.now().strftime("%Y%m%d")
    yesterday_dir = join(record_path, yesterday_date)

    if os.path.exists(yesterday_dir) == False:
        os.makedirs(yesterday_dir)

    for file in listdir(record_path):
        if delete_old_files(file):
            continue
        move_yesterday_records(file, yesterday_date, yesterday_dir)
    pass

last_date = date.today()

while True :
    #TODO: 00:00 분 기준으로 실행하도록 변경하기 하루단위
    #지금은 매번 체크중.
    Work()
    time.sleep(60)
    continue
    if last_date == (date.today() - timedelta(days=1)):
        Work()
        last_date = (date.today() - timedelta(days=1))
