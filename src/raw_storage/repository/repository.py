from src.raw_storage.models.models import Raw


class RawRepository:

    storage = []

    async def add_raw(self, raw: Raw) -> Raw:
        self.storage.append(raw)
        return raw

    async def get_storage(self):
        return self.storage
