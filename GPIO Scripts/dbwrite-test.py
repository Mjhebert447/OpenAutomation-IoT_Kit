#!/usr/bin/python3

import mariadb
import time

def logindb():
    print('chkdb placeholder')
    try:
        conn1 = mariadb.connect(
            user='controlapp',
            password="demopass123",
            host="localhost",
            port=3306,
            database="test"
        )
    
    
        print('connection successful')
        
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        raise RuntimeError
    
    #cur.execute()
    
    cur = conn1.cursor()
    cur.execute("SELECT * FROM JOB_ENTRY")
    print([x[0] for x in cur.description])
    for row in cur:
        print(row)
        
    #conn1.close()
    

#def tabletest()
 #   logindb()
  ##  cur.execute(execute)
    
def timeprt():
    tst_time = time.time()
    print(tst_time)
    form_time = tst_time//1
    print(form_time)
    cond_time = form_time/60
    print(cond_time)
    
logindb()
timeprt()
