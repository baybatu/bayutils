#!/usr/bin/python
# -*- coding: utf-8 -*-

# 08.08.11 / Batuhan Bayrakçı - batuhanbayrakci@gmail.com

# A converter for module files to mp3
# Usage from terminal:

# $ python mod2mp3.py [MODULE FILE] [TARGET FOLDER]

import subprocess
import os
import sys
import shutil

TOOLS = ["xmp","lame"]

for tool in TOOLS:
    ctrl_value = subprocess.call("which %s > /dev/null" % (tool), shell=True)
    if ctrl_value != 0:
        print "%s tool has not been installed. Please install and try again." % (tool)
        sys.exit()

if len(sys.argv) == 3:
    full_filename   = sys.argv[1]
    target_path     = sys.argv[2]

elif len(sys.argv) == 1:
    print "mod2mp3 tool converts your module sound files to mp3 file"
    print "Usage: python mod2mp3.py MODULE_FILE TARGET_PATH"
    sys.exit()

else:
    print "Missing parameters:"
    print "Usage: python mod2mp3.py MODULE_FILE TARGET_PATH"
    sys.exit()


filename        = os.path.splitext(full_filename)[0]

if os.path.exists("%s.wav" % (filename)):
    os.remove("%s.wav" % (filename))

mod2wav_command = "xmp '%s' -o '%s'.wav" % (full_filename, filename)
wav2mp3_command = "lame -V0 '%s'.wav '%s'.mp3" % (filename, filename)

command = mod2wav_command + " && " + wav2mp3_command  

# proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,)
proc = subprocess.call(command, shell = True)

try:
    os.remove("%s.wav" % (filename))
    print "%s.wav file removed" % (filename)
except:
    print "%s.wav file couldn't remove" % (filename)

shutil.move("%s.mp3" % filename, target_path)
print "CONVERTION PROCESS COMPLETED SUCCESSFULLY"
