# -*- coding: utf-8 -*-

import xbmcgui
import xbmc
import xbmcaddon
import os
import time
import shutil

try:
    from xbmc import translatePath
except ImportError:
    from xbmcvfs import translatePath
    
addon_id = 'script.tools.box'
selfAddon = xbmcaddon.Addon(addon_id)
__version__ = selfAddon.getAddonInfo('version')

userPath = translatePath("special://userdata/addon_data/plugin.video.stream-cinema-2-release")
sourceFile = translatePath("%s/settings.xml" % userPath)
targetFile = translatePath("%s/settings-scc.xml" % userPath)
dialog = xbmcgui.Dialog()

choice = dialog.select("Nabídka", ["Vytvořit kopii souboru", "Opravit soubor"])

def Msg(message):
    xbmc.log(message, level=xbmc.LOGINFO)

def file_exists(file_path):
    return os.path.exists(file_path)
    
def repair():
    if choice == 0:
        if dialog.yesno("VAROVÁNÍ", "ZÁLOHUJTE JEN PLNĚ FUNKČNÍ NASTAVENÍ SCC DOPLŇKU.[CR]V opačném případě nebude záložní kopie pro případnou obnovu nastavení SCC použitelná.[CR]Chcete pokračovat?"):
            if file_exists(sourceFile):
                shutil.copy(sourceFile, targetFile)
                dialog.ok("Záloha vytvořena", "Záložní kopie nastavení byla uložena pod názvem settings-scc.xml.")
            else:
                dialog.ok("Chyba", "Zálohu nelze vytvořit.[CR]Soubor settings.xml nebyl nalezen.")
    elif choice == 1:
        if file_exists(targetFile):
            scc = "plugin.video.stream-cinema-2-release"
            xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"%s","enabled":false},"id":1}' % scc)
            Msg('[scc_repair] SCC is stopping')
            time.sleep(2)
            shutil.copy(targetFile, sourceFile)
            time.sleep(2)
            xbmc.executebuiltin("EnableAddon(plugin.video.stream-cinema-2-release)")
            Msg('[scc_repair] SCC enabled')
            dialog.ok("Soubor opraven", "Povolte doplněk SCC a restartujte Kodi.")
        else:
            dialog.ok("Chyba", "Soubor nelze opravit.[CR]Záložní kopie souboru nebyla nalezena")

if __name__ == '__main__':
    repair()
