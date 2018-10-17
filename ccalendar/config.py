import os

google_path = ""

if os.environ['ADM_JSON'] is not None:
        google_path = os.environ['ADM_JSON']
else:
    google_path = '/Users/StasMaster/Downloads/adm.json'
