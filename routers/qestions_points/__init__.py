__all__ = ("router", )

from aiogram import Router

from .points import router as point_router

router = Router()

router.include_router(point_router)
