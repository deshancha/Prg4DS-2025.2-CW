from dataclasses import asdict
import aiofiles
import json
from domain.manager.isave_file import ISaveFile, T
from typing import List

class SaveFileImp(ISaveFile):
    async def saveJson(self, data: List[T], filename: str):
        serializable = [
            asdict(item) if not isinstance(item, dict) else item for item in data
        ]
        async with aiofiles.open(filename, "w") as f:
            await f.write(json.dumps(serializable, indent=4))