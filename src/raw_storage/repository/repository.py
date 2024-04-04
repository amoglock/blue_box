from src.raw_storage.models.models import IncomingRaw


class RawRepository:
    storage = {}

    # async def add_raw(self, raw: IncomingRaw) -> IncomingRaw:
    #     self.storage[raw.title] = raw
    #     return raw

    async def get_storage(self, name):
        """

        :param name:
        :return:
        """
        if name:
            return self.storage.get(name)
        return self.storage
