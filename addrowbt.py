import datetime
from google.cloud import bigtable
import pandas as pd

def write_simple():
    client = bigtable.Client(project='glowing-harmony-291618', admin=True)
    instance = client.instance('btable')
    table = instance.table('catalog')
    #print(table)

    df = pd.read_csv('gs://glowing-harmony-291618input/pddinput.csv')
    print(df.iloc[0,0])

    column_family_id = "descr"
    row_key = df.iloc[0,0]
    #row_key = "sku9875"

    row = table.direct_row(row_key)
    #print(row)

    column = "title"
    #value = "jacket"
    value=df.iloc[0,1]


    row = table.direct_row(row_key)
    row.set_cell(column_family_id,
                 column,
                 value,
                 timestamp=datetime.datetime.utcnow())
    row.commit()
    print("row inserted in bigtable")


if __name__ == '__main__':
    write_simple()