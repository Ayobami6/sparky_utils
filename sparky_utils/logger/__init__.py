import logging
import logging.config
from pathlib import Path
from dataclasses import dataclass
from django.utils.log import DEFAULT_LOGGING


@dataclass
class LoggerConfig:
    log_level: str = logging.INFO
    log_format: str = "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
    log_date_format: str = "%Y-%m-%d %H:%M:%S"
    base_dir: str = Path(__file__).resolve().parent.parent

    def __post__init(self):
        self.__configure_logger()

    def __configure_logger(self):
        try:
            logging.config.dictConfig(
                {
                    "version": 1,
                    "disable_existing_loggers": False,
                    "formatters": {
                        "console": {
                            "format": self.log_format,
                        },
                        "file": {
                            "format": self.log_format,
                        },
                        "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
                    },
                    "handlers": {
                        "console": {
                            "level": self.log_level,
                            "class": "logging.StreamHandler",
                            "formatter": "console",
                        },
                        "file": {
                            "level": self.log_level,
                            "class": "logging.handlers.RotatingFileHandler",
                            "formatter": "file",
                            "filename": self.base_dir / "logs" / "app.log",
                            "maxBytes": 1024 * 1024 * 10,  # 5 MB
                            "backupCount": 5,
                        },
                        "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
                    },
                    "loggers": {
                        "": {
                            "level": self.log_level,
                            "handlers": ["console", "file"],
                            "propagate": False,
                        },
                        "apps": {
                            "level": self.log_level,
                            "handlers": ["console", "file"],
                            "propagate": False,
                        },
                    },
                    "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
                }
            )

        except Exception as e:
            print(f"Failed to load logging configuration: {e}")