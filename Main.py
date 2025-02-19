import zipfile as zx
import os
import sys
import logging as log

def Main():
    if(os.path.isfile("WUB.zip")):
        with zx.ZipFile(file="WUB.zip") as x:
            x.extractall(os.getcwd())
            print("Extracted!!!")
    else:
        log.critical("Failed to Found WUB.zip!!!")
        os._exit(443)

if __name__ == "__main__":
    Main()