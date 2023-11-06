from fastapi import HTTPException
from http import HTTPStatus

from src.dtos import CreateEmpleadoDto, AsociateEmpleadoDto, ResponseDto
from src.models import Empresa,  Empleado, Proyecto_Empleado


async def create_empleado(data: CreateEmpleadoDto, user_id: int) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.CREATED

    data_keys = [key for key in data]
    empleado_keys = CreateEmpleadoDto.get_attributes(None)

    if not all(key in data_keys for key in empleado_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        # Se obtiene la empresa por medio del usuario
        empresa = await Empresa.findByUserId(user_id)
        if not empresa:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El usuario no tiene el ROL para agregar un Empleado.'}
        else:
            print('--------------------------------1')
            print(empresa.id)
            empleado = Empleado(nombre=data.get('nombre'),
                          tipo_documento=data.get('tipo_documento'), documento=data.get('documento'),
                          cargo=data.get('cargo'), email=data.get('email'),
                          empresaId=empresa.id)
            print('--------------------------------2')
            await empleado.save()
            print('--------------------------------3')
            body = "Se agrego el empleado correctamente"
            
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)

    return ResponseDto(body, status_code)

async def asociar_empleado_proyecto(data: AsociateEmpleadoDto) -> ResponseDto:
    body: str or dict = ''
    status_code: int = HTTPStatus.OK

    data_keys = [key for key in data]
    empleado_keys = AsociateEmpleadoDto.get_attributes(None)
    
    if not all(key in data_keys for key in empleado_keys):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail='The request not contains all required data')
    try:
        # Se obtiene la empresa por medio del usuario
        proyecto_empleado = await Proyecto_Empleado.findByProjectEmployed(data.get('proyectoId'), data.get('empleadoId'))
        if proyecto_empleado:
            status_code=HTTPStatus.BAD_REQUEST
            body= {'detail':'El empleado ya esta asociado al proyecto'}
        else:
            proyecto_empleado = Proyecto_Empleado(proyectoId=data.get('proyectoId'), empleadoId=data.get('empleadoId'))
            await proyecto_empleado.save()
            body = "Se asocio el empleado correctamente"
            
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e)

    return ResponseDto(body, status_code)
