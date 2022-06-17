import json

import os
from pathlib import Path

from utils.dot_dict import DotDict
from utils.singleton import Singleton


class Config(DotDict, metaclass=Singleton):

    def __init__(self):
        self.config_path = os.path.join(str(Path(os.path.abspath(__file__)).parent.parent),
                                        "config.json")
        config_data = self.read_config(self.config_path)
        super().__init__(DotDict(config_data))

    @staticmethod
    def read_config(config_path: str) -> dict:
        with open(config_path, encoding="utf-8") as file:
            config_data = json.load(file)
        return config_data
