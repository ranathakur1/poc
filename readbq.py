from google.cloud import bigquery
import pandas as pd
from google.cloud import storage


def writeRecordToDb():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of table to append to.
    table_id = "glowing-harmony-291618.1234.table1"

    rows_to_insert = [
        {u"x": 10, u"y": 5,u"z": 1},
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

    sql = """
    SELECT sku, title
    FROM `glowing-harmony-291618.1234.pddinput`
    LIMIT 100
    """
    df2=pd.read_gbq(sql)
    print(df2)
    df2.to_csv('file1.csv')

    bucket_name = "glowing-harmony-291618input"
    source_file_name = "file1.csv"
    destination_blob_name = "file1.csv"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)


if __name__ == '__main__':
    writeRecordToDb()