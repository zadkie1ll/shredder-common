import sys
import logging
import logging.handlers
from pathlib import Path
from typing import Optional
from common.fixed_width_formatter import FixedWidthFormatter


def setup_logger(
    filename: str, level: Optional[int] = logging.INFO, format: Optional[str] = None
):
    log_dir = Path("log")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / filename

    default_format = "[%(asctime)s][%(name)s] %(levelname)s: %(message)s"
    formatter = FixedWidthFormatter(format if format is not None else default_format)
    stdout_handler = logging.StreamHandler(sys.stdout)
    rotate_file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=log_path, when="midnight"
    )
    rotate_file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)
    logging.basicConfig(level=level, handlers=[stdout_handler, rotate_file_handler])
