from sqlalchemy import create_engine
from RSSFinder.RSS_Finder import RSS_Finder

db_name = ''
db_user = ''
db_pass = ''
db_host = ''
db_port = ''

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "" + \
            "SELECT links , rss " + \
            "FROM web_links " + \
            "LIMIT 1"

    result_set = db.execute(query)
    for (r) in result_set:
        return r[0]


if __name__ == '__main__':

    link = get_last_row()
    print(link)
    rss = RSS_Finder('http://www.farsnews.ir').Find_Feeds()
