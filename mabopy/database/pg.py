# -*- coding: utf-8 -*-

"""
postgresql lib
"""

import psycopg2

class PostgresProxy(object):
    """
    PostgreSQL Database Driver
    """
    
    def __init__(self, conn_str):
        """
        init
        """
        self.conn = psycopg2.connect(conn_str)

        self.cur = self.conn.cursor()
       
    def execute(self, sql):
        """
        execute
        """
        try:
            #sql = sql.decode("utf-8", "ignore")
            self.cur.execute(sql)
        except Exception, ex:
            #print sql
            raise Exception(ex.message)

    def commit(self):
        """
        commit
        """
        self.conn.commit()
    
    def fetchone(self):
        """
        fetch one
        """
        return self.cur.fetchone()

    def fetchall(self):
        """
        fetch all
        """
        return self.cur.fetchall()

    def __del___(self):
        """
        close
        """
        
        self.cur.close()

        self.conn.close()
        
        


