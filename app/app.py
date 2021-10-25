from sqlalchemy import create_engine
from RSSFinder.RSS_Finder import RSS_Finder

db_name = 'RSS_DB'
db_user = 'nasir'
db_pass = '123456'
db_host = '172.23.0.2'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query ="SELECT * " + \
            "FROM Web_links " + \
            "LIMIT 4"

    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]


if __name__ == '__main__':

    link = get_last_row()
    print(link)
    rss = RSS_Finder('http://www.farsnews.ir').Find_Feeds()
