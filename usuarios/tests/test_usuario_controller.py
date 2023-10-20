import pytest
import json
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app 
from unittest.mock import patch, AsyncMock
# Crea un cliente de prueba para la aplicación FastAPI
client = TestClient(app)

# Importa el controlador y la función de servicio
from src.controllers.usuario_controller import create_candidato  
from src.services.usuario_service import create_candidato as real_create_candidato  

@patch('src.controllers.usuario_controller.create_candidato', new_callable=AsyncMock)
def test_create_candidato_controller(mock_create_candidato):
    # Configura el mock para que devuelva una respuesta simulada
    mock_create_candidato.return_value.status_code = 201
    mock_create_candidato.return_value.json.return_value = {"message": "Usuario creado"}

    # Datos de prueba para el usuario
    usuario_data = {
        "nombre": "Juan Jose Ochoa Ortiz",
        "tipo_documento": 1,
        "documento": "1234567",
        "username": "juanochoa",
        "password": "password",
        "email": "ejemplo@ejemplo.com",
        "fecha_nacimiento": 20230601,
        "telefono": 123456,
        "pais": "Colombia",
        "ciudad": "Bogota"
    }

    # Llamada al controlador para crear un usuario
    response = client.post('/usuario/candidato', data=json.dumps(usuario_data))

    # Verifica que la respuesta tenga un código de estado 400
    assert response.status_code == 400

def test_ping():
    # Realiza una solicitud GET al endpoint /ping
    response = client.get('/usuario/ping')

    # Verifica que la respuesta tenga un código de estado 200 (OK)
    assert response.status_code == 200

# Ejecutar la prueba
if __name__ == '__main__':
    pytest.main()
