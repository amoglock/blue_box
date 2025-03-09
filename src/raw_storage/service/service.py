from src.raw_storage.models.models import Raw, ResponseModel, IncomingRaw
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    """
    Class for service
    """
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()
        self.groups = self._get_all_raw_models()

    async def _get_all_raw_models(self) -> dict[str, Raw]:
        """Get all models from Raw"""
        groups = dict((subclass.__name__, subclass) for subclass in Raw.__subclasses__())
        return groups

    async def arrival_raw(self, raw: IncomingRaw) -> ResponseModel:
        # TODO: Add try-except for KeyError
        incoming_raw = self.groups[raw.group.title()].model_validate(raw)
        await self.raw_repository.add_raw(incoming_raw)

        self.response.data = raw
        self.response.message = f"Item {raw.title} in amount {raw.incoming_amount} added successful"

        return self.response
    
    async def get_all_storage(self) -> ResponseModel:
        self.response.data = await self.raw_repository.get_all_storage()
        return self.response

    async def get_storage(self, name: str, group: str) -> ResponseModel:

        self.response.data = await self.raw_repository.get_storage(name.lower(), self.groups[group])

        if self.response.data is None:
            self.response.status = False
            self.response.message = f"Item {name} not found"

        return self.response
