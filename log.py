import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler('db.log')
fmtr = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fmtr)
logger.addHandler(fh)

class Log:
    def log_read():
        logger.info(f"User reading the data ")
    def log_connection(flag):
        if flag:
            logger.info("Connected")
        else:
            logger.info("Not Connected")
    def log_close(flag):
        if flag:
            logger.info("connection is closed")
        else:
            logger.info("connection is not closed")
    def read_log():
       with open('db.log','r') as f:
        data = f.readlines() 
        f.close()
        return data
