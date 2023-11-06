from src.controllers import offer_controller

router = lambda app: app.include_router(offer_controller.router)
