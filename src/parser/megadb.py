import requests
import chompjs
import time
import sys

def fetch_mcdb():
    cheaters = []
    suspicious = []
    watched = []
    legit = []

    def convert_attrib(data):
        if data['color']['border'] == "#ff3300": # cheaters (red)
            cheaters.append(int(data['id']))
        elif data['color']['border'] == "#ffff00": # suspicious (yellow)
            suspicious.append(int(data['id']))
        elif data['color']['border'] == "#ffffff": # watched (white)
            watched.append(int(data['id']))
        elif data['color']['border'] == "#33ff00": # legit (green)
            legit.append(int(data['id']))
        elif data['color']['border'] == "#00ffff": # MSB (cyan)
            legit.append(int(data['id']))
        else:
            print(f"Unknown color encountered: {data['color']['border']}")
            sys.exit()

    run_time = time.time()
    site_data_str = requests.get("https://megascatterbomb.com/mcd").text

    data_start_point = "var nodes = new vis.DataSet("
    data_start = site_data_str.find(data_start_point)
    data_start += len(data_start_point)

    data_end_point = "var edges = new vis.DataSet(["
    data_end = site_data_str.find(data_end_point)

    site_data_str = site_data_str[data_start:data_end]
    site_data_str = site_data_str[:site_data_str.rfind(");")]

    site_data = chompjs.parse_js_object(site_data_str)

    try:
        for mark_data in site_data:
            convert_attrib(mark_data)
    except Exception as e:
        print(f"Error parsing MCDB: {e}")
        return {}

    print(f"MCDB Result: {len(cheaters)} Cheaters, {len(suspicious)} Suspicious, {len(watched)} Watched, {len(legit)} Legits, {len(cheaters) + len(suspicious) + len(watched) + len(legit)} Total in {round((time.time()) - run_time, 2)}s.")

    return {
        "MCDB - Cheaters": cheaters,
        "MCDB - Suspicious": suspicious,
        "MCDB - Watched": watched,
        "MCDB - Legit": legit
    }
