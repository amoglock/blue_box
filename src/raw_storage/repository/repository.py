from src.raw_storage.models.models import Raw


class RawRepository:

    storage = {}

    async def add_raw(self, raw: Raw) -> Raw:
        self.storage[raw.title] = raw
        return raw

    async def get_storage(self, name):
        if name:
            return self.storage[name]
        return self.storage
