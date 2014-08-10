
import logging
import logging.handlers
import logging.config

def get_logger(app, logroot, logging_cfg):
    """
    create all logging files
    """

    logging_cfg['handlers']['debug']['filename'] = "".join([logroot, app, '_debug.log'])
    logging_cfg['handlers']['info']['filename'] = "".join([logroot, app, '_info.log'])
    logging_cfg['handlers']['warning']['filename'] = "".join([logroot, app, '_warning.log'])
    logging_cfg['handlers']['error']['filename'] = "".join([logroot, app, '_error.log'])
    logging_cfg['handlers']['performance']['filename'] = "".join([logroot, app, '_performance.log'])
    
    logging.config.dictConfig( logging_cfg )

    logger = logging.getLogger(app)
    
    return logger