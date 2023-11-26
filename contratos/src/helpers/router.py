from src.controllers import contrato_controller

router = lambda app: app.include_router(contrato_controller.router)
