
import os
import time
import xbmc
import xbmcgui

puls = (":")
zero = (" ")
monitor = xbmc.Monitor()

def Msg(msg):
    xbmc.log(msg,level=xbmc.LOGINFO)

if __name__ == '__main__':
    while not monitor.abortRequested():
        xbmcgui.Window(10000).setProperty('TikTak', puls)
        time.sleep(1)
        xbmcgui.Window(10000).setProperty('TikTak', zero)
        if monitor.waitForAbort(1):
            Msg('~Confluence TikTak~ Service Abort Called')
            break
            