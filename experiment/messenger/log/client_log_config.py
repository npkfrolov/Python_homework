import logging

msngr_log = logging.getLogger('mssngr.client')
msngr_log.setLevel(logging.DEBUG)
_format = logging.Formatter("%(asctime)s %(levelname)-10s %(module)-10s %(message)s")
my_file_handler = logging.FileHandler("app.log")
my_file_handler.setLevel(logging.DEBUG)
my_file_handler.setFormatter(_format)
msngr_log.addHandler(my_file_handler)