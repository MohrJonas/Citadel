from logging import Formatter, Logger, FileHandler, StreamHandler, getLogger, DEBUG, basicConfig

def create_logger(file_name: str) -> Logger:
    logging_formatter = Formatter("%(asctime)s %(message)s")
    logger = getLogger()
    basicConfig(level = DEBUG)

    file_handler = FileHandler(f"/var/log/citadel/{file_name}.log")
    file_handler.setFormatter(logging_formatter)

    console_handler = StreamHandler()
    console_handler.setFormatter(logging_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger