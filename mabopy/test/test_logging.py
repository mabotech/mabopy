

from flask.config import Config

from mabo.utils.logging_factory import get_logger

import unittest

class TestLogging(unittest.TestCase):
    
    def setUp(self):
    
        tmp = '../config/logging_config.py'
        
        
        log_cfg = Config('')

        log_cfg.from_pyfile(tmp)    
       
        self.logging_cfg = log_cfg['LOGGING']        
        
        
    
    
    def test_logging(self):
        
    
        app = "app2"
       
        logger = get_logger(app, '', self.logging_cfg)
       
        logger.debug(app+':debug log')
        logger.warning(app+':warning log')
        logger.error(app+':error log')
        logger.info(app+':info log')
        
    def test_perf_logging(self):
        
        perf = get_logger('performance', '', self.logging_cfg)
        
        perf.debug("info")
        
        
if __name__ == "__main__":
    
    unittest.main()    
 
    
    