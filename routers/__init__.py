__all__ = ("router", )

from aiogram import Router

from .questions_path import router as paths_router
from .qestions_points import router as points_router

router = Router(name=__name__)

router.include_router(paths_router)
router.include_router(points_router)
