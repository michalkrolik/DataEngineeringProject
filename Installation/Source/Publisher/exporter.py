import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_name = str(uuid.uuid4())
container_client = blob_service_client.create_container(container_name)

local_path = "./"
local_file_name = "forex.json"
upload_file_path = os.path.join(local_path, local_file_name)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
