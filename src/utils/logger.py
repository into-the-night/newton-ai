import logging

from settings import Config

def setup_logging():
    log_level = getattr(logging, Config.LOG_LEVEL.upper(), logging.DEBUG)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(), 
            logging.FileHandler("app.log")
        ],
    )