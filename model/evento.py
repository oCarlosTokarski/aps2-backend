from datetime import date, time
from pydantic import BaseModel, Field


class EventoBase(BaseModel):
    titulo: str = Field(..., min_length=1)
    descricao: str = Field(..., min_length=1)
    data: date
    horario: time
    local: str = Field(..., min_length=1)
    capacidade: int = Field(..., gt=0)
    categoria: str = Field(..., min_length=1)


class Evento(EventoBase):
    id: int
