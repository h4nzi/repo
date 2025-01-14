# -*- coding: utf-8 -*-

import subprocess
import socket
import xbmcgui

dialog = xbmcgui.Dialog()

output = subprocess.check_output(['netstat', '-tulan']).decode('utf-8')
dns_names = []
# Rozdělíme výstup na řádky a iterujeme přes ně
for line in output.splitlines():
    parts = line.split()
    if len(parts) >= 6 and parts[4].startswith('185.201'):
        ip = parts[4].split(':')[0]
        try:
            hostname = socket.gethostbyaddr(ip)
            dns_names.append(f"{hostname[0]}")
        except socket.herror:
            pass
# Vytvoření textu z DNS jmen pro zobrazení v Kodi
dns_name = ', '.join(dns_names)
xbmcgui.Window(10000).setProperty('WS', dns_name)
dialog.notification("Check DNS Name", dns_name,  xbmcgui.NOTIFICATION_INFO, 2000)

#xbmcgui.Window(10000).GetProperty('CFileCache')
#prop = GetProperty('CFileCache')
#dialog.notification("Check", prop,  xbmcgui.NOTIFICATION_INFO, 2000)
# dialog.textviewer('DNS Jména', text_to_display)

# Získání aktuálního okna
# win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
# cfcv = win.getProperty('CFileCache::Process')
# dialog.notification("CFileCache", cfcv,  xbmcgui.NOTIFICATION_INFO, 2000)
# xbmcgui.Window(10000).setProperty('CFC', cfcv)
# text = xbmcgui.Window(10000).getProperty('VideoPlayer::OpenFile')
# xbmcgui.Window(10000).setProperty('CFC', text)
# dialog.notification("CFC", text,  xbmcgui.NOTIFICATION_INFO, 2000)

# Výpis hodnoty vlastnosti CFileCache
# print(f'Hodnota CFileCache: {cfile_cache_value}')





