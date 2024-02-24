from pydantic import BaseModel

class myCollections(BaseModel):
    ID:int=0
    Autor:str
    Descripcion:str
    FechaEstreno:str