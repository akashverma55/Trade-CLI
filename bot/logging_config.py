from loguru import logger
import sys

def setup_logger():
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}"
    )

    logger.add(
        "bot.log",
        rotation="5 MB",
        format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    return logger