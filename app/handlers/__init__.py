from aiogram import Router

from .start import router as start_router
from .register.start import router as register_start_router         
from .register.first_name import router as first_name_router
from .register.second_name import router as second_name_router
from .register.number import router as number_router
from app.captcha import router as captcha_router
from .register.security_question import router as security_question_router

router = Router(name="main_router")

router.include_router(start_router)
router.include_router(register_start_router)        
router.include_router(first_name_router)
router.include_router(second_name_router)
router.include_router(number_router)
router.include_router(captcha_router)
router.include_router(security_question_router)

__all__ = ["router"]
