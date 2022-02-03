import os
from google.cloud import storage

#set up variable environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='/Users/nicole/Downloads/alert-cedar-340206-4a305968edd9.json'

# [START storage_download_file]
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob."""

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Blob {} downloaded to file path {}. successfully ".format(
            source_blob_name, destination_file_name
        )
    )
# [END storage_download_file]

#download house dataset
download_blob('housing-prediction', 'Ames_HousePrice.csv', './data/raw/Ames_HousePrice.csv')

#download house dataset
download_blob('housing-prediction', 'Ames Real Estate Data.csv', './data/raw/Ames Real Estate Data.csv')
