import logging.config
from sparky_utils.logger import LoggerConfig
import logging
from pathlib import Path
from logging.config import dictConfig

base_dir = Path(__file__).resolve().parent.parent

logger_config = LoggerConfig(log_level=logging.INFO)


def test_logger_config_log_level():
    assert logger_config.log_level == logging.INFO


def test_logger_config_log_file_path():
    assert str(logger_config.base_dir) == str(base_dir) + "\sparky_utils"


def test_logger_config_an_instance_of_logging_config():
    assert isinstance(logger_config, LoggerConfig)


def test_logger_info():
    logger = logging.getLogger(__name__)
    logger.info("This is a test info message")
    assert hasattr(logger, "handlers")


def test_logger_correctly_log(caplog):
    logger = logging.getLogger(__name__)
    with caplog.at_level(logging.INFO):
        logger.info("This is a test info message")

    # Check if the message was logged
    assert (
        "This is a test info message" in caplog.text
    ), "The log message was not captured"

    assert len(caplog.records) == 1, "Unexpected number of log records"
    assert caplog.records[0].levelname == "INFO", "The log level is incorrect"
    assert (
        caplog.records[0].message == "This is a test info message"
    ), "The log message content is incorrect"
