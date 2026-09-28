from fastapi import HTTPException, status

from model.participante import Participante, ParticipanteBase


participantes = []

proximo_id = 1


def criar_participante(dados: ParticipanteBase):
    global proximo_id

    participante = Participante(
        id=proximo_id,
        **dados.model_dump()
    )

    participantes.append(participante)
    proximo_id += 1

    return participante


def listar_participantes():
    return participantes


def buscar_participante(participante_id: int):
    for participante in participantes:
        if participante.id == participante_id:
            return participante

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Participante não encontrado."
    )


def atualizar_participante(
    participante_id: int,
    dados: ParticipanteBase
):
    participante = buscar_participante(participante_id)

    participante.nome = dados.nome
    participante.email = dados.email
    participante.curso = dados.curso

    return participante


def excluir_participante(participante_id: int):
    participante = buscar_participante(participante_id)

    participantes.remove(participante)
