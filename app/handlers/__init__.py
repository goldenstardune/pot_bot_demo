from aiogram import Router

# podroutery
from .start import router as start_router
from .register.first_name import router as first_name_router
from .register.second_name import router as second_name_router
from .register.number import router as number_router
from app.captcha import router as captcha_router

# gl router
router = Router(name="main_handlers_router")
router.include_router(start_router)
router.include_router(first_name_router)
router.include_router(second_name_router)
router.include_router(number_router)
router.include_router(captcha_router)

__all__ = ["router"]