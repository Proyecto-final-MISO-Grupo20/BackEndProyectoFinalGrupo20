from src.controllers import grades_controller

router = lambda app: app.include_router(grades_controller.router)
