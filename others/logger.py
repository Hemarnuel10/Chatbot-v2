import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Console output
#console_handler.setFormatter(formatter)

# File output
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

#logger.addHandler(console_handler)
logger.addHandler(file_handler)