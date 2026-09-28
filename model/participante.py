from pydantic import BaseModel, EmailStr, Field


class ParticipanteBase(BaseModel):
    nome: str = Field(..., min_length=1)
    email: EmailStr
    curso: str = Field(..., min_length=1)


class Participante(ParticipanteBase):
    id: int
