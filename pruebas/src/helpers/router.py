from src.controllers import prueba_controller

router = lambda app: app.include_router(prueba_controller.router)
