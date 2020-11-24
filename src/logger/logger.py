from src.config import LOG_LEVEL
import coloredlogs, logging
logger = logging.getLogger(__name__)


class Log:

    def __init__(self):
        coloredlogs.install(level=LOG_LEVEL, logger=logger)

    @staticmethod
    def log(*args, **kwargs):
        if not LOG_LEVEL:
            return

        log_func = logger
        if args[0] == 'i':
            log_func = log_func.info
        elif args[0] == 'd':
            log_func = log_func.debug
        elif args[0] == 'w':
            log_func = log_func.warning
        elif args[0] == 'er':
            log_func = log_func.error
        elif args[0] == 'c':
            log_func = log_func.critical
        elif args[0] == 'ex':
            log_func = log_func.exception

        if 'pp' in kwargs:
            from pprint import pprint
            pprint(*args, **kwargs)
        elif 'p' in kwargs:
            print(*args, **kwargs)
        else:
            if args[1:] is not None:
                format = (len(args) - 1) * "%s "
                log_func(format, *list(map(str, args[1:])), **kwargs)