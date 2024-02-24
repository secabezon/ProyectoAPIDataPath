from fastapi import APIRouter
from controllers.movie_controllers import router as collection_router

router = APIRouter()
router.include_router(collection_router)
