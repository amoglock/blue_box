class ProductService:

    async def create_product(self, name: str, **kwargs):
        print(name)
        for p in kwargs:
            print(p)
        return {"status": 200}
