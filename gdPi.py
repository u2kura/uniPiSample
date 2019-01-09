#!/usr/bin/env python
#coding: UTF-8

import commands
from datetime import datetime

time = datetime.now().isoformat()
gdrive = "./gdrive upload --parent 'ドライブのURLの最後の部分' "+ time + ".jpeg"

commands.getoutput("fswebcam pfarm.jpeg")
commands.getoutput("cp ./pfarm.jpeg ./" + time + ".jpeg")
commands.getoutput(gdrive)
commands.getoutput("rm " + time + ".jpeg")
