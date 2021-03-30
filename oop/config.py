import logging
from pathlib import Path
import yaml


class Config:
    @staticmethod
    def open_config_file():
        try:
            with open(r'config.yaml') as configfile:
                config_file = yaml.load(configfile, Loader=yaml.FullLoader)
            return config_file
        except FileNotFoundError:
            logging.warning("The config file's missing")
            return Path.home() / 'config.yaml'
