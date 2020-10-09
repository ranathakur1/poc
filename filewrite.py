import tempfile
from google.cloud import storage


def my_function(greet):
    print("@@@The transformation process@@@ count is:" + greet)


def creWrtUpldFile():
    obj = open("pddinput.csv", "w+")
    obj.write("sku, title \n")
    obj.write("sku2020, clock")
    obj.close()
    print("file created and data entered")
    client = storage.Client()

    bucket_name = "glowing-harmony-291618input"
    source_file_name = "pddinput.csv"
    destination_blob_name = "pddinput.csv"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)


if __name__ == '__main__':
    my_function("Trasformed")
    creWrtUpldFile()