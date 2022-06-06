import logging
logger=logging.getLogger(__name__)
"""logger.propagate=False
logger.info("hello from helper")
"""
#log handlers
#create log handler
stream_h=logging.StreamHandler()
file_h=logging.FileHandler("file.log")

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter("%(name)s-%(levelname)s-%(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)


#adding log handler
logger.addHandler(stream_h)
logger.addHandler(file_h)


logger.warning("This is a warning")
logger.error("This is an Error")