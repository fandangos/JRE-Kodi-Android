#!/usr/bin/python3.4
import os, sys, xbmc, time, stat, xbmcvfs, xbmcaddon
from zipfile import ZipFile
import shutil

src = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/lib/j2re-image.zip')
loc = xbmcvfs.translatePath("special://xbmcbin/j2re-image.zip")
loc2 = xbmcvfs.translatePath("special://xbmcbin/j2re-image/")
loc3 = xbmcvfs.translatePath("special://xbmcbin/")

if xbmcvfs.exists(loc2):
    shutil.rmtree(loc2)
    os.remove(loc)

if xbmcvfs.exists(src):
    xbmcvfs.copy(src, loc)

zip = ZipFile(loc)
zip.extractall(loc3)
zip.close()


for path, subdirs, files in os.walk(loc2):
    for name in files:
        print(os.path.join(path, name))

