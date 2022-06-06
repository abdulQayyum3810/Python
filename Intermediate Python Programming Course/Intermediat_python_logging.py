#there are five different levels of loging
import logging
#by default only message with level warning or higher are printed
#it can be changed using basic configuration
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
datefmt="%m/%d/%Y %H:%M:%S")
"""logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
"""
#it is good practice to make our own logger instead of root loggger
import helper
#see fileconfig and dictconfig later 