from sqlmodel import Session, select
from src.database import engine
from src.raw_storage.models.database_models import Meat, Raw, Vegetables
from src.semiproducts.models.models import Semiproduct

class SemiproductRepository:
    """
    """
    def __init__(self):
        self.engine = engine

    async def create_semiproduct(self, new_semiproduct: Semiproduct):
        with Session(self.engine) as session:
            raw = select(Vegetables).where(Vegetables.id == 1)
            result = session.exec(raw).first()
            print(new_semiproduct)
            new_semiproduct.source_raw = result.id
            session.add(new_semiproduct)
            session.commit()


    async def get_all_semiproducts(self):
        #TODO fixme!!!!!
        with Session(self.engine) as session:
            statement = select(Meat).where(Meat.title=='beef')
            result = session.exec(statement).first()    
            return result 