from domain.manager.isave_file import ISaveFile, T
from typing import List

class SaveDataUseCases:
    def __init__(
            self,
            isaveFile: ISaveFile):
        self.isaveFile = isaveFile

    async def saveJson(self, listData: List[T], filename: str):
        return await self.isaveFile.saveJson(listData, filename)
    