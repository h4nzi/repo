
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
        xbmcgui.Window(10000).setProperty('Mrk', puls)
        time.sleep(1)
        xbmcgui.Window(10000).setProperty('Mrk', zero)
        if monitor.waitForAbort(1):
            Msg('~Confluence Mrk~ Service Abort Called')
            break
            