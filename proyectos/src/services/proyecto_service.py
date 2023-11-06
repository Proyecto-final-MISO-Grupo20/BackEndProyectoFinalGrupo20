from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import CreateProyectoDto, ResponseDto
from src.models import Usuario, Empresa, Proyecto
import json
import asyncio

async def create_proyecto(data: CreateProyectoDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    data_keys = [key for key in data]
    proyecto_keys = CreateProyectoDto.get_attributes(None)

    if not all(key in data_keys for key in proyecto_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        # Se obtiene la empresa por medio del usuario
        empresa = await Empresa.findByUserId(user_id)
        
        if not empresa:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El usuario no tiene el ROL para crear un Proyecto.'}
        else:

            proyecto = Proyecto(nombre=data.get('nombre'),
                          descripcion=data.get('descripcion'), codigo=data.get('codigo'),
                          empresaId=empresa.id)

            await proyecto.save()

            body = "Se agrego el proyecto correctamente"
            
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)

    return ResponseDto(body, status_code)

async def list_proyectos(user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    try:
        # Se obtiene la empresa por medio del usuario
        empresa = await Empresa.findByUserId(user_id)
        
        if not empresa:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El usuario no tiene el ROL para crear un Proyecto.'}
        else:
            body = await Proyecto.findByEmpresaId(empresa.id)
            
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)

    return ResponseDto(body, status_code)

