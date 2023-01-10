#!/usr/bin/python3.4
import os, sys, xbmc, time, stat, xbmcvfs, xbmcaddon
from zipfile import ZipFile
import shutil

src = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/lib/j2re-image.zip')
loc = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image.zip")
libbluray = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image/libbluray.jar")
loc2 = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image/")
loc3 = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/")


if xbmcvfs.exists(libbluray):
    print("Java Runtime is already installed.")
else:
    if xbmcvfs.exists(src):
        xbmcvfs.copy(src, loc)
        zip = ZipFile(loc)
        zip.extractall(loc3)
        zip.close()
    else:
        print("Could not find j2re-image.zip")


for path, subdirs, files in os.walk(loc2):
    for name in files:
        print(os.path.join(path, name))
