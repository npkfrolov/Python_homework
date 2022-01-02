import logging.handlers

msngr_log = logging.getLogger("mssngr.server")
msngr_log.setLevel(logging.DEBUG)
_format = logging.Formatter("%(asctime)s %(levelname)-10s %(module)-10s %(message)s")
my_file_handler = logging.handlers.TimedRotatingFileHandler("app.log", when="D", interval=1)
my_file_handler.setLevel(logging.DEBUG)
my_file_handler.setFormatter(_format)
msngr_log.addHandler(my_file_handler)

