"""VERITAS API error types and safe exception handlers."""

from __future__ import annotations

from typing import Any

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.schemas import ErrorDetail, ErrorResponse


class VeritasError(Exception):
    """Base application error intended for a controlled API response."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        status_code: int = 400,
        field: str | None = None,
    ) -> None:
        super().__init__(message)

        self.code = code
        self.message = message
        self.status_code = status_code
        self.field = field


def _error_response(
    *,
    status_code: int,
    code: str,
    message: str,
    field: str | None = None,
) -> JSONResponse:
    payload = ErrorResponse(
        error=ErrorDetail(
            code=code,
            message=message,
            field=field,
        )
    )

    return JSONResponse(
        status_code=status_code,
        content=payload.model_dump(mode="json"),
    )


async def veritas_error_handler(
    _: Request,
    exc: VeritasError,
) -> JSONResponse:
    """Return a controlled application error without exposing internals."""

    return _error_response(
        status_code=exc.status_code,
        code=exc.code,
        message=exc.message,
        field=exc.field,
    )


def _safe_validation_field(
    location: tuple[Any, ...],
) -> str | None:
    """Return only the request field path, never the submitted value."""

    fields = [
        str(item)
        for item in location
        if item not in {"body", "query", "path", "header"}
    ]

    return ".".join(fields) or None


async def validation_error_handler(
    _: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Convert validation errors into a safe API envelope."""

    errors = exc.errors()

    first_error = errors[0] if errors else {}

    field = _safe_validation_field(
        tuple(first_error.get("loc", ()))
    )

    return _error_response(
        status_code=422,
        code="VALIDATION_ERROR",
        message="The request could not be validated.",
        field=field,
    )


async def unhandled_error_handler(
    _: Request,
    __: Exception,
) -> JSONResponse:
    """Return a generic error without exposing implementation details."""

    return _error_response(
        status_code=500,
        code="INTERNAL_ERROR",
        message="An unexpected server error occurred.",
    )
