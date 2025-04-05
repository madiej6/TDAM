import logging


def get_logger(module: str, level: int = logging.INFO):
    """Set up logger for the module.
    
    Args:
        module (str): the module for the logger (i.e. '__main__')
        level (int): the level of logging (i.e. logging.INFO or logging.WARNING)
    
    Returns:
        logger (logging.logger): the logger"""
    logger = logging.getLogger(module)
    logging.basicConfig()
    logger.setLevel(level)

    return logger