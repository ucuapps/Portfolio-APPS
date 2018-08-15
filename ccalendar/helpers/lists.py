from google.oauth2 import service_account
from dateutil.parser import parse
import googleapiclient.discovery


def calendar_list(buildingId):
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.resource.calendar']
    SERVICE_ACCOUNT_FILE = '/Users/StasMaster/Downloads/adm.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    # registering api
    # credentials.create_delegated("zavaliy@ucu.edu.ua")
    credentials = credentials.with_subject('zavaliy@ucu.edu.ua')
    resourceApi = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    result = resourceApi.resources().calendars().list(customer="C01ak6gy3", query=str("buildingId="+buildingId)).execute()
    # result = filter(lambda x: x.get("buildingId") == buildingId, result.get("items"))
    return result.get("items")