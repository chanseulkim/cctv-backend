
conf_file = "/etc/motion/motion.conf"
newlines = ""
with open(conf_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if "movie_filename" in line:
            newlines += "movie_filename %Y-%m-%d-%H-%M-%S\n"
        elif "target_dir" in line:
            newlines += "target_dir /home/motion_records\n"
        else:
            newlines += line

with open(conf_file,'w') as f:
    f.write(newlines)