# -*- coding: utf-8 -*-

import xbmc
import xbmcgui

dialog = xbmcgui.Dialog()
PLAYED = 'played_stream'
DOWNLOADED = 'downloaded_server'

def logInfo(text):
    xbmc.log('[Source Script] {}'.format(text), xbmc.LOGINFO)

def setProperty(variable, value, window=10000):
    xbmcgui.Window(window).setProperty(variable, value)

def clearProperty(variable, window=10000):
    xbmcgui.Window(window).clearProperty(variable)

def clearProperties(variables, window=10000):
    for variable in variables:
        clearProperty(variable, window)

logInfo('Start script')
logInfo("Script spuštěn.")
clearProperties({PLAYED, DOWNLOADED})

if xbmc.getCondVisibility('Player.HasVideo'):
    stream = xbmc.Player().getPlayingFile()
    xbmcgui.Window(10000).setProperty('PLAYED', stream)
    logInfo('Played stream: {}'.format(stream))
    parsedAddress = stream.split('/')
    xbmcgui.Window(10000).setProperty('DOWNLOADED',  parsedAddress[2])
    dialog.notification("Check Server Path", parsedAddress[2],  xbmcgui.NOTIFICATION_INFO, 2000)
    logInfo('Downloaded server: {}'.format(parsedAddress[2]))
    clearProperties({PLAYED, DOWNLOADED})


logInfo('Stop script')
