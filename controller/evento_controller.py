from fastapi import APIRouter, Response, status

from model.evento import Evento, EventoBase
from service import evento_service
from service.participante_service import participantes


router = APIRouter(
    prefix="/eventos",
    tags=["Eventos"]
)


@router.post(
    "",
    response_model=Evento,
    status_code=status.HTTP_201_CREATED
)
def cadastrar_evento(dados: EventoBase):
    return evento_service.criar_evento(dados)


@router.get(
    "",
    response_model=list[Evento],
    status_code=status.HTTP_200_OK
)
def listar_eventos():
    return evento_service.listar_eventos()


@router.get(
    "/{evento_id}",
    response_model=Evento,
    status_code=status.HTTP_200_OK
)
def consultar_evento(evento_id: int):
    return evento_service.buscar_evento(evento_id)


@router.put(
    "/{evento_id}",
    response_model=Evento,
    status_code=status.HTTP_200_OK
)
def atualizar_evento(evento_id: int, dados: EventoBase):
    return evento_service.atualizar_evento(evento_id, dados)


@router.delete(
    "/{evento_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_evento(evento_id: int):
    evento_service.excluir_evento(evento_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post(
    "/{evento_id}/inscricoes/{participante_id}",
    status_code=status.HTTP_201_CREATED
)
def realizar_inscricao(
    evento_id: int,
    participante_id: int
):
    return evento_service.inscrever_participante(
        evento_id,
        participante_id,
        participantes
    )


@router.get(
    "/{evento_id}/inscricoes",
    response_model=list
)
def consultar_inscritos(evento_id: int):
    return evento_service.listar_inscritos(
        evento_id,
        participantes
    )
