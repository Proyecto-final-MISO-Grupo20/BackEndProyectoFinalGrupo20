from src.controllers import proyecto_controller

router = lambda app: app.include_router(proyecto_controller.router)
