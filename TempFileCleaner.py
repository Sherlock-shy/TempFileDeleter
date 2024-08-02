import os
import shutil

recPath = "your path to %temp%"

if os.path.exists(recPath):
    for file in os.listdir(recPath):
        if os.path.exists(os.path.join(recPath, file)):
            os.remove(os.path.join(recPath, file))
