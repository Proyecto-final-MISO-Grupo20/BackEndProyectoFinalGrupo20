from src.controllers import entrevistas_controller

router = lambda app: app.include_router(entrevistas_controller.router)
