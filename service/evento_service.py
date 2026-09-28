from fastapi import HTTPException, status

from model.evento import Evento, EventoBase
from model.participante import Participante


eventos = []
inscricoes = []

proximo_id = 1


def criar_evento(dados: EventoBase):
    global proximo_id

    evento = Evento(
        id=proximo_id,
        **dados.model_dump()
    )

    eventos.append(evento)
    proximo_id += 1

    return evento


def listar_eventos():
    return eventos


def buscar_evento(evento_id: int):
    for evento in eventos:
        if evento.id == evento_id:
            return evento

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Evento não encontrado."
    )


def atualizar_evento(evento_id: int, dados: EventoBase):
    evento = buscar_evento(evento_id)

    evento.titulo = dados.titulo
    evento.descricao = dados.descricao
    evento.data = dados.data
    evento.horario = dados.horario
    evento.local = dados.local
    evento.capacidade = dados.capacidade
    evento.categoria = dados.categoria

    return evento


def excluir_evento(evento_id: int):
    evento = buscar_evento(evento_id)

    eventos.remove(evento)

    inscricoes[:] = [
        inscricao
        for inscricao in inscricoes
        if inscricao["evento_id"] != evento_id
    ]


def inscrever_participante(
    evento_id: int,
    participante_id: int,
    participantes: list[Participante]
):
    evento = buscar_evento(evento_id)

    participante = None

    for p in participantes:
        if p.id == participante_id:
            participante = p
            break

    if participante is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Participante não encontrado."
        )

    for inscricao in inscricoes:
        if (
            inscricao["evento_id"] == evento_id
            and inscricao["participante_id"] == participante_id
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Participante já está inscrito neste evento."
            )

    total_inscritos = sum(
        1
        for inscricao in inscricoes
        if inscricao["evento_id"] == evento_id
    )

    if total_inscritos >= evento.capacidade:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não existem vagas disponíveis para este evento."
        )

    nova_inscricao = {
        "evento_id": evento_id,
        "participante_id": participante_id
    }

    inscricoes.append(nova_inscricao)

    return {
        "detail": "Participante inscrito com sucesso."
    }


def listar_inscritos(
    evento_id: int,
    participantes: list[Participante]
):
    buscar_evento(evento_id)

    participantes_inscritos = []

    for inscricao in inscricoes:
        if inscricao["evento_id"] == evento_id:
            for participante in participantes:
                if participante.id == inscricao["participante_id"]:
                    participantes_inscritos.append(participante)

    return participantes_inscritos
