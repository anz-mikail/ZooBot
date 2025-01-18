__all__ = ("router", )

from aiogram import Router

from .path import router as path_router

router = Router()

router.include_router(path_router)
