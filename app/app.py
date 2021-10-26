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


def get_last_row(table , status):
    # Retrieve the last number inserted inside the 'numbers'
    query = "SELECT * " + \
            "FROM {0} ".format(table) + \
            "WHERE  status='{0}' OR status IS NULL ".format(status) + \
            "LIMIT 1"
    try:
        result_set = db.execute(query)
        for row in result_set:
            return row
    except Exception as e:
        print(e)
        return None


def Update_status(Id, status, table):
    """
    :param Id: where we want to status update
    """
    db.execute("update {2} set status='{0}' where link_id='{1}';".format(status, Id, table))
    print('Update ' + str(Id) + ' in status : ' + str(status))


def Update_RSS(Id, RSS):
    """
    :param Id: where get data
    """
    db.execute("update Web_links set rss='{0}' where id='{1}';".format(RSS, Id))
    print('Update ' + str(Id) + ' in RSS value : ' + str(RSS))


def Insert_RSS_Find(Id, rss):
    db.execute("INSERT INTO rss_fined (link_id ,rss , status) " + \
               "VALUES ({0} , '{1}' , 'find');".format(Id , rss))


def Process_On_read(Data, table):
    Update_status(Data[0], 'running', table)
    RSS_Data = RSSReader().Read_RSS(Data[2])
    if RSS_Data:
        print(RSS_Data)
        Update_status(Data[0], 'done', table)
    else:
        Update_status(Data[0], 'failed', table)


def Process_On_Find(Data, table):
    RSS_Links = RSS_Finder(Data[1]).Find_Feeds()
    if RSS_Links:
        [Insert_RSS_Find(Data[0], item[0]) for item in RSS_Links]
    else:
        Update_status(Data[0], "WRONG Link", table)


def Process_Links(Data, table):
    """
      Check if we do not have rss link in database
        if we have it so we just read rss from rss link
        if we do not have it so we find rss from link
            Check if come back rss then Update with true way
    :param Data:
    """
    if Data:
        if Data[2] not in ('None', None, 'NULL', ''):
            Process_On_read(Data, table)
        else:
            print('We do not have RSS')
            Process_On_Find(Data, table)


if __name__ == '__main__':
    # InsertFake()
    table_Links = 'Web_links'
    table_RSS_Find = 'RSS_Fined'
    while True:
        Data = get_last_row(table_Links , status='failed')
        Process_Links(Data , table_Links)

        Data_RSS_Find = get_last_row(table_RSS_Find , status='find')
        RSS_Content = Process_On_read(Data_RSS_Find ,table_RSS_Find)