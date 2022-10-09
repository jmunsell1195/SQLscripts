import psycopg2 as pg
import csv
import os

## Get directory of desktop for specific machine the script is running on
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

## Connect to database module
conn = pg.connect(database='module',user='jeremy',password='1195Eldorado')
## Setup cursor object to interact with database
curr = conn.cursor()

## Get a list of tables in the database
query = 'SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\''
curr.execute(query)
tabs = [tup[0] for tup in curr.fetchall() if 'Force' in tup[0] and 'vector' not in tup[0]]

for tab in tabs:
    ## Create list of users for each data table
    user_query = 'SELECT DISTINCT(\"{}\".user)'.format(tab)+ 'FROM' + ' \"{}\"'.format(tab)
    curr.execute(user_query)
    users = [user[0] for user in curr.fetchall() if user[0] != '']

    ## Get column names from the table
    sch_query = 'SELECT column_name FROM information_schema.columns WHERE table_name = \'{}\''.format(tab)
    curr.execute(sch_query)
    cols = curr.fetchall()
    cols = [itm[0] for itm in cols]

    ## Get data from table pertaining to particular user
    for user in users:
        query = 'SELECT * FROM ' + '\"{}\"'.format(tab) + ' WHERE ' + '\"{}\"'.format(tab) +'.user = \'{}\''.format(user)
        curr.execute(query)
        res = curr.fetchall()
        itm = [tuple(cols)] + list(res)

        file = r"\data\{}".format(user)
        path = desktop + file + '\{}.csv'.format(tab)

        ## Make directory root\data\
        try:
            os.mkdir(desktop + '\data')
        ## pass if it already exists
        except:
            pass
        ## make folder for each user
        try:
            os.mkdir(desktop + file)
        ## pass if already exists
        except:
            pass
        
        with open(path,'w',newline = '') as csvfile:
            wrtr = csv.writer(csvfile,delimiter=',')
            for row in itm:
                wrtr.writerow(row)