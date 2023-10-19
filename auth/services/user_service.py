from models.usuario import Usuario
from helpers.utils import object_as_dict


def get_auth_by_id(id: int):
    message: str = ''
    status: int = 200
    try:
        user = Usuario.find_by_id(id)
        message = object_as_dict(user)
    except Exception as e:
        status = 400
        message = {'Error': "El token no es válido o está vencido."}

    return message, status
