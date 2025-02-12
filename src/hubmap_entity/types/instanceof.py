# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Instanceof"]


class Instanceof(BaseModel):
    instanceof: Optional[bool] = None
    """True of False depending on whether the Entity id is an instance of the type"""
