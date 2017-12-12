import logging


def get_logger(logfile):
    log_format = '%(asctime)s %(filename)s:%(lineno)s - %(funcName)20s() %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        filename=logfile,
                        format=log_format,
                        filemod='w')

    formatter = logging.Formatter(log_format)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    return logging.getLogger()