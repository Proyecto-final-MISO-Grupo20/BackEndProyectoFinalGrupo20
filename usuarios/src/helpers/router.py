from src.controllers import usuario_controller

router = lambda app: app.include_router(usuario_controller.router)