import time
import random

from sqlalchemy import create_engine

db_name = 'source_links'
db_user = 'pgs'
db_pass = '123456'
db_host = '172.17.0.2'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT links " + \
            "FROM source_links " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" + \
            "LIMIT 1"

    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]


if __name__ == '__main__':
    print('Application started')
    while True:
        print('The last value insterted is: {}'.format(get_last_row()))
        time.sleep(5)
