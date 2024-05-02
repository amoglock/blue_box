from src.raw_storage.models.models import IncomingRaw, ResponseModel, Vegetables, Meat, Gastronomy
from src.raw_storage.repository.repository import RawRepository


class RawStorageService:
    """
    Class for service
    """
    def __init__(self):
        self.raw_repository = RawRepository()
        self.response = ResponseModel()
        # TODO: It's boolshit)))). self.groups needs to create not from hardcoded dict.
        self.groups = {"Vegetables": Vegetables, "Meat": Meat, "Gastronomy": Gastronomy}

    async def arrival_raw(self, raw: IncomingRaw):
        # TODO: Add try-except for KeyError
        incoming_raw = self.groups[raw.group.title()].model_validate(raw)
        await self.raw_repository.add_raw(incoming_raw)

        self.response.data = raw
        self.response.message = f"Item {raw.title} in amount {raw.incoming_amount} added successful"

        return self.response

    async def get_storage(self, name: str, group: str):
        item_from_base = await self.raw_repository.get_storage(name, self.groups[group.title()])

        if name and not item_from_base:
            self.response.status = False
            self.response.message = f"Item {name} not found"
            return self.response

        if name:
            # self.response.data = IncomingRaw.model_validate(item_from_base)
            print(item_from_base)
            return self.response

        self.response.message = "No item for search"
        self.response.data = item_from_base
        return self.response
