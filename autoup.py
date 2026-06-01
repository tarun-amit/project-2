import requests
from google_play_scraper import app

import requests
from google_play_scraper import app

def AuToUpDaTE():
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    try:
        result = app('com.dts.freefireth', lang="fr", country='fr')
        version = result['version']
    except:
        version = "1.111.1"
        
    try:
        r = requests.get(
            f'https://bdversion.ggbluefox.com/live/ver.php?version={version}&lang=ar&device=android&channel=android&appstore=googleplay&region=ME&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993',
            verify=False
        ).json()
        url = r['server_url']
        ob = r['latest_release_version']
    except:
        url = "https://client.us.freefiremobile.com/"
        ob = "OB53"
        
    return url, ob, version