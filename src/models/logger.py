import logging
import os

LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "app.log"))
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


def log_event(message):
    print(message)
    logger.info(message)
