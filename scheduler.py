import record

import shutil

diskLabel = '/'

def Schedule():
    total, used, free = shutil.disk_usage(diskLabel)
    print(free)
    
    record.RecStart()

    pass
