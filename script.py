#!/usr/bin/python3

import os

os.system('find /home/user -type f -mtime +2 ! -name "*.rar" -exec rar u /home/user/arc_log.rar \;')
os.system('find /home/user -type f -mtime +2 ! -name "*.rar" -exec rm {} \;')