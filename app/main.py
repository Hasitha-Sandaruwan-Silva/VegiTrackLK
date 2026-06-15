"""
app/main.py
============
VegiTrack LK - FastAPI Application Entry Point
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logger import logger


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Root
    @app.get("/", tags=["Root"])
    def root():
        return {
            "service": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "docs":    "/docs",
            "health":  f"{settings.API_V1_STR}/health",
        }

    @app.on_event("startup")
    async def startup_event():
        logger.info("=" * 50)
        logger.info("%s v%s starting...", settings.PROJECT_NAME, settings.VERSION)
        logger.info("Docs: http://localhost:8000/docs")
        logger.info("=" * 50)

    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("%s shutting down.", settings.PROJECT_NAME)

    return app


app = create_app()