#!/usr/bin/python3.4
import os, xbmc, xbmcvfs, xbmcaddon, xbmc, xbmcgui
from zipfile import ZipFile

jreZipSrc = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/lib/j2re-image.zip')
jreZipInstall = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image.zip")
libbluray = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image/libbluray.jar")
java_home = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/j2re-image/")
jreInstall = xbmcvfs.translatePath("special://xbmcbin/../../../cache/lib/")

profileDir = xbmcvfs.translatePath("special://home/userdata/decoderfilter.xml")
keymapsDir = xbmcvfs.translatePath("special://home/userdata/keymaps/keyboard.xml")
keyboardProfile = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/keyboard.xml')
decoderProfile = os.path.join(xbmcaddon.Addon().getAddonInfo('path'), 'resources/decoderfilter.xml')

if xbmcvfs.exists(libbluray):
    print("Java Runtime is already installed.")
else:
    if xbmcvfs.exists(jreZipSrc):
        xbmcvfs.copy(jreZipSrc, jreZipInstall)
        zip = ZipFile(jreZipInstall)
        zip.extractall(jreInstall)
        zip.close()

        askKeymap = xbmcgui.Dialog().yesno("Install the KEYBOARD profile?", "Installing the keyboard profile makes easier to control Bluray menus using remotes with fewer keys", yeslabel="Yes, overwrite my current KEYBOARD profile", nolabel="No, do not alter my KEYBOARD profile")
        if askKeymap:
            xbmcvfs.copy(keyboardProfile, keymapsDir)

        askDecoder = xbmcgui.Dialog().yesno("Install the DECODER profile?", "Installing the decoder profile fixes Bluray menus with background video", yeslabel="Yes, overwrite my DECODER profile", nolabel="No, do not alter my DECODER profile")
        if askDecoder:
            xbmcvfs.copy(decoderProfile, profileDir)

    else:
        print("Could not find j2re-image.zip")


for path, subdirs, files in os.walk(java_home):
    for name in files:
        print(os.path.join(path, name))
