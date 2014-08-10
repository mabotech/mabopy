
"""
test case for pg
"""

import unittest

from mabo.database import pg

class TestPg(unittest.TestCase):
    """
    test pg
    """
    def setUp(self):
        
        conn_str = "port=6432 dbname=maboss user=mabotech password=mabouser"
        
        self.dbi = pg.PostgresProxy(conn_str)

    def test_conn(self):

        self.dbi.execute("select 1")
        rtn = self.dbi.fetchone()
        print(rtn)
        assert rtn == (1,)
        
    def test_func(self):
        
        self.dbi.execute("select * from mt_co_test1()")
        
        print (self.dbi.fetchone()[0])
        
        assert True
        

        
if __name__ == "__main__":
    
    unittest.main()