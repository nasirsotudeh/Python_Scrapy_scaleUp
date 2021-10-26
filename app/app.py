from sqlalchemy import create_engine
from RSSFinder.RSS_Finder import RSS_Finder
from RSSReader.RSSReader import RSSReader
db_name = 'RSS_DB'
db_user = 'nasir'
db_pass = '123456'
db_host = '172.23.0.2'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)


def Insert():
    db.execute("INSERT INTO Web_links (links) " + \
               "VALUES ('http://www.farsnews.ir');")


def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = "SELECT * " + \
            "FROM Web_links " + \
            "WHERE  status='failed' OR status IS NULL " + \
            "LIMIT 1"
    try:
        result_set = db.execute(query)
        for row in result_set:
            return row
    except Exception as e:
        print(e)
        return None

def Update_status(Id, status):
    """
    :param Id: where get data
    """
    db.execute("update Web_links set status='{0}' where id='{1}';".format(status,Id))

def Update_RSS(Id, RSS):
    """
    :param Id: where get data
    """
    db.execute("update Web_links set rss='{0}' where id='{1}';".format(RSS,Id))


def Process_Links(Data):
    if Data:
        print(Data)
        if Data[2] not in ('None' , None , 'NULL' ,''):
            Update_status(Data[0], 'running')
            rss = RSSReader().Read_RSS(Data[2])
            print(rss)
            Update_status(Data[0], 'done')

        else:
            print('we do not have RSS')
            rss = RSS_Finder(Data[1]).Find_Feeds()
            Update_RSS(Data[0] , rss)
            print(rss)


if __name__ == '__main__':
    # Insert()
    while True:
        Data = get_last_row()
        Process_Links(Data)


