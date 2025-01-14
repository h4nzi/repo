import json
import requests
import xbmc

# Nastavení adresy Kodi JSON-RPC API
KODI_URL = "http://localhost:8080/jsonrpc"  # Změňte na správnou adresu a port vašeho Kodi

xbmc.log("[Stream type] Script spuštěn.", level=xbmc.LOGINFO)

# Funkce pro volání Kodi JSON-RPC API
def call_kodi_api(method, params=None):
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params if params else {},
        "id": 1
    }
    try:
        response = requests.post(KODI_URL, headers=headers, data=json.dumps(payload))
        xbmc.log(f"[Stream type] Response: {response}", level=xbmc.LOGINFO)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        xbmc.log(f"Chyba při komunikaci s Kodi: {e}", level=xbmc.LOGINFO)
        return None

# Získání aktuálně přehrávaného média
def get_current_stream_type():
    # Zjistíme, zda je aktivní nějaký přehrávač
    active_players = call_kodi_api("Player.GetActivePlayers")
    xbmc.log(f"[Stream type] Active Player: {active_players}", level=xbmc.LOGINFO)
    if not active_players or "result" not in active_players or not active_players["result"]:
        xbmc.log("Žádný přehrávač není aktivní.", level=xbmc.LOGINFO)
        return

    player_id = active_players["result"][0]["playerid"]

    # Získáme podrobnosti o aktuálně přehrávaném médiu
    item_details = call_kodi_api("Player.GetItem", {
        "playerid": player_id,
        "properties": ["file", "streamdetails"]
    })

    if not item_details or "result" not in item_details:
        xbmc.log("[Stream type] Nepodařilo se získat podrobnosti o aktuálně přehrávaném médiu.", level=xbmc.LOGINFO)
        return

    item = item_details["result"].get("item", {})
    file_path = item.get("file", "")
    stream_details = item.get("streamdetails", {})

    # Výpis informací
    xbmc.log("[Stream type] \n--- Informace o aktuálním přehrávání ---", level=xbmc.LOGINFO)
    xbmc.log(f"[Stream type] Cesta k souboru/URL: {file_path}", level=xbmc.LOGINFO)

    if "video" in stream_details and stream_details["video"]:
        xbmc.log("[Stream type] Typ: Video stream", level=xbmc.LOGINFO)
    elif "audio" in stream_details and stream_details["audio"]:
        xbmc.log("[Stream type] Typ: Audio stream", level=xbmc.LOGINFO)
    else:
        xbmc.log("[Stream type]Typ streamu nebyl rozpoznán.", level=xbmc.LOGINFO)

    if "hls" in file_path.lower():
        xbmc.log("[Stream type] Formát: HLS", level=xbmc.LOGINFO)
    elif "mpd" in file_path.lower():
        xbmc.log("[Stream type]Formát: MPEG-DASH", level=xbmc.LOGINFO)
    elif file_path.lower().startswith("rtmp"):
        xbmc.log("[Stream type]Formát: RTMP", level=xbmc.LOGINFO)
    else:
        xbmc.log("[Stream type]Formát není specifikovaný nebo není podporovaný.", level=xbmc.LOGINFO)

# Spuštění skriptu
if __name__ == "__main__":
    get_current_stream_type()
