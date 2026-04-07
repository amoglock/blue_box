from sqlmodel import SQLModel, Field

class Semiproduct(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(...)  # добавляем Field для явного определения
    source_raw: int = Field(...)  # добавляем Field для явного определения
    semiproduct_amount: int = Field(...)  