from src.raw_storage.models.models import Raw


class RawStorageService:
    def __init__(self):
        self.storage = {}

    async def arrival_raw(self, raw: Raw):
        self.storage[raw.title] = raw
        return self.storage
