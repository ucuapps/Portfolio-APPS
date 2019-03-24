import os

google_path = ""

try:
    google_path = os.environ['ADM_JSON']
except:
    google_path = '/Users/StasMaster/Downloads/adm.json'
