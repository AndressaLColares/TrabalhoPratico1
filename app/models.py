from pydantic import BaseModel

class Item(BaseModel):
    id: int
    reino: str
    filo: str
    classe: str
    ordem: str
    familia: str
    genero: str
    especie: str