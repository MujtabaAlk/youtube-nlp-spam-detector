from __future__ import annotations

from typing import TypedDict


class ErrorResponse(TypedDict):
    error: _Error


class _Error(TypedDict):
    errors: list[_ErrorObject]
    code: int
    message: str


class _ErrorObject(TypedDict):
    domain: str
    reason: str
    message: str
    locationType: str
    location: str
