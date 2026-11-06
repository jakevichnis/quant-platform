import logging

def get_logger(service_name):
    logger = logging.getLogger(service_name)        # gives one named logger per service, so the log shows where a line came from
    if not logger.handlers:         # check stops it from adding a second handler if the function is called twice
        handler = logging.StreamHandler()
        handler = handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ))      # time, severity, service name, and message on each line
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

