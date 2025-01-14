#!/usr/bin/env python3

import subprocess
import re
import xbmcgui

try:
    from xbmc import translatePath
except ImportError:
    from xbmcvfs import translatePath

# Definuje cestu k souboru pomocí translatePath
SP = translatePath('special://profile/addon_data/plugin.video.stream-cinema-2-release/settings.xml')

# Najde a extrahuje hodnotu vip_check
vip_check = subprocess.check_output(["grep", "last_vip_check", SP])
vip_check = re.search(r'>\s*(\d+)\.', vip_check.decode("utf-8"))
if vip_check:
    vip_check = vip_check.group(1)
    xbmcgui.Window(10000).setProperty('vip_check', vip_check)

# Najde a extrahuje hodnoty vip_duration a vip_days
vip_duration = subprocess.check_output(["grep", "provider.vip_duration", SP])
vip_duration = re.search(r'>\s*(.*?)\s*<', vip_duration.decode("utf-8"))
if vip_duration:
    xbmcgui.Dialog().notification('VIP Days Webshare', 'Kontrola zbývajícich dní předplatného', xbmcgui.NOTIFICATION_INFO, 2000, sound=True)
    vip_duration = vip_duration.group(1)
    vip_days = re.search(r'\(Dny: (\d+)\)', vip_duration).group(1)
    color = ""
    if int(vip_days) > 14:
        color = "blue"
    elif int(vip_days) > 7:
        color = "yellow"
    else:
        color = "red"
    xbmcgui.Window(10000).setProperty('vip_days', f'[COLOR {color}]{vip_days}[/COLOR]')

# Najde a extrahuje hodnotu username
username = subprocess.check_output(["grep", "provider.username", SP])
username = re.search(r'>\s*(.*?)\s*<', username.decode("utf-8"))
if username:
    username = username.group(1)
    xbmcgui.Window(10000).setProperty('username', username)




