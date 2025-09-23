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

        # unicode escaping is need to save readable : eg : "price": "£51.77" vs "price": "\u00a351.77",
        async with aiofiles.open(filename, "w", encoding="utf-8") as f:
            await f.write(json.dumps(serializable, ensure_ascii=False, indent=4))