from fastapi import APIRouter, Response, status

from model.participante import Participante, ParticipanteBase
from service import participante_service


router = APIRouter(
    prefix="/participantes",
    tags=["Participantes"]
)


@router.post(
    "",
    response_model=Participante,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_participante(dados: ParticipanteBase):
    return participante_service.criar_participante(dados)


@router.get(
    "",
    response_model=list[Participante],
    status_code=status.HTTP_200_OK
)
def listar_participantes():
    return participante_service.listar_participantes()


@router.get(
    "/{participante_id}",
    response_model=Participante,
    status_code=status.HTTP_200_OK
)
def consultar_participante(participante_id: int):
    return participante_service.buscar_participante(participante_id)


@router.put(
    "/{participante_id}",
    response_model=Participante,
    status_code=status.HTTP_200_OK
)
def atualizar_participante(
    participante_id: int,
    dados: ParticipanteBase
):
    return participante_service.atualizar_participante(
        participante_id,
        dados
    )


@router.delete(
    "/{participante_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_participante(participante_id: int):
    participante_service.excluir_participante(participante_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
