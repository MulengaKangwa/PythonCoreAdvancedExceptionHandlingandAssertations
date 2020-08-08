import logging

logging.basicConfig(filename="mylog.log",level=logging.debug)
logging.critical("Critical")
logging.error("Error")
logging.info("Information")
logging.debug("Debug")