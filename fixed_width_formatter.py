import logging


class FixedWidthFormatter(logging.Formatter):
    def format(self, record):
        level = f"{record.levelname}:".ljust(9)  # "INFO:" → "INFO:    "
        msg = super().format(record)
        return msg.replace(f"{record.levelname}:", level, 1)
