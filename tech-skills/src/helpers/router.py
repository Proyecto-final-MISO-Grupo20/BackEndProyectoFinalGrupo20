from src.controllers import skill_controller

router = lambda app: app.include_router(skill_controller.router)
