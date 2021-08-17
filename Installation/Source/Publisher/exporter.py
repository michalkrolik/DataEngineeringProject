import os, uuid
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

CONFIG_LOCATION='./'
CONFIG = json.loads(open(str(CONFIG_LOCATION+'config.json')).read())
AZURE_STORAGE_CONNECTION_STRING    = CONFIG['secrets']['AZURE_STORAGE_CONNECTION_STRING']

os.environ['AZURE_STORAGE_CONNECTION_STRING'] = AZURE_STORAGE_CONNECTION_STRING

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#container_name = str(uuid.uuid4())
container_name = str(datetime.datetime.today().strftime('%Y%m%d'))
container_client = blob_service_client.create_container(container_name)

local_path = "/app/"
local_file_name = "forex.json"
upload_file_path = os.path.join(local_path, local_file_name)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)

