import os
from typing import Optional

from models.exportobject import ExportObject, ExportObjectJSONDecoder
import json


WORLD_FILE_NAME = 'default_map.txt'


def _load_from_file() -> Optional[ExportObject]:
    if os.stat(WORLD_FILE_NAME).st_size != 0:
        with open(WORLD_FILE_NAME, 'r') as myfile:
            loaded_dict = json.load(cls=ExportObjectJSONDecoder, fp=myfile)
            return ExportObject(**loaded_dict)
    else:
        return None


memoryCache: ExportObject = _load_from_file()
